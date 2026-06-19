#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from docx import Document
from docx.document import Document as DocumentType
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


GLOSSARY = [
    ("HCI", "人机交互"),
    ("Human-Computer Interaction", "人机交互"),
    ("UI/UX Design", "UI/UX 设计"),
    ("User Interface", "用户界面"),
    ("User Experience", "用户体验"),
    ("interaction design", "交互设计"),
    ("interactive systems", "交互系统"),
    ("interactive toolkit", "交互工具包"),
    ("toolkit", "工具包"),
    ("constructive research", "构建性研究"),
    ("empirical research", "实证研究"),
    ("empirical study", "实证研究"),
    ("experiment design", "实验设计"),
    ("research question", "研究问题"),
    ("research contribution", "研究贡献"),
    ("literature review", "文献综述"),
    ("systematic literature review", "系统性文献综述"),
    ("scoping review", "范围综述"),
    ("formal literature review", "正式文献综述"),
    ("related work", "相关工作"),
    ("paper reading", "论文阅读"),
    ("reviewer", "审稿人"),
    ("rebuttal", "回应信"),
    ("response to reviewers", "审稿意见回复"),
    ("research prototype", "研究原型"),
    ("prototype", "原型"),
    ("prototyping", "原型制作"),
    ("design space", "设计空间"),
    ("design space exploration", "设计空间探索"),
    ("interaction technique", "交互技术"),
    ("input technique", "输入技术"),
    ("user study", "用户研究"),
    ("usability study", "可用性研究"),
    ("controlled experiment", "受控实验"),
    ("within-subjects design", "被试内设计"),
    ("between-subjects design", "被试间设计"),
    ("mixed design", "混合设计"),
    ("independent variable", "自变量"),
    ("dependent variable", "因变量"),
    ("control variable", "控制变量"),
    ("confounding variable", "混淆变量"),
    ("condition", "条件"),
    ("block", "区组"),
    ("trial", "试次"),
    ("repetition", "重复"),
    ("counterbalancing", "平衡顺序"),
    ("Latin square", "拉丁方"),
    ("randomization", "随机化"),
    ("hypothesis", "假设"),
    ("null hypothesis", "零假设"),
    ("statistical power", "统计功效"),
    ("effect size", "效应量"),
    ("p-value", "p 值"),
    ("ANOVA", "方差分析"),
    ("qualitative research", "质性研究"),
    ("quantitative research", "量化研究"),
    ("mixed methods", "混合方法"),
    ("interview", "访谈"),
    ("survey", "问卷调查"),
    ("questionnaire", "问卷"),
    ("participant", "参与者"),
    ("recruitment", "招募"),
    ("pilot study", "预实验"),
    ("formative study", "形成性研究"),
    ("summative evaluation", "总结性评估"),
    ("evaluation method", "评估方法"),
    ("benchmark", "基准"),
    ("baseline", "基线"),
    ("workflow", "工作流程"),
    ("taxonomy", "分类体系"),
    ("framework", "框架"),
    ("methodology", "方法论"),
    ("validity", "效度"),
    ("reliability", "信度"),
    ("ecological validity", "生态效度"),
    ("internal validity", "内部效度"),
    ("external validity", "外部效度"),
    ("construct validity", "构念效度"),
    ("generalizability", "可推广性"),
    ("replicability", "可复现性"),
    ("novelty", "新颖性"),
    ("technical contribution", "技术贡献"),
    ("system paper", "系统论文"),
    ("toolkit paper", "工具包论文"),
    ("method paper", "方法论文"),
    ("CHI", "CHI 会议"),
    ("ACM CHI", "ACM CHI 会议"),
]

ZH_FIXES = [
    ("人机互动", "人机交互"),
    ("人机相互作用", "人机交互"),
    ("用户介面", "用户界面"),
    ("交互式系统", "交互系统"),
    ("互动系统", "交互系统"),
    ("交互式工具包", "交互工具包"),
    ("建设性研究", "构建性研究"),
    ("建构性研究", "构建性研究"),
    ("实证式研究", "实证研究"),
    ("研究问题 ", "研究问题"),
    ("p值", "p 值"),
    ("P值", "p 值"),
]

REFERENCE_HEADING_RE = re.compile(r"^(references|参考文献)$", re.I)
ACK_HEADING_RE = re.compile(r"^acknowledg(e)?ment$", re.I)
URL_RE = re.compile(r"https?://|doi\.org|^\s*doi\s*:", re.I)
CITATION_RE = re.compile(r"\(\d{4}\)|\b\d{4}\.\s")


@dataclass
class Block:
    kind: str
    style: str
    text: str
    data: object | None = None


def iter_block_items(parent: DocumentType) -> Iterable[Paragraph | Table]:
    for child in parent.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def has_cjk(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)


def has_latin_words(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]{3,}", text))


def should_translate(text: str, in_references: bool) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if in_references:
        return False
    if has_cjk(stripped) and len(re.findall(r"[A-Za-z]{3,}", stripped)) < 8:
        return False
    if URL_RE.search(stripped):
        return False
    return has_latin_words(stripped)


def normalize_ws(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def markdown_escape_cell(text: str) -> str:
    return normalize_ws(text).replace("|", "\\|").replace("\n", "<br>")


def image_refs(paragraph: Paragraph) -> list[str]:
    refs = []
    for blip in paragraph._element.xpath(".//a:blip"):
        rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
        if rid:
            refs.append(rid)
    return refs


def paragraph_text(paragraph: Paragraph) -> str:
    return normalize_ws(paragraph.text)


def collect_blocks(doc: Document, asset_dir: Path) -> list[Block]:
    blocks: list[Block] = []
    asset_dir.mkdir(parents=True, exist_ok=True)
    image_counter = 1

    for item in iter_block_items(doc):
        if isinstance(item, Paragraph):
            text = paragraph_text(item)
            refs = image_refs(item)
            image_paths = []
            for rid in refs:
                part = item.part.related_parts.get(rid)
                if not part:
                    continue
                ext = Path(part.partname).suffix or ".png"
                filename = f"image-{image_counter:03d}{ext}"
                target = asset_dir / filename
                target.write_bytes(part.blob)
                image_paths.append(target.name)
                image_counter += 1
            if text or image_paths:
                blocks.append(Block("paragraph", item.style.name, text, image_paths))
        elif isinstance(item, Table):
            rows = []
            for row in item.rows:
                rows.append([normalize_ws(cell.text) for cell in row.cells])
            blocks.append(Block("table", "Table", "", rows))

    return blocks


def load_cache(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_cache(path: Path, cache: dict[str, str]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def cache_key(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def google_translate(text: str, retries: int = 8) -> str:
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "zh-CN",
        "dt": "t",
        "q": text,
    }
    data = urllib.parse.urlencode(params).encode("utf-8")
    url = "https://translate.googleapis.com/translate_a/single"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(
                url,
                data=data,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                    "User-Agent": "Mozilla/5.0",
                },
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            translated = "".join(part[0] for part in payload[0] if part and part[0])
            return translated.strip()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429:
                time.sleep(min(90, 15 * (attempt + 1)))
            else:
                time.sleep(2 * (attempt + 1))
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"translation failed after retries: {last_error}")


def translate_batch(texts: list[str], cache: dict[str, str], cache_path: Path) -> list[str]:
    results: list[str] = []
    missing = []
    missing_indexes = []
    for idx, text in enumerate(texts):
        key = cache_key(text)
        if key in cache:
            results.append(cache[key])
        else:
            results.append("")
            missing.append(text)
            missing_indexes.append(idx)

    if not missing:
        return results

    batch: list[tuple[int, str]] = []
    batch_chars = 0

    def flush() -> None:
        nonlocal batch, batch_chars
        if not batch:
            return
        joined_parts = []
        for seq, original in batch:
            joined_parts.append(f"<<<SEG_{seq:05d}>>>")
            joined_parts.append(original)
        joined = "\n".join(joined_parts)
        translated_joined = google_translate(joined)
        matches = list(re.finditer(r"<<<SEG_(\d{5})>>>", translated_joined))
        if len(matches) != len(batch):
            # Fall back to single-item calls if the delimiter parser is confused.
            for seq, original in batch:
                translated = google_translate(original)
                translated = apply_zh_fixes(translated)
                cache[cache_key(original)] = translated
                results[missing_indexes[seq]] = translated
            save_cache(cache_path, cache)
            batch = []
            batch_chars = 0
            return
        seq_to_text: dict[int, str] = {}
        for pos, match in enumerate(matches):
            start = match.end()
            end = matches[pos + 1].start() if pos + 1 < len(matches) else len(translated_joined)
            seq = int(match.group(1))
            seq_to_text[seq] = translated_joined[start:end].strip()
        for seq, original in batch:
            translated = apply_zh_fixes(seq_to_text.get(seq, ""))
            cache[cache_key(original)] = translated
            results[missing_indexes[seq]] = translated
        save_cache(cache_path, cache)
        print(f"translated {len([r for r in results if r])}/{len(texts)} segments", file=sys.stderr, flush=True)
        time.sleep(1.25)
        batch = []
        batch_chars = 0

    for local_seq, text in enumerate(missing):
        projected = batch_chars + len(text) + 20
        if projected > 4200:
            flush()
        batch.append((local_seq, text))
        batch_chars += len(text) + 20
    flush()
    return results


def apply_zh_fixes(text: str) -> str:
    for old, new in ZH_FIXES:
        text = text.replace(old, new)
    text = re.sub(r"\s+([，。；：？！、）】》])", r"\1", text)
    text = re.sub(r"([（【《])\s+", r"\1", text)
    return text.strip()


def heading_level(style: str) -> int | None:
    match = re.match(r"Heading\s+(\d+)", style)
    if not match:
        return None
    return max(1, min(6, int(match.group(1))))


def glossary_markdown() -> str:
    lines = [
        "",
        "# 专有名词和关键名词中英文对照表",
        "",
        "| 英文 | 中文 |",
        "| --- | --- |",
    ]
    seen = set()
    for en, zh in GLOSSARY:
        key = en.lower()
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"| {en} | {zh} |")
    return "\n".join(lines)


def preprocess_translation_units(blocks: list[Block]) -> tuple[list[str], dict[tuple[int, str], int]]:
    units: list[str] = []
    mapping: dict[tuple[int, str], int] = {}
    in_references = False
    for block_index, block in enumerate(blocks):
        if block.kind == "paragraph":
            raw = block.text
            if heading_level(block.style):
                if REFERENCE_HEADING_RE.match(raw.strip()):
                    in_references = True
                elif raw.strip() and not ACK_HEADING_RE.match(raw.strip()):
                    in_references = False
            if should_translate(raw, in_references):
                mapping[(block_index, "text")] = len(units)
                units.append(raw)
        elif block.kind == "table":
            rows = block.data or []
            assert isinstance(rows, list)
            for r_idx, row in enumerate(rows):
                for c_idx, cell in enumerate(row):
                    if should_translate(cell, in_references):
                        mapping[(block_index, f"{r_idx}:{c_idx}")] = len(units)
                        units.append(cell)
    return units, mapping


def render_blocks(
    blocks: list[Block],
    translations: list[str],
    mapping: dict[tuple[int, str], int],
    asset_dir_name: str,
) -> str:
    lines: list[str] = []
    for block_index, block in enumerate(blocks):
        if block.kind == "paragraph":
            text = block.text
            translated_index = mapping.get((block_index, "text"))
            if translated_index is not None:
                text = translations[translated_index]
            level = heading_level(block.style)
            if level:
                prefix = "#" * level
                lines.append(f"{prefix} {text}".rstrip())
                lines.append("")
            elif text:
                lines.append(text)
                lines.append("")
            for image_name in block.data or []:
                lines.append(f"![图]({asset_dir_name}/{image_name})")
                lines.append("")
        elif block.kind == "table":
            rows = block.data or []
            assert isinstance(rows, list)
            translated_rows = []
            for r_idx, row in enumerate(rows):
                translated_row = []
                for c_idx, cell in enumerate(row):
                    translated_index = mapping.get((block_index, f"{r_idx}:{c_idx}"))
                    translated_row.append(translations[translated_index] if translated_index is not None else cell)
                translated_rows.append(translated_row)

            max_cols = max((len(row) for row in translated_rows), default=0)
            if max_cols <= 1:
                for row in translated_rows:
                    cell = markdown_escape_cell(row[0] if row else "")
                    if cell:
                        lines.append(f"> {cell}")
                lines.append("")
            else:
                header = translated_rows[0] if translated_rows else []
                header = header + [""] * (max_cols - len(header))
                lines.append("| " + " | ".join(markdown_escape_cell(cell) for cell in header) + " |")
                lines.append("| " + " | ".join("---" for _ in range(max_cols)) + " |")
                for row in translated_rows[1:]:
                    row = row + [""] * (max_cols - len(row))
                    lines.append("| " + " | ".join(markdown_escape_cell(cell) for cell in row) + " |")
                lines.append("")
    lines.append(glossary_markdown())
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--asset-dir", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    args = parser.parse_args()

    if args.asset_dir.exists():
        shutil.rmtree(args.asset_dir)
    doc = Document(args.docx)
    blocks = collect_blocks(doc, args.asset_dir)
    units, mapping = preprocess_translation_units(blocks)
    cache = load_cache(args.cache)
    print(f"blocks={len(blocks)} translation_units={len(units)} cache_entries={len(cache)}", file=sys.stderr)
    translations = translate_batch(units, cache, args.cache)
    rendered = render_blocks(blocks, translations, mapping, args.asset_dir.name)
    args.out.write_text(rendered, encoding="utf-8")
    print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
