from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "tables/设计机会表.csv"
out_dir = ROOT / "outputs/portfolio/opportunity_cards"
out_dir.mkdir(parents=True, exist_ok=True)

with source.open(encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

for i, row in enumerate(rows, start=1):
    slug = f"{i:02d}_" + "".join(ch if ch.isalnum() else "_" for ch in row["方向标题"])[:40]
    content = f"""# {row['方向标题']}

- 目标用户：{row['目标用户']}
- 场景：{row['场景']}
- 核心问题：{row['核心问题']}
- 相关知识节点：{row['相关知识节点']}
- 原型形式：{row['原型形式']}
- 评估方法：{row['评估方法']}
- 作品集价值：{row['作品集价值']}
"""
    (out_dir / f"{slug}.md").write_text(content, encoding="utf-8")

print(f"Generated {len(rows)} opportunity cards in {out_dir}")
