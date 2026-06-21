# 机器人产品资料库项目说明

生成时间：2026-06-21  
项目目录：`/Users/sampuichan/Documents/New project/机器人产品资料库_2026-06-21`

## 一、当前完成情况

本次整理基于两个源文件：

- Excel：`/Users/sampuichan/Desktop/机器人产品调研简报索引表.xlsx`
- Word：`/Users/sampuichan/Desktop/个人PRD_人形机器人产品实习能力建设系统.docx`

处理结果：

- Excel 原表共抽取到 48 条 URL，已全部处理：43 条直接下载成功，5 条原站下载受限但已保存公开网页 Markdown 快照。
- Word 文档没有直接链接，但抽取出“竞品调研、岗位解析、用户手册、场景验证、政策背景”等补充资料需求；据此补充 22 条资料源，19 条直接下载成功，1 条保存快照，2 条 Tesla 链接受限未能下载。
- 当前资料库可用文件/快照共 68 个，约 104MB。
- 文件类型：PDF 36 个，HTML 网页快照 26 个，Markdown 受限页快照 6 个。
- 2026-06-21 追加：已将 26 个 HTML 网页快照全部转换为同目录 PDF，原 HTML 文件保留不变；转换结果记录在 `_metadata/html_to_pdf_results.csv` 和 `_metadata/html_to_pdf_results.json`。

## 二、目录结构

```text
机器人产品资料库_2026-06-21/
├── 01_Excel链接资料/
│   ├── 企业与产品资料/
│   ├── 市场与行业报告/
│   ├── 论文与技术资料/
│   ├── 竞品与岗位能力/
│   ├── 新闻与媒体/
│   └── 其他资料/
├── 02_Word补充资料/
│   ├── 企业与产品资料/
│   ├── 竞品与岗位能力/
│   ├── 政策与标准/
│   └── 新闻与媒体/
├── 03_下载受限网页快照/
└── _metadata/
```

每个下载文件旁边都有一个 `.source.txt`，记录原始 URL、下载 URL、内容类型、来源位置和上下文，便于回溯。

## 三、分类说明

`01_Excel链接资料` 是严格按 Excel 表中的链接下载或保存快照，包括 IFR、Stanford AI Index、券商/行业 PDF、HRI 论文、酒店/养老/清洁/协作机器人资料等。

`02_Word补充资料` 是根据 Word 里的能力建设需求补充的资料，重点覆盖：

- 竞品资料：Unitree G1、UBTECH Walker S2、Agility Digit、Tesla Optimus 相关公开资料。
- 产品文档样例：Unitree G1 用户手册、Unitree G1 数据表、Walker S2 产品手册。
- 岗位能力样本：机器人产品经理/产品实习/JD 页面，支持简历关键词、岗位匹配矩阵和能力证据拆解。
- 场景与政策背景：2026 年人形机器人与具身智能实景实训行动相关公开报道。

`03_下载受限网页快照` 存放原站 403 或限制下载时，用公开网页读取器保存下来的 Markdown 正文快照。它不是原站原始 PDF，但保留了可读正文和原始 URL。

## 四、未能下载的资料

以下 2 条经过 curl、地区入口和网页快照方式尝试后仍被 Tesla/Akamai 拒绝访问：

- Tesla AI & Robotics - Optimus official page：`https://www.tesla.com/AI`
- Tesla product manager factory design robotics JD：`https://www.tesla.com/careers/search/job/product-manager-factory-design-robotics-248693`

已保留在 `_metadata/download_results.csv` 和 `_metadata/download_results.json` 中，状态为 `failed`，方便以后用浏览器登录或更换网络环境手动获取。

## 五、元数据文件

- `_metadata/sources_manifest.csv`：从 Excel 和 Word 初步抽取出的来源/需求清单。
- `_metadata/combined_download_manifest.json`：Excel 链接 + Word 补充资料源合并清单。
- `_metadata/download_results.csv`：最适合人工查看的下载结果表。
- `_metadata/download_results.json`：完整机器可读结果，包含保存路径、失败原因、快照说明。
- `_metadata/html_to_pdf_results.csv`：HTML 转 PDF 的结果表，包含页数、大小、源 HTML 和生成 PDF 路径。
- `_metadata/html_to_pdf_results.json`：HTML 转 PDF 的完整机器可读结果。

## 六、建议使用方式

如果要快速写 5-8 页机器人竞品调研简报，建议先看：

1. `01_Excel链接资料/市场与行业报告`
2. `01_Excel链接资料/企业与产品资料`
3. `02_Word补充资料/企业与产品资料`
4. `02_Word补充资料/竞品与岗位能力`

如果要做作品集/面试材料，建议优先从 `02_Word补充资料` 中提炼：

- 竞品对比维度：产品定位、目标场景、硬件规格、交互入口、安全/异常处理、商业化阶段。
- 岗位关键词：需求调研、竞品分析、PRD、用户手册、测试验证、跨部门协同、硬件/软件/算法接口理解。
- 输出物模板：岗位匹配矩阵、竞品分析表、机器人场景产品案例、PRD 样例、用户操作说明。

## 七、当前状态一句话

资料库已经完成第一版可用整理：Excel 链接基本全覆盖，Word 补充资料已按竞品、岗位、产品文档和政策场景补齐，只有 2 条 Tesla 官方链接因访问限制暂未下载。
