#!/usr/bin/env python3
import json
import mimetypes
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse


SAFE_RE = re.compile(r"[\\/:*?\"<>|]+")


def slug(text: str, fallback: str = "item", limit: int = 90) -> str:
    text = SAFE_RE.sub("_", (text or "").strip())
    text = re.sub(r"\s+", "_", text).strip("._ ")
    return (text[:limit] or fallback)


def infer_ext(path: Path, content_type: str, url: str) -> str:
    lower_url = urlparse(url).path.lower()
    for ext in [".pdf", ".docx", ".xlsx", ".pptx", ".zip", ".csv"]:
        if lower_url.endswith(ext):
            return ext
    ct = (content_type or "").split(";")[0].strip().lower()
    by_ct = {
        "application/pdf": ".pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
        "text/html": ".html",
        "text/plain": ".txt",
    }
    if ct in by_ct:
        return by_ct[ct]
    guessed = mimetypes.guess_extension(ct) if ct else None
    if guessed:
        return guessed
    try:
        head = path.read_bytes()[:16]
        if head.startswith(b"%PDF"):
            return ".pdf"
        if head.startswith(b"PK\x03\x04"):
            return ".zip"
        if b"<html" in head.lower() or b"<!doctype" in head.lower():
            return ".html"
    except OSError:
        pass
    return ".bin"


def candidate_urls(url: str):
    candidates = [url]
    if "arxiv.org/abs/" in url:
        arxiv_id = url.rstrip("/").split("/abs/", 1)[1]
        candidates.insert(0, f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    if "mdpi.com/" in url and not url.rstrip("/").endswith("/pdf"):
        candidates.insert(0, url.rstrip("/") + "/pdf")
    if "link.springer.com/article/" in url:
        doi = url.rstrip("/").split("/article/", 1)[1]
        candidates.insert(0, f"https://link.springer.com/content/pdf/{doi}.pdf")
    if "pmc.ncbi.nlm.nih.gov/articles/" in url:
        candidates.insert(0, url.rstrip("/") + "/pdf/")
    return list(dict.fromkeys(candidates))


def curl_download(url: str, output: Path):
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--compressed",
        "--retry",
        "2",
        "--connect-timeout",
        "15",
        "--max-time",
        "60",
        "-A",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36",
        "-o",
        str(output),
        "-w",
        "%{http_code}\t%{content_type}\t%{url_effective}",
        url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def download_one(index: int, item: dict, root: Path):
    source_kind = item.get("source_type", "")
    top = "01_Excel链接资料" if source_kind == "excel" else "02_Word补充资料"
    category = item.get("category") or "其他资料"
    target_dir = root / top / slug(category, "其他资料")
    target_dir.mkdir(parents=True, exist_ok=True)

    title = item.get("title") or item.get("context") or urlparse(item.get("url", "")).netloc
    base = slug(f"{index:03d}_{title}", f"{index:03d}_source")
    url = item.get("url", "")
    if not url:
        return {**item, "status": "skipped_no_url", "saved_path": "", "attempt_url": "", "error": "No URL"}

    last_error = ""
    for attempt_url in candidate_urls(url):
        tmp = target_dir / f"{base}.download"
        if tmp.exists():
            tmp.unlink()
        code, out, err = curl_download(attempt_url, tmp)
        if code != 0 or not tmp.exists() or tmp.stat().st_size == 0:
            last_error = (err or out or f"curl exit {code}")[-600:]
            if tmp.exists():
                tmp.unlink()
            continue
        parts = out.split("\t")
        http_code = parts[0] if len(parts) > 0 else ""
        content_type = parts[1] if len(parts) > 1 else ""
        effective_url = parts[2] if len(parts) > 2 else attempt_url
        ext = infer_ext(tmp, content_type, effective_url)
        final = target_dir / f"{base}{ext}"
        counter = 2
        while final.exists():
            final = target_dir / f"{base}_{counter}{ext}"
            counter += 1
        shutil.move(str(tmp), str(final))
        sidecar = final.with_suffix(final.suffix + ".source.txt")
        sidecar.write_text(
            "\n".join(
                [
                    f"title: {title}",
                    f"source_type: {source_kind}",
                    f"category: {category}",
                    f"original_url: {url}",
                    f"downloaded_url: {attempt_url}",
                    f"effective_url: {effective_url}",
                    f"http_code: {http_code}",
                    f"content_type: {content_type}",
                    f"context: {item.get('context', '')}",
                    f"location: {item.get('location', '')}",
                ]
            ),
            encoding="utf-8",
        )
        return {
            **item,
            "status": "downloaded",
            "saved_path": str(final),
            "attempt_url": attempt_url,
            "effective_url": effective_url,
            "http_code": http_code,
            "content_type": content_type,
            "error": "",
        }
    return {**item, "status": "failed", "saved_path": "", "attempt_url": url, "error": last_error}


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--supplement", required=True)
    parser.add_argument("--out-root", required=True)
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args()

    root = Path(args.out_root)
    meta = root / "_metadata"
    meta.mkdir(parents=True, exist_ok=True)
    base_items = [i for i in json.loads(Path(args.manifest).read_text(encoding="utf-8")) if i.get("url")]
    supplement_items = json.loads(Path(args.supplement).read_text(encoding="utf-8"))
    items = base_items + supplement_items
    (meta / "combined_download_manifest.json").write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(download_one, idx, item, root): (idx, item) for idx, item in enumerate(items, 1)}
        for fut in as_completed(futures):
            idx, item = futures[fut]
            try:
                result = fut.result()
            except Exception as exc:
                result = {**item, "status": "failed", "saved_path": "", "error": repr(exc)}
            results.append(result)
            print(f"{len(results)}/{len(items)} {result.get('status')} {result.get('title', '')[:80]}")

    results.sort(key=lambda r: (r.get("source_type", ""), r.get("title", ""), r.get("url", "")))
    (meta / "download_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    with (meta / "download_results.csv").open("w", encoding="utf-8") as f:
        headers = ["status", "source_type", "category", "title", "url", "saved_path", "error"]
        f.write(",".join(headers) + "\n")
        for row in results:
            f.write(",".join('"' + str(row.get(h, "")).replace('"', '""') + '"' for h in headers) + "\n")
    summary = {
        "total": len(results),
        "downloaded": sum(1 for r in results if r.get("status") == "downloaded"),
        "failed": sum(1 for r in results if r.get("status") == "failed"),
        "skipped": sum(1 for r in results if r.get("status", "").startswith("skipped")),
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
