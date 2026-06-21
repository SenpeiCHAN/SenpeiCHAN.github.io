#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import quote, urlparse


def slug(text: str, fallback: str = "snapshot", limit: int = 90) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "_", (text or "").strip())
    text = re.sub(r"\s+", "_", text).strip("._ ")
    return text[:limit] or fallback


def read_url(url: str, out: Path):
    reader_url = "https://r.jina.ai/http://r.jina.ai/http://" + url
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--compressed",
        "--connect-timeout",
        "15",
        "--max-time",
        "75",
        "-A",
        "Mozilla/5.0",
        "-o",
        str(out),
        reader_url,
    ]
    return subprocess.run(cmd, capture_output=True, text=True)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--out-root", required=True)
    args = parser.parse_args()

    root = Path(args.out_root)
    meta = root / "_metadata"
    results_path = Path(args.results)
    results = json.loads(results_path.read_text(encoding="utf-8"))
    snapshot_dir = root / "03_下载受限网页快照"
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    changed = []
    for idx, item in enumerate([r for r in results if r.get("status") == "failed"], 1):
        title = item.get("title") or urlparse(item.get("url", "")).netloc
        final = snapshot_dir / f"{idx:03d}_{slug(title)}.md"
        proc = read_url(item["url"], final)
        ok = final.exists() and final.stat().st_size > 300
        if ok:
            text = final.read_text(encoding="utf-8", errors="ignore")
            if "Access Denied" in text and len(text) < 1200:
                ok = False
        if ok:
            item["status"] = "snapshot_saved"
            item["saved_path"] = str(final)
            item["snapshot_note"] = "原站下载受限，已保存 r.jina.ai 公开网页 Markdown 快照。"
            item["error"] = ""
            sidecar = final.with_suffix(".source.txt")
            sidecar.write_text(
                f"title: {title}\noriginal_url: {item.get('url')}\nsnapshot_method: r.jina.ai Markdown reader\n",
                encoding="utf-8",
            )
            print(f"snapshot_saved {title[:80]}")
        else:
            if final.exists():
                final.unlink()
            item["snapshot_note"] = "原站与网页快照均受限或无正文。"
            print(f"still_failed {title[:80]} :: {(proc.stderr or '')[-160:]}")
        changed.append(item)

    results_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    with (meta / "download_results.csv").open("w", encoding="utf-8") as f:
        headers = ["status", "source_type", "category", "title", "url", "saved_path", "error", "snapshot_note"]
        f.write(",".join(headers) + "\n")
        for row in results:
            f.write(",".join('"' + str(row.get(h, "")).replace('"', '""') + '"' for h in headers) + "\n")
    summary = {
        "snapshot_saved": sum(1 for r in results if r.get("status") == "snapshot_saved"),
        "downloaded": sum(1 for r in results if r.get("status") == "downloaded"),
        "failed": sum(1 for r in results if r.get("status") == "failed"),
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
