from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tables/术语表.csv"
target = ROOT / "appendix/术语表.md"

with source.open(encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

lines = ["# 术语表", ""]
for row in rows:
    lines.append(f"## {row['英文术语']} / {row['中文术语']}")
    lines.append(f"- 定义：{row['定义']}")
    lines.append(f"- 相关概念：{row['相关概念']}")
    lines.append(f"- 设计意义：{row['设计意义']}")
    lines.append(f"- 示例场景：{row['示例场景']}")
    lines.append("")

target.write_text("\n".join(lines), encoding="utf-8")
print(f"Exported {target}")
