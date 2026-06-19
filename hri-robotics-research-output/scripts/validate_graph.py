from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
nodes = json.loads((ROOT / "data/graph/nodes.json").read_text(encoding="utf-8"))
relations = json.loads((ROOT / "data/graph/relations.json").read_text(encoding="utf-8"))
node_schema = json.loads((ROOT / "data/schemas/node.schema.json").read_text(encoding="utf-8"))
relation_schema = json.loads((ROOT / "data/schemas/relation.schema.json").read_text(encoding="utf-8"))

node_types = set(node_schema["properties"]["type"]["enum"])
relation_types = set(relation_schema["properties"]["relation_type"]["enum"])
node_required = set(node_schema["required"])
relation_required = set(relation_schema["required"])
node_ids = {n.get("id") for n in nodes}

errors = []

for i, node in enumerate(nodes):
    missing = node_required - node.keys()
    if missing:
        errors.append(f"node[{i}] missing fields: {sorted(missing)}")
    if node.get("type") not in node_types:
        errors.append(f"node[{i}] invalid type: {node.get('type')}")

for i, relation in enumerate(relations):
    missing = relation_required - relation.keys()
    if missing:
        errors.append(f"relation[{i}] missing fields: {sorted(missing)}")
    if relation.get("source") not in node_ids:
        errors.append(f"relation[{i}] unknown source: {relation.get('source')}")
    if relation.get("target") not in node_ids:
        errors.append(f"relation[{i}] unknown target: {relation.get('target')}")
    if relation.get("relation_type") not in relation_types:
        errors.append(f"relation[{i}] invalid relation_type: {relation.get('relation_type')}")

if errors:
    print("Graph validation failed:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print(f"Graph validation passed: {len(nodes)} nodes, {len(relations)} relations.")
