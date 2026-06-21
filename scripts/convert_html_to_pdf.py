#!/usr/bin/env python3
import csv
import html as html_std
import json
import re
from pathlib import Path

from lxml import html as lxml_html
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def pdf_page_count(path: Path) -> int:
    with path.open("rb") as fh:
        return len(PdfReader(fh).pages)


def clean_text(value: str) -> str:
    value = html_std.unescape(value or "")
    value = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def extract_html_blocks(path: Path) -> tuple[str, list[tuple[str, str]]]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    doc = lxml_html.fromstring(raw)
    for bad in doc.xpath("//script|//style|//noscript|//svg|//canvas|//iframe"):
        parent = bad.getparent()
        if parent is not None:
            parent.remove(bad)
    title = clean_text(" ".join(doc.xpath("//title/text()"))) or path.stem
    blocks: list[tuple[str, str]] = []
    seen = set()
    tags = "h1|h2|h3|h4|h5|h6|p|li|blockquote|pre|th|td"
    xpath = "//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::p or self::li or self::blockquote or self::pre or self::th or self::td]"
    for node in doc.xpath(xpath):
        text = clean_text(node.text_content())
        if not text or len(text) < 2:
            continue
        if len(text) > 5000:
            text = text[:5000] + " ..."
        key = (node.tag, text)
        if key in seen:
            continue
        seen.add(key)
        if node.tag in {"h1", "h2", "h3"}:
            kind = "heading"
        elif node.tag == "li":
            kind = "list"
        elif node.tag in {"th", "td"}:
            kind = "table"
        elif node.tag == "pre":
            kind = "pre"
        else:
            kind = "body"
        blocks.append((kind, text))
    if not blocks:
        text = clean_text(doc.text_content())
        chunks = [text[i : i + 1500] for i in range(0, len(text), 1500)]
        blocks = [("body", chunk) for chunk in chunks if chunk]
    return title, blocks


def register_fonts() -> tuple[str, str]:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light", "STSong-Light"
    except Exception:
        return "Helvetica", "Helvetica-Bold"


def build_reading_pdf(html_path: Path, pdf_path: Path) -> dict:
    title, blocks = extract_html_blocks(html_path)
    body_font, heading_font = register_fonts()
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocTitle",
            fontName=heading_font,
            fontSize=16,
            leading=22,
            textColor=colors.HexColor("#111827"),
            spaceAfter=12,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            fontName=body_font,
            fontSize=8,
            leading=11,
            textColor=colors.HexColor("#6B7280"),
            spaceAfter=10,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading",
            fontName=heading_font,
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#1F2937"),
            spaceBefore=8,
            spaceAfter=5,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="ReadableBody",
            fontName=body_font,
            fontSize=9.5,
            leading=14,
            textColor=colors.HexColor("#111827"),
            spaceAfter=5,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="ListItem",
            parent=styles["ReadableBody"],
            leftIndent=12,
            firstLineIndent=-8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableText",
            parent=styles["ReadableBody"],
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#374151"),
        )
    )
    story = [
        Paragraph(html_std.escape(title), styles["DocTitle"]),
        Paragraph(f"Source HTML: {html_std.escape(str(html_path))}", styles["Meta"]),
    ]
    for kind, text in blocks:
        escaped = html_std.escape(text)
        if kind == "heading":
            story.append(Paragraph(escaped, styles["Heading"]))
        elif kind == "list":
            story.append(Paragraph(f"- {escaped}", styles["ListItem"]))
        elif kind == "table":
            story.append(Paragraph(escaped, styles["TableText"]))
        else:
            story.append(Paragraph(escaped, styles["ReadableBody"]))
        if len(story) % 90 == 0:
            story.append(Spacer(1, 0.08 * cm))
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=title,
        author="Codex",
    )
    doc.build(story)
    pages = pdf_page_count(pdf_path)
    return {
        "html_path": str(html_path),
        "pdf_path": str(pdf_path),
        "status": "converted" if pages > 0 else "failed",
        "pages": pages,
        "bytes": pdf_path.stat().st_size if pdf_path.exists() else 0,
        "error": "" if pages > 0 else "PDF has zero pages",
    }


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="Directory containing HTML files")
    parser.add_argument("--metadata-dir", default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    meta = Path(args.metadata_dir) if args.metadata_dir else root / "_metadata"
    meta.mkdir(parents=True, exist_ok=True)
    html_files = sorted(root.rglob("*.html"))
    results = []

    for index, html_path in enumerate(html_files, 1):
        pdf_path = html_path.with_suffix(".pdf")
        if pdf_path.exists() and not args.overwrite:
            result = {
                "html_path": str(html_path),
                "pdf_path": str(pdf_path),
                "status": "skipped_exists",
                "pages": pdf_page_count(pdf_path),
                "bytes": pdf_path.stat().st_size,
                "error": "",
            }
        else:
            result = build_reading_pdf(html_path, pdf_path)
        results.append(result)
        print(f"{index}/{len(html_files)} {result['status']} pages={result['pages']} {html_path}")

    json_path = meta / "html_to_pdf_results.json"
    csv_path = meta / "html_to_pdf_results.csv"
    json_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["status", "pages", "bytes", "html_path", "pdf_path", "error"])
        writer.writeheader()
        writer.writerows(results)

    summary = {
        "total": len(results),
        "converted": sum(1 for r in results if r["status"] == "converted"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "skipped_exists": sum(1 for r in results if r["status"] == "skipped_exists"),
        "metadata": str(meta),
    }
    print(json.dumps(summary, ensure_ascii=False))
    raise SystemExit(1 if summary["failed"] else 0)


if __name__ == "__main__":
    main()
