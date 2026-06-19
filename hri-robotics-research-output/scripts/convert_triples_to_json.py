from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
nodes = json.loads((ROOT / "data/graph/nodes.json").read_text(encoding="utf-8"))
label_to_id = {n["label"]: n["id"] for n in nodes}
label_to_id.update({n["zh_label"]: n["id"] for n in nodes})

pattern = re.compile(r"^\s*(.*?)\s+--\s+([a-zA-Z_]+)\s+-->\s+(.*?)\s*$")

def convert_line(line: str) -> dict | None:
    match = pattern.match(line)
    if not match:
        return None
    subject, predicate, obj = match.groups()
    return {
        "source": label_to_id.get(subject, subject),
        "target": label_to_id.get(obj, obj),
        "relation_type": predicate,
        "description": f"Converted from triple: {line.strip()}",
        "evidence": [],
        "directionality": "directed",
        "confidence_level": "medium",
        "design_implication": "",
    }

input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "appendix/知识图谱三元组.md"
items = []
for line in input_path.read_text(encoding="utf-8").splitlines():
    item = convert_line(line)
    if item:
        items.append(item)
print(json.dumps(items, ensure_ascii=False, indent=2))
