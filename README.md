[README.md](https://github.com/user-attachments/files/29142314/README.md)
# HRI Robotics Research Output / 智能交互设计 × 机器人研究输出文档包

## 项目定位

这是一个面向“智能交互设计 × 机器人”的中文研究资料包和机器可读知识库。它支持：

- Word/Markdown 研究报告整理；
- HRI 知识图谱构建；
- LLM / RAG / GraphRAG 复用；
- 作品集项目、conference poster 和论文选题生成；
- 长期学习与文献扩展。

## 重要假设

- 本次不创建网站，也不生成前端代码。
- 本包是 seed repository，不是最终系统综述；引用和 DOI 已尽量使用权威来源，但投稿前仍建议二次核验。
- LLM robotics 相关资料发展很快，其中 preprint 已在来源记录中标注。
- 机器人标准主要用于工业/协作机器人场景，不能直接替代医疗、家庭、公共空间的伦理审查。

## 目录

- `01_主研究报告.md`：可直接整理成 Word 的主报告草稿。
- `02_知识图谱框架说明.md`：ontology、节点、关系、应用场景。
- `03_顶层本体与领域边界.md`：Scope、纳入/排除标准和 10 个本体。
- `04_节点类型与关系类型.md`：节点类型、关系类型和示例三元组。
- `05_核心主题模块.md`：24 个 HRI/机器人交互主题模块。
- `06_机器人系统视角.md`：感知、导航、规划、安全、失败恢复等系统模块如何转化为设计问题。
- `07_交互设计视角.md`：用户研究、任务流、状态可见性、RtD 等设计模块。
- `08_研究方法与评估指标.md`：20 个方法和 20 个指标。
- `09_设计机会与作品集方向.md`：20 个作品集方向。
- `10_论文与Poster选题.md`：poster、论文雏形和 RtD 方向。
- `11_大模型复用与知识库结构.md`：RAG / GraphRAG 使用方式。
- `12_结论与未来工作.md`：贡献和扩展路线。
- `13_研究路径思路结果与时间线.md`：基于主研究报告的后续研究路径、阶段结果、时间线和知识内容。
- `tables/`：适合 Excel 的 CSV 表格。
- `appendix/`：三元组、JSON 示例、来源记录和模板。
- `data/`：schema、nodes、relations 和 graph sample。
- `scripts/`：验证和转换脚本。

## 来源策略

文档引用使用 `Sxx` 编号，并在 `appendix/来源与检索记录.md` 中保留作者、年份、出处、链接和用途。核心来源包括 Goodrich & Schultz 的 HRI survey [S01](https://doi.org/10.1561/1100000005)、Fong 等社会机器人综述 [S02](https://doi.org/10.1016/S0921-8890(02)00372-X)、HRI trust 元分析 [S05](https://doi.org/10.1177/0018720811417254)、VAM-HRI survey [S12](https://doi.org/10.1145/3597623)、RtD 经典文献 [S14](https://doi.org/10.1145/1240624.1240704) [S15](https://doi.org/10.1145/2207676.2208538)、ISO 机器人安全标准 [S21](https://www.iso.org/standard/73933.html) [S22](https://www.iso.org/standard/62996.html)。

## 如何验证图谱

```bash
cd hri-robotics-research-output
python3 scripts/validate_graph.py
```

## 如何扩展

1. 新文献先填入 `appendix/参考文献整理模板.md`。
2. 提炼概念，加入 `data/graph/nodes.json`。
3. 提炼关系，加入 `data/graph/relations.json`。
4. 如果是术语，加入 `tables/术语表.csv`。
5. 运行验证脚本。
6. 把新的设计机会写入 `tables/设计机会表.csv`，运行 `python3 scripts/generate_opportunity_cards.py`。
