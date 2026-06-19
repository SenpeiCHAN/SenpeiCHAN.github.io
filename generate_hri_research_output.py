from __future__ import annotations

import csv
import json
from pathlib import Path
from textwrap import dedent


BASE = Path("hri-robotics-research-output")


def source_link(source_id: str) -> str:
    source = SOURCE_BY_ID[source_id]
    return f"[{source_id}]({source['url']})"


SOURCES = [
    {
        "id": "S01",
        "title": "Human-Robot Interaction: A Survey",
        "authors": "Goodrich, M. A.; Schultz, A. C.",
        "year": "2007",
        "venue": "Foundations and Trends in Human-Computer Interaction",
        "url": "https://doi.org/10.1561/1100000005",
        "type": "peer-reviewed survey",
        "note": "HRI 早期统一框架，适合定义领域边界、交互类型与挑战。",
    },
    {
        "id": "S02",
        "title": "A Survey of Socially Interactive Robots",
        "authors": "Fong, T.; Nourbakhsh, I.; Dautenhahn, K.",
        "year": "2003",
        "venue": "Robotics and Autonomous Systems",
        "url": "https://doi.org/10.1016/S0921-8890(02)00372-X",
        "type": "peer-reviewed survey",
        "note": "社交机器人分类与设计组件的经典综述。",
    },
    {
        "id": "S03",
        "title": "Socially Intelligent Robots: Dimensions of Human-Robot Interaction",
        "authors": "Dautenhahn, K.",
        "year": "2007",
        "venue": "Philosophical Transactions of the Royal Society B",
        "url": "https://doi.org/10.1098/rstb.2006.2004",
        "type": "peer-reviewed article",
        "note": "提出 HRI 的社会维度与 robotiquette 议题。",
    },
    {
        "id": "S04",
        "title": "Measurement Instruments for the Anthropomorphism, Animacy, Likeability, Perceived Intelligence, and Perceived Safety of Robots",
        "authors": "Bartneck, C.; Kulic, D.; Croft, E.; Zoghbi, S.",
        "year": "2009",
        "venue": "International Journal of Social Robotics",
        "url": "https://doi.org/10.1007/s12369-008-0001-3",
        "type": "peer-reviewed method paper",
        "note": "Godspeed 问卷来源，用于社交机器人感知维度测量。",
    },
    {
        "id": "S05",
        "title": "A Meta-Analysis of Factors Affecting Trust in Human-Robot Interaction",
        "authors": "Hancock, P. A.; Billings, D. R.; Schaefer, K. E.; Chen, J. Y. C.; de Visser, E. J.; Parasuraman, R.",
        "year": "2011",
        "venue": "Human Factors",
        "url": "https://doi.org/10.1177/0018720811417254",
        "type": "peer-reviewed meta-analysis",
        "note": "HRI 信任研究的关键元分析。",
    },
    {
        "id": "S06",
        "title": "Trust in Automation: Designing for Appropriate Reliance",
        "authors": "Lee, J. D.; See, K. A.",
        "year": "2004",
        "venue": "Human Factors",
        "url": "https://doi.org/10.1518/hfes.46.1.50_30392",
        "type": "peer-reviewed review",
        "note": "自动化信任与适当依赖的基础文献。",
    },
    {
        "id": "S07",
        "title": "A Model for Types and Levels of Human Interaction with Automation",
        "authors": "Parasuraman, R.; Sheridan, T. B.; Wickens, C. D.",
        "year": "2000",
        "venue": "IEEE Transactions on Systems, Man, and Cybernetics",
        "url": "https://doi.org/10.1109/3468.844354",
        "type": "peer-reviewed theory/model",
        "note": "信息获取、分析、决策、行动四类自动化与不同自动化等级。",
    },
    {
        "id": "S08",
        "title": "Common Metrics for Human-Robot Interaction",
        "authors": "Steinfeld, A. et al.",
        "year": "2006",
        "venue": "ACM/IEEE HRI",
        "url": "https://doi.org/10.1145/1121241.1121249",
        "type": "conference paper",
        "note": "面向任务型 HRI 的通用评价指标框架。",
    },
    {
        "id": "S09",
        "title": "Toward a Framework for Levels of Robot Autonomy in Human-Robot Interaction",
        "authors": "Beer, J. M.; Fisk, A. D.; Rogers, W. A.",
        "year": "2014",
        "venue": "Journal of Human-Robot Interaction",
        "url": "https://doi.org/10.5898/JHRI.3.2.Beer",
        "type": "peer-reviewed article",
        "note": "机器人自主性等级和 HRI 角色分配的重要参考。",
    },
    {
        "id": "S10",
        "title": "A Survey of Methods for Safe Human-Robot Interaction",
        "authors": "Lasota, P. A.; Fong, T.; Shah, J. A.",
        "year": "2017",
        "venue": "Foundations and Trends in Robotics",
        "url": "https://doi.org/10.1561/2300000052",
        "type": "peer-reviewed survey",
        "note": "把安全 HRI 方法归纳为控制、运动规划、预测和心理因素等类别。",
    },
    {
        "id": "S11",
        "title": "Survey on Human-Robot Collaboration in Industrial Settings: Safety, Intuitive Interfaces and Applications",
        "authors": "Villani, V.; Pini, F.; Leali, F.; Secchi, C.",
        "year": "2018",
        "venue": "Mechatronics",
        "url": "https://doi.org/10.1016/j.mechatronics.2018.02.009",
        "type": "peer-reviewed survey",
        "note": "工业协作机器人中的安全、认知交互和直觉界面综述。",
    },
    {
        "id": "S12",
        "title": "Virtual, Augmented, and Mixed Reality for Human-Robot Interaction: A Survey and Virtual Design Element Taxonomy",
        "authors": "Walker, M.; Phung, T.; Chakraborti, T.; Williams, T.; Szafir, D.",
        "year": "2023",
        "venue": "ACM Transactions on Human-Robot Interaction",
        "url": "https://doi.org/10.1145/3597623",
        "type": "peer-reviewed survey",
        "note": "VAM-HRI 虚拟设计元素分类，是 AR/MR 机器人界面模块的核心来源。",
    },
    {
        "id": "S13",
        "title": "Legibility and Predictability of Robot Motion",
        "authors": "Dragan, A. D.; Lee, K. C. T.; Srinivasa, S. S.",
        "year": "2013",
        "venue": "ACM/IEEE HRI",
        "url": "https://doi.org/10.1109/HRI.2013.6483603",
        "type": "conference paper",
        "note": "区分可读性 motion legibility 与可预测性 predictability。",
    },
    {
        "id": "S14",
        "title": "Research Through Design as a Method for Interaction Design Research in HCI",
        "authors": "Zimmerman, J.; Forlizzi, J.; Evenson, S.",
        "year": "2007",
        "venue": "CHI",
        "url": "https://doi.org/10.1145/1240624.1240704",
        "type": "conference paper",
        "note": "RtD 作为 HCI 设计研究方法的经典论文。",
    },
    {
        "id": "S15",
        "title": "What Should We Expect from Research Through Design?",
        "authors": "Gaver, W.",
        "year": "2012",
        "venue": "CHI",
        "url": "https://doi.org/10.1145/2207676.2208538",
        "type": "conference paper",
        "note": "讨论 RtD 的知识形态、注释作品集与设计研究的非收敛性。",
    },
    {
        "id": "S16",
        "title": "Where the Action Is: The Foundations of Embodied Interaction",
        "authors": "Dourish, P.",
        "year": "2001",
        "venue": "MIT Press",
        "url": "https://mitpress.mit.edu/9780262541787/where-the-action-is/",
        "type": "book",
        "note": "具身交互理论基础，把行动、实践、情境作为交互理解中心。",
    },
    {
        "id": "S17",
        "title": "Plans and Situated Actions: The Problem of Human-Machine Communication",
        "authors": "Suchman, L. A.",
        "year": "1987",
        "venue": "Cambridge University Press",
        "url": "https://dl.acm.org/doi/abs/10.5555/38407",
        "type": "book",
        "note": "情境行动理论，为机器人任务流和人机协作中的计划-行动偏差提供理论依据。",
    },
    {
        "id": "S18",
        "title": "Assessing Acceptance of Assistive Social Agent Technology by Older Adults: The Almere Model",
        "authors": "Heerink, M.; Krose, B.; Evers, V.; Wielinga, B.",
        "year": "2010",
        "venue": "International Journal of Social Robotics",
        "url": "https://doi.org/10.1007/s12369-010-0068-5",
        "type": "peer-reviewed article",
        "note": "面向老年用户和 assistive social agent 的接受度模型。",
    },
    {
        "id": "S19",
        "title": "Development of NASA-TLX: Results of Empirical and Theoretical Research",
        "authors": "Hart, S. G.; Staveland, L. E.",
        "year": "1988",
        "venue": "Human Mental Workload",
        "url": "https://doi.org/10.1016/S0166-4115(08)62386-9",
        "type": "method chapter",
        "note": "NASA-TLX 工作负荷测量来源。",
    },
    {
        "id": "S20",
        "title": "Toward a Theory of Situation Awareness in Dynamic Systems",
        "authors": "Endsley, M. R.",
        "year": "1995",
        "venue": "Human Factors",
        "url": "https://doi.org/10.1518/001872095779049543",
        "type": "peer-reviewed theory",
        "note": "情境感知 SA 的基础理论，用于远程操作、监控和协作机器人。",
    },
    {
        "id": "S21",
        "title": "ISO 10218-1:2025 Robotics - Safety Requirements - Part 1: Industrial Robots",
        "authors": "International Organization for Standardization",
        "year": "2025",
        "venue": "ISO Standard",
        "url": "https://www.iso.org/standard/73933.html",
        "type": "standard",
        "note": "工业机器人安全要求。检索日期：2026-06-19。",
    },
    {
        "id": "S22",
        "title": "ISO/TS 15066:2016 Robots and Robotic Devices - Collaborative Robots",
        "authors": "International Organization for Standardization",
        "year": "2016",
        "venue": "ISO Technical Specification",
        "url": "https://www.iso.org/standard/62996.html",
        "type": "standard",
        "note": "协作机器人系统与共享工作空间安全要求。检索日期：2026-06-19。",
    },
    {
        "id": "S23",
        "title": "ACM/IEEE International Conference on Human-Robot Interaction 2026",
        "authors": "ACM/IEEE HRI",
        "year": "2026",
        "venue": "Conference website",
        "url": "https://humanrobotinteraction.org/2026/",
        "type": "official website",
        "note": "HRI 官方会议网页称其为 HRI 创新的主要 venue，并列出跨学科范围。检索日期：2026-06-19。",
    },
    {
        "id": "S24",
        "title": "ACM CHI 2026",
        "authors": "ACM SIGCHI",
        "year": "2026",
        "venue": "Conference website",
        "url": "https://chi2026.acm.org/",
        "type": "official website",
        "note": "CHI 官方网页称其为 HCI 领先国际会议。检索日期：2026-06-19。",
    },
    {
        "id": "S25",
        "title": "IEEE Robotics and Automation Society Technical Committees",
        "authors": "IEEE RAS",
        "year": "2026",
        "venue": "Official website",
        "url": "https://www.ieee-ras.org/technical-committees/",
        "type": "official website",
        "note": "IEEE RAS technical committees and human-centered robotics context. 检索日期：2026-06-19。",
    },
    {
        "id": "S26",
        "title": "World Robotics Reports",
        "authors": "International Federation of Robotics",
        "year": "2025",
        "venue": "IFR statistics portal",
        "url": "https://ifr.org/worldrobotics/",
        "type": "industry statistics",
        "note": "全球工业和服务机器人统计、趋势和预测来源。检索日期：2026-06-19。",
    },
    {
        "id": "S27",
        "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
        "authors": "Ahn, M. et al.",
        "year": "2022",
        "venue": "arXiv / SayCan project",
        "url": "https://arxiv.org/abs/2204.01691",
        "type": "preprint",
        "note": "LLM 与机器人可供性 grounding 的代表性工作；用于未来方向，需按 preprint 看待。",
    },
    {
        "id": "S28",
        "title": "PaLM-E: An Embodied Multimodal Language Model",
        "authors": "Driess, D. et al.",
        "year": "2023",
        "venue": "ICML / arXiv",
        "url": "https://arxiv.org/abs/2303.03378",
        "type": "conference/preprint",
        "note": "具身多模态语言模型，支持视觉、语言和机器人任务的共同 grounding。",
    },
    {
        "id": "S29",
        "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "authors": "Zitkovich, B. et al.",
        "year": "2023",
        "venue": "Conference on Robot Learning / PMLR",
        "url": "https://proceedings.mlr.press/v229/zitkovich23a.html",
        "type": "conference paper",
        "note": "VLA model 把视觉语言模型迁移到机器人控制。",
    },
    {
        "id": "S30",
        "title": "A Taxonomy of Mixed Reality Visual Displays",
        "authors": "Milgram, P.; Kishino, F.",
        "year": "1994",
        "venue": "IEICE Transactions on Information and Systems",
        "url": "https://globals.ieice.org/en_transactions/information/10.1587/e77-d_12_1321/_p",
        "type": "peer-reviewed article",
        "note": "Reality-virtuality continuum 与 mixed reality 概念基础。",
    },
    {
        "id": "S31",
        "title": "Progress and Prospects of the Human-Robot Collaboration",
        "authors": "Ajoudani, A. et al.",
        "year": "2018",
        "venue": "Autonomous Robots",
        "url": "https://doi.org/10.1007/s10514-017-9677-2",
        "type": "peer-reviewed survey",
        "note": "HRC 的技术、控制、安全和协作趋势综述。",
    },
    {
        "id": "S32",
        "title": "Toward Sociable Robots",
        "authors": "Breazeal, C.",
        "year": "2003",
        "venue": "Robotics and Autonomous Systems",
        "url": "https://doi.org/10.1016/S0921-8890(02)00373-1",
        "type": "peer-reviewed article",
        "note": "社交机器人、情感表达和 sociability 的基础文献。",
    },
    {
        "id": "S33",
        "title": "Human-Robot Interaction: Status and Challenges",
        "authors": "Sheridan, T. B.",
        "year": "2016",
        "venue": "Human Factors",
        "url": "https://doi.org/10.1177/0018720816644364",
        "type": "peer-reviewed review",
        "note": "从 human factors 视角总结 HRI 现状和挑战。",
    },
]

SOURCE_BY_ID = {s["id"]: s for s in SOURCES}


ONTOLOGY = [
    {
        "name": "Human / 人",
        "definition": "HRI 中的人不是抽象用户，而是有身体能力、认知负荷、情绪、经验、责任和社会角色的行动者。",
        "subclasses": "User Group, Ability, Mental Model, Trust, Emotion, Agency, Expertise",
        "relations": "Human 执行 Task、感知 Robot、通过 Interface 与 Robot 协作，并受 Context 与 Ethics 约束。",
        "design": "把用户研究从偏好收集推进到能力、风险、角色和长期关系的建模。",
        "questions": "人如何理解机器人意图？人何时希望接管？不同用户如何校准信任？",
        "scenarios": "医院导诊、老年陪护、工业协作、公共空间服务。",
        "portfolio": "以特定用户群体为中心的服务机器人体验系统。",
    },
    {
        "name": "Robot / 机器人",
        "definition": "机器人是能感知、决策并在物理世界行动的具身系统；其交互体验受硬件形态、传感器、控制和安全策略共同塑造。",
        "subclasses": "Service Robot, Social Robot, Cobot, Mobile Manipulator, Telepresence Robot, Medical Robot",
        "relations": "Robot 承载 Intelligence 与 Embodiment，通过 Interface 反馈状态，在 Context 中执行 Task。",
        "design": "把技术模块翻译成用户可理解、可预测、可协作的行为。",
        "questions": "机器人应显露哪些状态？何时表达不确定性？不同形态如何影响社会期待？",
        "scenarios": "酒店配送、病房物流、工位协作、家庭助理。",
        "portfolio": "机器人状态表达、失败恢复或意图可视化原型。",
    },
    {
        "name": "Interaction / 交互",
        "definition": "交互是人和机器人围绕任务、环境与社会意义进行的连续协调，不只是一条输入-输出通道。",
        "subclasses": "Command, Feedback, Turn-taking, Handover, Coordination, Repair, Negotiation",
        "relations": "Interaction 连接 Human 与 Robot，并由 Interface、Context、Task、Evaluation 共同定义。",
        "design": "重点从界面控件转向协作节奏、可见状态、互相适应和失败修复。",
        "questions": "机器人如何请求澄清？人如何知道机器人下一步？交互失败怎样不破坏信任？",
        "scenarios": "人机交接、协作装配、公共空间避让、远程操作。",
        "portfolio": "多模态交互流程与可测试原型。",
    },
    {
        "name": "Intelligence / 智能",
        "definition": "智能包括感知、识别、推理、规划、学习、解释和自主性；在 HRI 中必须被人理解和约束。",
        "subclasses": "Perception, Intention Recognition, Planning, Autonomy, LLM Agent, Explainability",
        "relations": "Intelligence enables Robot action, but constrains Human trust when opaque or unstable.",
        "design": "把算法能力转成可控、可解释、可协商的交互体验。",
        "questions": "LLM agent 如何作为机器人中间层？智能系统如何表达置信度和失败原因？",
        "scenarios": "自然语言任务规划、共享自主、开放场景服务。",
        "portfolio": "AI agent + robot 任务协商界面。",
    },
    {
        "name": "Embodiment / 具身",
        "definition": "具身强调身体、动作、空间和环境不是交互背景，而是认知与协作的组成部分。",
        "subclasses": "Body, Motion, Spatial Presence, Affordance, Materiality, Physical Feedback",
        "relations": "Embodiment mediates Interaction and shapes Human mental models.",
        "design": "关注路径、姿态、速度、距离、接触和物理可供性如何传达意义。",
        "questions": "机器人运动怎样表达意图？身体形态会引发哪些错误期待？",
        "scenarios": "移动导览、机械臂协作、康复训练、家庭空间移动。",
        "portfolio": "具身状态表达与空间交互研究。",
    },
    {
        "name": "Interface / 界面",
        "definition": "界面是人与机器人系统交换意图、状态、解释和控制权的媒介，可以是屏幕、语音、手势、AR/MR、触觉或物理形态本身。",
        "subclasses": "Voice UI, Gesture UI, Gaze UI, Haptic UI, Tangible UI, AR/MR UI, Status Display",
        "relations": "Interface enables Interaction and mediates Intelligence legibility.",
        "design": "界面要降低不确定性、展示状态边界，并支持不同用户的控制与恢复策略。",
        "questions": "哪种模态最适合低负荷场景？AR/MR 能否提升路径和意图理解？",
        "scenarios": "协作机器人路径提示、服务机器人状态显示、远程操作反馈。",
        "portfolio": "AR/MR 机器人路径与意图可视化界面。",
    },
    {
        "name": "Context / 场景",
        "definition": "场景包括物理空间、组织流程、社会规范、风险水平和时间节奏，是机器人交互成立的条件。",
        "subclasses": "Home, Hospital, Hotel, Factory, Public Space, Museum, School",
        "relations": "Context constrains Task, Interface, Safety, Ethics and Evaluation.",
        "design": "同一个机器人能力在不同场景中会变成不同交互问题。",
        "questions": "公共空间机器人如何遵守隐性社会规范？医院机器人如何与护理流程共存？",
        "scenarios": "医院、酒店、工厂、社区、博物馆、机场。",
        "portfolio": "基于服务蓝图的场景化机器人体验设计。",
    },
    {
        "name": "Task / 任务",
        "definition": "任务是人机协作的目标结构，包括目标、子任务、责任、风险、时序和交接点。",
        "subclasses": "Delivery, Guidance, Handover, Assembly, Monitoring, Rehabilitation, Cleaning",
        "relations": "Task requires Robot capability, Human role allocation, Interface support and Evaluation criteria.",
        "design": "任务建模把机器人能力转译为交互流程和原型范围。",
        "questions": "哪些步骤应自动化？哪些步骤必须保留人类决策？任务失败后怎样恢复？",
        "scenarios": "物品递送、协作装配、导览、远程巡检。",
        "portfolio": "任务流、控制权转移和失败恢复设计。",
    },
    {
        "name": "Evaluation / 评估",
        "definition": "评估用于判断机器人交互是否可用、可信、安全、可接受、低负荷且能长期融入场景。",
        "subclasses": "Usability, Trust, Workload, Acceptance, Safety, Situation Awareness, Social Presence",
        "relations": "Evaluation measures Interaction outcomes and informs design iteration.",
        "design": "把作品集从“做了一个原型”推进到“有研究问题、测量方案和证据”。",
        "questions": "用什么指标证明 AR 路径提示有效？如何测量信任校准而不是单纯信任高低？",
        "scenarios": "Wizard-of-Oz 实验、可用性测试、长期部署、控制实验。",
        "portfolio": "带有评估矩阵的 HRI 设计研究项目。",
    },
    {
        "name": "Ethics & Society / 伦理与社会",
        "definition": "伦理与社会层关注隐私、安全、责任归属、偏见、可访问性、劳动影响和社会规范。",
        "subclasses": "Privacy, Accountability, Bias, Accessibility, Labor, Consent, Norms",
        "relations": "Ethics constrains Intelligence, Data, Context and deployment decisions.",
        "design": "要求设计不仅提升效率，还要明确边界、告知、同意、责任与脆弱群体保护。",
        "questions": "服务机器人收集哪些数据？LLM 机器人误导用户时谁负责？机器人是否加剧不平等？",
        "scenarios": "养老、医疗、公共空间、教育、家庭。",
        "portfolio": "机器人伦理交互准则与设计审计工具。",
    },
]


NODE_TYPE_ROWS = [
    ["Discipline", "学科", "组织领域来源与研究传统。", "id,label,definition,evidence", "Human-Robot Interaction", "用于建立领域边界与检索入口。"],
    ["Concept", "概念", "可被定义、比较和连接的核心术语。", "definition,parent,related_nodes", "Trust Calibration", "适合 RAG 查询与主题索引。"],
    ["Theory", "理论", "解释交互现象的抽象模型。", "claim,scope,limitations,evidence", "Situated Action", "用于支撑设计推论。"],
    ["Method", "方法", "研究、设计或评估的方法。", "stage,procedure,pros,limits", "Wizard-of-Oz", "用于推荐研究方案。"],
    ["Technology", "技术", "机器人或界面系统模块。", "capability,constraints,design_risk", "AR Interface", "用于把工程能力转成交互问题。"],
    ["Interaction Modality", "交互模态", "输入输出通道与反馈形式。", "input,feedback,context", "Voice Interaction", "用于多模态组合。"],
    ["Robot Type", "机器人类型", "按形态、任务或场景划分的机器人。", "embodiment,tasks,risks", "Service Robot", "用于场景化设计。"],
    ["Scenario", "应用场景", "机器人运行的真实环境和服务情境。", "users,tasks,constraints", "Hospital Guidance", "用于作品集 brief。"],
    ["Task", "任务", "目标、步骤、责任与失败点。", "goal,subtasks,handoff", "Medication Delivery", "用于任务流和评估设计。"],
    ["User Group", "用户群体", "具有特定能力、需求和风险的使用者。", "needs,abilities,risks", "Older Adults", "用于用户研究。"],
    ["Design Issue", "设计问题", "可被设计介入的痛点或张力。", "problem,cause,impact", "Unclear Robot Intent", "用于机会生成。"],
    ["Evaluation Metric", "评估指标", "衡量交互结果的变量。", "measure,tool,scenario", "Trust", "用于实验和可用性研究。"],
    ["Paper / Source", "文献来源", "支持事实或理论的论文、标准或网页。", "authors,year,venue,url", "Goodrich & Schultz 2007", "用于证据追踪。"],
    ["Case / Product", "案例或产品", "真实或研究原型案例。", "context,features,lessons", "Hotel Delivery Robot", "用于案例研究。"],
    ["Design Opportunity", "设计机会", "可发展为项目或原型的方向。", "users,scenario,prototype,metrics", "AR Path Guidance", "用于作品集与 poster。"],
    ["Research Question", "研究问题", "可被方法和数据回答的问题。", "theme,method,data,contribution", "How does robot transparency affect trust?", "用于论文和 poster。"],
]


RELATION_TYPE_ROWS = [
    ["is_part_of", "属于", "层级、模块、主题从属关系。", "Shared Autonomy -- is_part_of --> Robot Autonomy"],
    ["related_to", "相关", "弱关系或横向主题连接。", "HRI -- related_to --> Human Factors"],
    ["enables", "使能", "技术或方法让某种交互成为可能。", "AR Interface -- enables --> Spatial Robot Guidance"],
    ["constrains", "约束", "安全、场景、能力限制设计空间。", "Safety Requirement -- constrains --> Robot Motion"],
    ["improves", "改善", "设计策略提升体验或指标。", "Robot Transparency -- improves --> Trust Calibration"],
    ["evaluated_by", "被评估", "主题、原型或指标之间的评估关系。", "Service Robot Prototype -- evaluated_by --> Usability Testing"],
    ["used_in", "用于", "方法、技术或概念被应用到场景。", "Wizard-of-Oz -- used_in --> Social Robot Prototyping"],
    ["depends_on", "依赖", "能力或体验依赖某系统模块。", "Shared Autonomy -- depends_on --> Intention Recognition"],
    ["conflicts_with", "冲突", "目标、指标或策略之间存在张力。", "High Autonomy -- conflicts_with --> User Control"],
    ["derived_from", "源自", "概念或机会由文献、方法、图谱路径推导。", "Trust Calibration -- derived_from --> Trust in Automation"],
    ["applied_to", "应用到", "理论或方法应用到具体对象。", "Situated Action -- applied_to --> Service Robot Workflow"],
    ["measured_by", "由……测量", "指标与量表、日志或行为数据连接。", "Workload -- measured_by --> NASA-TLX"],
    ["designed_for", "为……设计", "机会、界面或机器人面向目标用户。", "Hospital Guidance Robot -- designed_for --> Patients"],
    ["supports", "支持", "节点促进流程、目标或研究输出。", "Knowledge Graph -- supports --> Design Opportunity Discovery"],
    ["challenges", "挑战", "技术或场景引出设计困难。", "LLM Agent -- challenges --> Accountability"],
    ["requires", "需要", "任务或评估对条件提出要求。", "Collaborative Assembly -- requires --> Human Safety"],
    ["influences", "影响", "变量之间存在影响但方向强度需研究确认。", "Robot Autonomy -- influences --> Human Trust"],
    ["mediates", "中介", "一个节点作为关系中介。", "Interface Transparency -- mediates --> Autonomy and Trust"],
    ["extends", "扩展", "新主题扩展旧理论或框架。", "GraphRAG -- extends --> RAG"],
]


THEMES = [
    ("Human-Robot Interaction / 人机机器人交互", "研究人与机器人在物理、认知、社会和组织层面的相互作用。", "HRI, role allocation, trust, safety, cooperation", "Robotics; HCI; Human Factors; AI; Design Research", "人如何理解机器人能力和边界？机器人何时应主动、何时应等待？", "literature review; controlled experiment; field study; Wizard-of-Oz", "把机器人从工程对象转成可共同工作的交互对象。", "服务、医疗、工厂、公共空间", "discipline_hri; concept_robot_autonomy; metric_trust", "S01; S23; S33", "HRI 知识图谱与设计机会地图", "不同自主性等级如何影响责任归属？", "半自主服务机器人任务协商原型"),
    ("Human-Computer Interaction / 人机交互", "研究人与计算系统的交互体验、可用性、意义建构和社会影响。", "usability, UX, interaction design, HCI methods", "Computer Science; Design; Psychology", "HCI 方法如何迁移到有身体和物理风险的机器人？", "user research; usability testing; prototyping", "为 HRI 提供用户研究、信息架构和实验设计基础。", "界面、系统、服务、智能代理", "discipline_hci; method_contextual_inquiry", "S14; S15; S24", "HCI-to-HRI 方法转译矩阵", "传统可用性指标在机器人场景是否充分？", "机器人控制界面可用性测试"),
    ("Embodied Interaction / 具身交互", "把行动、身体、材料和情境视为交互意义生成的组成部分。", "embodiment, situated action, affordance, tangible interaction", "HCI; Cognitive Science; Design Theory", "机器人身体和运动如何参与用户理解？", "theory review; observational study; RtD", "提示设计者关注路径、距离、姿态、接触和环境布置。", "移动机器人、协作机械臂、康复机器人", "concept_embodied_interaction; theory_situated_action", "S16; S17", "具身状态表达系统", "运动可读性如何影响协作效率？", "机器人运动意图可视化与实体反馈"),
    ("Embodied AI / 具身智能", "智能体通过身体、感知和行动在真实或模拟环境中学习与推理。", "VLA, grounding, affordance, perception-action loop", "AI; Robotics; Cognitive Science", "大模型如何连接语言、感知和动作？", "paper review; prototype; simulation", "让智能交互设计从对话框转向环境中的行动协商。", "家庭助理、实验室机器人、移动操作", "discipline_embodied_ai; tech_llm_agent_layer", "S27; S28; S29", "LLM-robot 中间层交互设计", "语言规划如何被机器人可供性约束？", "自然语言任务分解与可执行性反馈原型"),
    ("Social Robotics / 社交机器人", "关注机器人作为社会互动对象时的表达、人格、规范、关系和接受度。", "social presence, anthropomorphism, emotion, robotiquette", "Robotics; Social Psychology; HCI", "怎样避免过度拟人化和错误期待？", "questionnaire; Wizard-of-Oz; longitudinal study", "帮助设计情感表达、人格边界和长期关系。", "陪护、教育、导览、娱乐", "robot_social; concept_social_presence; metric_anthropomorphism", "S02; S03; S04; S32", "社交机器人性格与边界设计", "机器人礼貌策略如何影响接受度？", "可调人格服务机器人原型"),
    ("Service Robots / 服务机器人", "在酒店、医疗、家庭、零售、公共服务等场景中执行服务任务的机器人。", "service blueprint, delivery, guidance, recovery", "Service Design; HRI; Operations", "服务失败时机器人如何补救和解释？", "case study; field observation; service blueprint", "连接服务流程、用户情绪和机器人任务能力。", "酒店配送、医院物流、机场导览", "robot_service; scenario_hotel_delivery", "S01; S26", "酒店机器人服务蓝图", "服务接触点中哪些环节适合机器人？", "服务机器人失败恢复流程原型"),
    ("Collaborative Robots / 协作机器人", "与人共享工作空间并协同完成任务的机器人系统。", "cobot, shared workspace, handover, safety", "Industrial Robotics; Human Factors; Ergonomics", "安全约束如何影响直觉界面和效率？", "risk analysis; controlled experiment; ergonomic study", "把安全、可预测运动和角色分配转成设计变量。", "工业装配、实验室自动化、物流分拣", "robot_cobot; metric_safety", "S10; S11; S21; S22; S31", "协作机械臂意图提示系统", "AR 提示能否降低协作装配负荷？", "协作工位路径和安全区 AR 原型"),
    ("Robot Autonomy / 机器人自主性", "机器人从人工控制到完全自主之间的能力、权限和责任分配。", "levels of autonomy, supervisory control, agency", "Automation; Robotics; Human Factors", "自主性提高是否总是提升体验？", "taxonomy; experiment; scenario analysis", "帮助设计控制权、接管机制和责任边界。", "远程巡检、配送、医疗辅助、工厂", "concept_robot_autonomy; theory_levels_automation", "S07; S09; S33", "自主性等级体验对比研究", "不同自主等级如何影响控制感？", "可调自主性控制面板"),
    ("Shared Autonomy / 共享自主性", "人和机器人共同控制任务，系统在必要处辅助、补全或约束人类操作。", "human-in-the-loop, assistance, intent inference", "Robotics; AI; HCI", "系统如何辅助而不剥夺控制感？", "prototype testing; teleoperation experiment", "适合处理不确定场景中的责任分配和控制权转移。", "轮椅、机械臂、远程操作、救援", "concept_shared_autonomy; tech_intention_recognition", "S07; S09", "共享自主控制体验设计", "辅助强度如何影响信任校准？", "可解释共享自主操作台"),
    ("Teleoperation / 远程操作", "人通过远程界面控制或监督机器人在异地执行任务。", "remote control, latency, feedback, situation awareness", "Robotics; Human Factors; XR", "远程操作者如何建立情境感知？", "simulation; controlled experiment; workload study", "强调感知反馈、延迟补偿和空间理解。", "救援、医疗、巡检、空间机器人", "scenario_remote_inspection; metric_situation_awareness", "S20; S33", "远程巡检多模态反馈界面", "触觉反馈是否提升远程操作信任？", "低延迟与解释反馈结合的远程操作原型"),
    ("Multimodal Interaction / 多模态交互", "组合语音、视觉、手势、触觉、实体和空间界面进行输入输出。", "voice, gesture, gaze, haptic, visual feedback", "HCI; HRI; Cognitive Psychology", "哪些模态组合能降低认知负荷而非增加复杂度？", "usability testing; comparative study", "适合为不同场景选择低负荷、高可理解的交互通道。", "公共空间、医疗、工业、家庭", "concept_multimodal_feedback; metric_workload", "S08; S19", "低负荷多模态机器人控制系统", "多模态反馈如何影响 situation awareness？", "语音+AR+触觉协同反馈原型"),
    ("Voice Interaction / 语音交互", "使用自然语言或语音命令与机器人沟通。", "speech command, dialogue repair, natural language", "HCI; NLP; Robotics", "机器人听不懂时如何澄清？", "dialogue prototyping; Wizard-of-Oz", "适合表达目标，但需要处理噪声、歧义和隐私。", "家庭、酒店、护理、导览", "modality_voice; tech_llm_agent_layer", "S27; S28", "机器人澄清对话设计", "澄清策略如何影响用户耐心？", "任务型语音协商原型"),
    ("Gesture Interaction / 手势交互", "使用手势、身体动作或指向来传达命令、注意方向和空间意图。", "pointing, gesture recognition, body language", "HCI; Computer Vision; HRI", "用户手势在动态公共空间中是否可靠？", "field observation; recognition test", "适合近距离、嘈杂或空间目标明确的交互。", "导览、协作装配、家庭服务", "modality_gesture; tech_gesture_recognition", "S01", "服务机器人手势引导体验", "手势和语音组合是否减少误解？", "指向式任务分配原型"),
    ("Gaze Interaction / 视线交互", "通过注视方向、眼动或共同注意建立交互意图。", "gaze cue, joint attention, attention management", "Psychology; HCI; HRI", "机器人视线如何提示注意而不令人不适？", "lab study; behavioral coding", "适合社交机器人、导览和辅助情境。", "陪护、教育、导览", "modality_gaze; concept_social_presence", "S03; S04", "视线提示与共同注意原型", "机器人 gaze cue 如何影响用户信任？", "导览机器人注视与路径提示"),
    ("Haptic Interaction / 触觉交互", "通过力、震动、接触或触觉设备传达状态和控制反馈。", "force feedback, vibration, contact, comfort", "Haptics; Robotics; Ergonomics", "触觉反馈何时增强安全感，何时造成干扰？", "prototype test; workload measure", "适合远程操作、康复、协作机械臂。", "康复、手术、远程操作", "modality_haptic; tech_haptic_feedback", "S08; S19", "触觉式机器人状态反馈", "触觉反馈如何影响错误恢复？", "远程机械臂触觉反馈原型"),
    ("Tangible Interaction / 实体交互", "通过可触摸物件、空间布局和物理控制器与系统交互。", "tangible UI, physical tokens, affordance", "HCI; Industrial Design; Embodied Interaction", "实体控制是否帮助用户理解机器人任务边界？", "RtD; usability test", "把机器人控制从屏幕转为空间和物理操作。", "教育、家庭、协作任务", "modality_tangible; concept_affordance", "S16", "实体化机器人任务编排工具", "物理 token 是否降低任务规划负荷？", "桌面任务编排 tangible prototype"),
    ("AR/MR Interfaces for Robotics / 面向机器人的 AR/MR 界面", "用增强或混合现实显示机器人路径、意图、状态、风险区和任务信息。", "VAM-HRI, virtual design elements, path, safety zone", "XR; HRI; Visualization", "AR 提示能否提高意图理解并避免过度遮挡？", "comparative study; prototype testing", "适合把不可见的机器人计划和传感状态转为可见线索。", "协作工位、公共空间、远程巡检", "tech_ar_mr_interface; modality_visual_ar", "S12; S30", "AR 机器人路径与意图可视化", "AR path preview 如何影响安全感？", "HoloLens / mobile AR 路径提示原型"),
    ("Trust and Explainability / 信任与可解释性", "关注人对机器人能力、意图、风险和决策过程的理解与适当依赖。", "trust calibration, transparency, explanation, reliance", "Human Factors; XAI; HRI", "如何避免过度信任或过低信任？", "questionnaire; behavioral measures; experiment", "解释不是越多越好，而是要服务任务、风险和接管。", "医疗、驾驶、服务、工业", "concept_trust_calibration; concept_explainability", "S05; S06", "信任校准界面", "解释粒度如何影响接管意愿？", "机器人置信度与理由展示原型"),
    ("Safety and Predictability / 安全与可预测性", "关注物理安全、心理安全、运动可预测性、风险沟通和标准合规。", "safety, predictability, risk, legible motion", "Robotics; Ergonomics; Standards", "安全提示如何不降低效率和自然性？", "risk assessment; experiment; standards mapping", "把安全从后台约束变为可理解的交互特征。", "工业协作、公共空间、医疗", "metric_safety; concept_legible_motion", "S10; S13; S21; S22", "安全区与可预测运动设计", "运动可读性是否提升心理安全？", "安全距离可视化与预测路径原型"),
    ("Robot Personality and Emotion / 机器人性格与情感表达", "机器人通过声音、表情、动作、语言风格和节奏传达社会线索。", "personality, emotion, affect, social cues", "Social Robotics; Design; Psychology", "人格是否会造成过度拟人化和责任误解？", "Wizard-of-Oz; questionnaire; longitudinal study", "可用于提升亲近感，但要明确边界和伦理风险。", "陪护、教育、酒店、导览", "concept_anthropomorphism; metric_social_presence", "S02; S03; S04; S32", "可调人格服务机器人", "不同人格强度如何影响服务失败容忍度？", "机器人语气和动作风格原型"),
    ("Human-AI-Robot Collaboration / 人、AI 与机器人协作", "人、AI agent 和机器人共同完成任务，AI 可能成为解释、规划和协商中间层。", "LLM agent, planner, mediator, shared control", "AI; Robotics; HCI; CSCW", "AI agent 的建议和机器人动作如何对齐？", "scenario prototyping; task simulation", "把大模型能力转成可验证、可接管、可追责的 HRI 流程。", "家庭、办公、实验室、服务", "tech_llm_agent_layer; concept_graph_rag", "S27; S28; S29", "LLM 机器人任务协商系统", "LLM 中间层会提升还是削弱用户控制感？", "LLM + robot planning dashboard"),
    ("Design Research for Robotics / 面向机器人的设计研究", "用设计研究方法把机器人技术、用户场景和社会意义转化为知识与原型。", "RtD, service design, case study, prototyping", "Design Research; HCI; HRI", "设计产物如何成为研究贡献？", "RtD; case study; participatory design", "帮助作品集从造型展示升级为研究型项目。", "服务、公共空间、医疗、教育", "discipline_design_research; theory_rtd", "S14; S15", "机器人设计研究作品集系统", "原型如何承载 HRI 理论？", "设计机会卡 + 原型 + 评估组合"),
    ("Evaluation Methods in HRI / HRI 评估方法", "面向 HRI 原型和系统的可用性、信任、安全、负荷、接受度和长期影响评估。", "metrics, questionnaire, behavioral data, field study", "Human Factors; HCI; Statistics", "什么指标能证明设计改变了协作质量？", "controlled experiment; usability testing; longitudinal study", "为报告、poster 和论文提供证据链。", "所有 HRI 项目", "metric_usability; metric_trust; metric_workload", "S04; S05; S08; S18; S19; S20", "HRI 评估指标选择器", "不同指标组合如何适配不同场景？", "评估方法推荐工具"),
    ("Ethics, Privacy, and Social Impact / 伦理、隐私与社会影响", "关注机器人采集数据、参与劳动、影响关系和介入脆弱场景时的社会后果。", "privacy, consent, accountability, bias, access", "STS; Ethics; Law; HCI", "机器人系统的责任链如何被用户理解？", "ethics review; stakeholder mapping; speculative design", "为服务机器人和 AI agent 添加必要的边界、告知和反滥用机制。", "医疗、养老、家庭、公共空间、工作场所", "ethics_society; concept_human_agency", "S21; S22; S23", "机器人伦理交互审计", "透明告知如何影响接受度？", "机器人隐私与同意流程原型"),
]


METHODS = [
    ["Literature Review", "文献综述", "汇总并解释现有研究，用于建立概念、问题和证据基础。", "前期定义范围", "快速形成领域地图", "可能不够系统", "知识图谱初始构建"],
    ["Systematic Review", "系统综述", "用明确检索式、筛选标准和记录流程综合证据。", "研究问题明确后", "可复现、可信度高", "耗时，范围需要收窄", "投稿或毕业论文"],
    ["Taxonomy Building", "分类法构建", "把概念、案例或界面元素按维度归类。", "图谱建模", "便于组织复杂领域", "容易过度简化", "AR/MR HRI 分类"],
    ["User Interview", "用户访谈", "收集用户经验、期待和痛点。", "发现问题", "获得深层解释", "依赖样本和访谈能力", "服务机器人用户研究"],
    ["Contextual Inquiry", "情境访查", "在真实使用环境中观察并询问。", "场景研究", "连接流程和环境约束", "进入现场困难", "医院/酒店服务流程"],
    ["Field Observation", "现场观察", "记录真实行为、空间和社会规范。", "场景定义", "发现隐性规则", "难以控制变量", "公共空间机器人"],
    ["Participatory Design", "参与式设计", "让用户和利益相关者参与构思与评估。", "概念生成", "提高接受度和贴合度", "协调成本高", "医疗/养老机器人"],
    ["Co-design", "共同设计", "设计者、用户、技术人员共同探索方案。", "概念与原型", "促进跨学科对齐", "产出可能发散", "HRI 设计工作坊"],
    ["Wizard-of-Oz", "绿野仙踪原型", "由人隐藏控制系统来模拟机器人智能。", "早期 HRI 原型", "低成本验证交互", "容易高估真实系统能力", "语音/社交机器人"],
    ["Prototype Testing", "原型测试", "用低/中/高保真原型评估概念。", "迭代阶段", "快速获得反馈", "生态效度有限", "AR 路径提示"],
    ["Usability Testing", "可用性测试", "测量任务完成、错误、理解和满意度。", "界面验证", "直接可操作", "不足以覆盖长期信任", "机器人控制界面"],
    ["Controlled Experiment", "控制实验", "操纵变量并测量因果影响。", "验证假设", "因果证据强", "真实场景复杂性不足", "解释粒度对信任影响"],
    ["Longitudinal Study", "长期研究", "观察用户和机器人长期共处与习惯形成。", "部署后", "理解关系和采纳", "成本高、变量多", "家庭/养老机器人"],
    ["Research through Design", "通过设计进行研究", "通过创造和反思设计产物生成知识。", "探索性研究", "适合开放问题", "评价标准需清晰", "作品集/CHI pictorial"],
    ["Speculative Design", "思辨设计", "用未来情境引发讨论和价值判断。", "伦理与未来研究", "揭示社会后果", "不直接验证可用性", "机器人伦理边界"],
    ["Design Fiction", "设计虚构", "用故事、道具和场景表达未来系统。", "概念探索", "适合复杂社会技术系统", "可能被误读为概念宣传", "LLM 机器人未来服务"],
    ["Case Study", "案例研究", "深入分析一个或多个真实案例。", "中期分析", "保留情境复杂性", "泛化有限", "酒店机器人服务案例"],
    ["Comparative Study", "比较研究", "比较不同界面、模态或自主等级。", "方案选择", "利于设计决策", "需要控制条件", "语音 vs AR 指令"],
    ["Service Blueprinting", "服务蓝图", "绘制用户、前台、后台和支持系统。", "服务机器人设计", "连接流程和组织", "需要现场资料", "酒店/医院机器人"],
    ["Knowledge Graph Modeling", "知识图谱建模", "把概念、证据、机会和问题结构化为节点关系。", "知识库建设", "适合 LLM 复用", "维护成本高", "GraphRAG 研究助手"],
]


METRICS = [
    ["Usability", "可用性", "用户完成任务的效率、效果和满意度。", "SUS、任务完成率、错误率", "机器人界面与控制流程", "界面复杂、状态不可见"],
    ["Trust", "信任", "用户对机器人能力、意图和可靠性的依赖倾向。", "HRI trust questionnaire、行为依赖", "自主机器人、AI agent", "过度信任/不信任"],
    ["Acceptance", "接受度", "用户愿意采用和持续使用机器人的程度。", "Almere model、UTAUT 变量", "社交/服务机器人", "有用性、易用性、社会影响"],
    ["Workload", "工作负荷", "任务带来的认知、身体和时间压力。", "NASA-TLX", "远程操作、协作任务", "多模态复杂度"],
    ["Situation Awareness", "情境感知", "用户对系统、环境和未来状态的理解。", "SAGAT、问卷、行为日志", "远程操作、AR 提示", "状态和路径不可见"],
    ["Safety", "安全", "物理和心理风险控制程度。", "碰撞/近失事件、感知安全量表", "协作机器人、公共空间", "路径、速度、距离"],
    ["Transparency", "透明性", "系统状态、意图和限制是否可理解。", "透明性感知问卷、理解测试", "自主机器人", "黑箱决策"],
    ["Explainability", "可解释性", "系统能否给出与任务相关的理由和不确定性。", "解释理解、接管正确率", "LLM agent、规划系统", "解释过多/过少"],
    ["Perceived Intelligence", "感知智能", "用户认为机器人聪明、适应和有能力的程度。", "Godspeed 相关维度", "社交和服务机器人", "能力展示与实际能力不一致"],
    ["Social Presence", "社会临场感", "用户感到机器人像社会参与者的程度。", "social presence scales", "社交、教育、陪护机器人", "过度拟人化"],
    ["Anthropomorphism", "拟人化", "用户将人类特质归因给机器人。", "Godspeed anthropomorphism", "社交机器人", "错误期待、伦理风险"],
    ["Comfort", "舒适度", "用户在空间、距离、速度和交互方式上的舒适感。", "舒适度问卷、距离行为", "公共空间、协作机器人", "接近速度和空间侵入"],
    ["Engagement", "参与度", "用户持续关注和参与互动的程度。", "观察编码、停留时间、互动频次", "教育、导览、陪护", "长期新鲜感衰减"],
    ["Learnability", "易学性", "用户学习使用系统所需成本。", "首次任务成功率、学习曲线", "新机器人服务", "指令复杂"],
    ["Error Recovery", "错误恢复", "系统和用户从失败中恢复的能力。", "恢复时间、成功率、满意度", "服务机器人、LLM agent", "失败解释和补救路径"],
    ["Long-Term Adoption", "长期采纳", "系统进入日常习惯和组织流程的程度。", "日志、访谈、留存", "家庭、养老、工作场所", "维护、信任、社会规范"],
    ["Legibility", "运动可读性", "人能否从机器人部分动作推断其目标。", "目标推断准确率", "协作机械臂、移动机器人", "意图不清"],
    ["Predictability", "可预测性", "机器人动作是否符合人对其行为的预期。", "轨迹预测、反应时间", "协作任务", "突然动作"],
    ["Sense of Control", "控制感", "用户感到自己能影响系统行为的程度。", "控制感量表、接管行为", "共享自主", "自主性过高"],
    ["Accountability Clarity", "责任清晰度", "用户是否理解谁对决策和结果负责。", "情境判断题、访谈", "高风险 HRI、LLM 机器人", "责任模糊"],
]


SCENARIOS = [
    ["酒店配送", "Service Robot", "住客、前台、保洁", "送物、引导、通知", "服务失败、路径干扰、语气边界", "失败恢复与服务蓝图"],
    ["医院导诊", "Service Robot", "患者、家属、护士", "导航、排队、说明", "焦虑、隐私、无障碍", "低负荷引导与交接"],
    ["康复训练", "Rehabilitation Robot", "患者、治疗师", "动作训练、反馈", "安全、动力、长期坚持", "触觉/视觉反馈"],
    ["家庭陪伴", "Social Robot", "儿童、老人、家庭成员", "提醒、陪伴、轻服务", "隐私、情感依赖、角色边界", "人格边界和同意机制"],
    ["工业装配", "Cobot", "操作员、工程师", "协同装配、递送工具", "安全区、意图、节拍", "AR 路径与角色分配"],
    ["实验室自动化", "Mobile Manipulator", "研究员、技术员", "样品搬运、仪器操作", "错误成本、责任、追踪", "可解释任务日志"],
    ["公共空间清洁", "Service Robot", "路人、保洁、管理者", "清扫、避让、警示", "社会规范、拥挤、误解", "robotiquette 与状态表达"],
    ["博物馆导览", "Social Robot", "游客、儿童、馆员", "讲解、引导、问答", "注意力、群体互动", "gaze 与路径提示"],
    ["机场问询", "Service Robot", "旅客、工作人员", "问询、路线、语言支持", "多语言、焦虑、拥堵", "多模态导引"],
    ["远程巡检", "Telepresence Robot", "操作员、现场人员", "巡检、确认、记录", "情境感知、延迟", "远程操作反馈"],
    ["餐饮送餐", "Service Robot", "顾客、服务员", "配送、取餐、避让", "路线拥堵、礼貌", "状态灯与语音边界"],
    ["商场导购", "Service Robot", "消费者、店员", "推荐、导航、促销", "打扰、隐私、可信度", "可拒绝的主动交互"],
    ["学校教育", "Social Robot", "学生、教师", "教学辅助、互动", "注意力、权威、数据", "教育机器人角色设计"],
    ["仓储分拣", "Mobile Robot", "工人、调度员", "搬运、协作", "安全、预测、效率", "可预测路径和调度界面"],
    ["养老机构", "Assistive Robot", "老人、护理员、家属", "提醒、陪伴、护理支持", "依赖、接受度、隐私", "长期关系与护理流程"],
    ["智能家居", "Home Robot", "家庭成员", "清洁、巡逻、提醒", "共享空间、信任", "家庭机器人行为规范"],
    ["农业机器人", "Field Robot", "农户、技术员", "巡田、采摘、喷洒", "环境不确定、解释", "低技术门槛控制"],
    ["建筑工地", "Mobile Robot", "工人、管理者", "巡检、搬运", "高风险、动态环境", "安全可视化"],
    ["灾害救援", "Teleoperation Robot", "救援人员", "搜索、探测、传递信息", "延迟、压力、负荷", "高压情境感知界面"],
    ["零售库存", "Mobile Robot", "店员、顾客", "盘点、导航", "顾客干扰、可见性", "公共空间机器人礼仪"],
]


OPPORTUNITIES = [
    ["AR 机器人路径与意图可视化", "协作工人、公共空间用户", "工厂/商场/医院", "用户难以预测机器人下一步", "AR/MR Interface; Legible Motion; Safety", "移动 AR / HoloLens 原型", "Situation Awareness; Safety; Workload", "视觉冲击力强，能展示系统图和实验设计"],
    ["服务机器人失败恢复体验系统", "酒店住客、前台", "酒店配送", "机器人失败时用户不知道发生了什么", "Failure Recovery; Service Robot; Trust", "服务蓝图 + 对话原型", "Trust; Error Recovery; Satisfaction", "适合做完整服务设计 case"],
    ["协作机械臂意图表达界面", "工厂操作员", "协作装配", "机械臂动作目标不透明", "Cobot; Legibility; AR Interface", "灯光/投影/AR 轨迹", "Legibility; Safety; Workload", "体现工业设计与 HRI 结合"],
    ["LLM 机器人任务协商中间层", "家庭用户、办公人员", "家庭/办公室", "自然语言指令不一定可执行", "LLM Agent; Affordance; Shared Autonomy", "对话 + 可执行性反馈界面", "Trust; Sense of Control; Error Recovery", "前沿且能体现 AI agent 设计能力"],
    ["老年陪护机器人边界与同意机制", "老人、护理员、家属", "养老机构/家庭", "陪伴与监控容易越界", "Social Robot; Privacy; Acceptance", "服务流程 + 隐私控制原型", "Acceptance; Comfort; Accountability", "有伦理深度和社会价值"],
    ["多模态低负荷机器人控制", "医院工作人员", "医院物流", "语音或屏幕单一模态负荷高", "Voice; Gesture; AR; Workload", "语音+手势+视觉反馈原型", "NASA-TLX; Usability", "适合做对比实验"],
    ["公共空间机器人礼仪 Robotiquette", "路人、空间管理者", "商场/机场/博物馆", "机器人在人群中容易打扰或造成紧张", "Social Norms; Safety; Comfort", "行为规范卡 + 状态表达原型", "Comfort; Social Presence; Safety", "能连接设计研究和社会规范"],
    ["医院机器人交接 Handover 体验", "护士、患者、机器人调度员", "医院病区", "人机交接责任不清", "Task; Accountability; Service Blueprint", "交接界面 + 任务日志", "Accountability; Trust; Error Recovery", "问题真实且流程复杂"],
    ["远程巡检情境感知仪表盘", "巡检操作员", "危险/远程场地", "远程操作者缺乏空间和风险理解", "Teleoperation; Situation Awareness; Haptic Feedback", "地图+视频+触觉提示界面", "Situation Awareness; Workload", "适合 poster 和原型演示"],
    ["机器人性格强度调节器", "服务机器人运营者", "酒店/零售/导览", "固定人格不适配所有场景", "Personality; Anthropomorphism; Acceptance", "人格参数面板 + 对话原型", "Godspeed; Acceptance", "设计变量清晰，易测试"],
    ["家庭机器人任务可供性卡片", "家庭成员", "智能家居", "用户不知道机器人能做什么和不能做什么", "Affordance; LLM Agent; Task", "卡片式任务编排工具", "Learnability; Trust", "信息架构和实体交互结合"],
    ["协作机器人安全区可视化", "工厂操作员", "共享工作站", "安全约束隐藏在后台", "Safety; ISO 15066; AR", "投影/灯光安全区", "Perceived Safety; Efficiency", "有明确标准映射"],
    ["机器人不确定性表达语言", "公共服务用户", "公共服务", "机器人不确定时常表现得过于确定", "Transparency; Explainability; Trust Calibration", "状态语句库 + UI patterns", "Trust Calibration; Error Recovery", "适合设计系统化输出"],
    ["康复机器人鼓励与反馈系统", "康复患者、治疗师", "康复训练", "反馈不够个性化或过度机械", "Haptic; Emotion; Longitudinal", "动作反馈 + 情绪支持原型", "Engagement; Comfort; Adoption", "有人文与身体交互价值"],
    ["博物馆机器人共同注意导览", "游客、儿童", "博物馆", "机器人讲解难以协调群体注意", "Gaze; Social Presence; Guidance", "视线/灯光/路径提示", "Engagement; Social Presence", "适合空间体验作品集"],
    ["机器人责任链可视化日志", "操作者、管理者、用户", "高风险服务/实验室", "AI/机器人/人谁负责不清", "Accountability; LLM Agent; Task Log", "可解释任务时间线", "Accountability Clarity; Trust", "研究价值强"],
    ["服务机器人排队与等待体验", "患者、旅客、顾客", "医院/机场/餐饮", "等待中的机器人状态不可见", "Status Visibility; Service Robot; Comfort", "等待状态屏 + 语音提示", "Satisfaction; Comfort", "小切口但落地"],
    ["儿童教育机器人可控拟人化", "儿童、教师、家长", "学校/家庭", "过度拟人化影响认知和依赖", "Anthropomorphism; Ethics; Social Robot", "人格边界 + 家长控制", "Anthropomorphism; Acceptance", "有伦理和教育意义"],
    ["低技术门槛农业机器人控制", "农户、技术员", "农业场景", "复杂控制界面不适合现场使用", "Service Robot; Voice; Tangible UI", "实体控制器 + 语音确认", "Usability; Workload", "体现包容性设计"],
    ["机器人长期关系维护机制", "家庭/养老用户", "长期陪护场景", "短期好感不能代表长期采纳", "Long-Term Adoption; Social Presence; Privacy", "长期互动日程与边界设置", "Long-Term Adoption; Trust", "适合研究型作品集延伸"],
]


RESEARCH_QUESTIONS = [
    ["机器人自主性等级如何影响用户控制感与责任归属？", "Robot Autonomy", "Controlled Experiment", "接管次数、信任问卷、责任判断题", "区分效率、自主性和控制感的关系", "论文/poster"],
    ["AR 路径提示是否提升用户对移动机器人意图的理解？", "AR/MR HRI", "Comparative Study", "目标推断准确率、NASA-TLX", "验证 VAM-HRI 设计元素价值", "作品集/CHI LBW"],
    ["服务机器人失败解释的粒度如何影响信任校准？", "Trust and Explainability", "Wizard-of-Oz + Questionnaire", "信任变化、恢复时间、访谈", "形成失败恢复设计原则", "poster"],
    ["LLM agent 作为机器人中间层会提升还是削弱用户控制感？", "Human-AI-Robot Collaboration", "Prototype Testing", "控制感、接管意愿、错误理解", "连接 AI agent 和 HRI", "论文雏形"],
    ["多模态反馈如何降低远程操作中的认知负荷？", "Teleoperation", "Controlled Experiment", "NASA-TLX、任务完成时间", "为远程操作界面提供证据", "poster"],
    ["社交机器人人格强度是否影响服务失败后的用户容忍度？", "Social Robotics", "Wizard-of-Oz", "Godspeed、满意度、访谈", "拟人化边界设计", "作品集"],
    ["公共空间机器人如何通过行为礼仪减少打扰感？", "Ethics and Society", "Field Observation + RtD", "观察编码、舒适度问卷", "robotiquette 设计模式", "设计研究"],
    ["协作机械臂运动可读性与效率之间是否存在权衡？", "Safety and Predictability", "Controlled Experiment", "目标推断、装配时间、安全事件", "连接 motion planning 和体验", "论文"],
    ["实体任务卡是否帮助家庭用户理解机器人可供性？", "Tangible Interaction", "Usability Testing", "学习时间、任务成功率", "降低智能系统黑箱感", "作品集"],
    ["机器人状态可见性如何影响等待体验？", "Service Robots", "Field Study", "等待满意度、状态理解", "服务机器人微交互原则", "poster"],
    ["老年用户如何理解陪护机器人的数据采集边界？", "Ethics and Privacy", "Interview + Participatory Design", "隐私心智模型、控制偏好", "脆弱群体保护框架", "论文"],
    ["机器人 gaze cue 是否促进导览场景中的共同注意？", "Gaze Interaction", "Lab Study", "视线跟随、记忆测试、参与度", "社交线索设计", "poster"],
    ["触觉反馈是否能改善远程机械臂的错误恢复？", "Haptic Interaction", "Prototype Testing", "恢复成功率、工作负荷", "多模态反馈机制", "论文"],
    ["医院机器人交接日志能否提升责任清晰度？", "Accountability", "Scenario-based Evaluation", "责任判断、访谈", "高风险服务设计", "作品集"],
    ["不同用户群体对机器人主动性的接受阈值有何差异？", "Acceptance", "Survey + Interview", "接受度、场景偏好", "场景化主动交互准则", "研究报告"],
    ["协作机器人安全区可视化是否影响心理安全和效率？", "Collaborative Robots", "Comparative Study", "感知安全、任务效率", "安全设计可视化证据", "poster"],
    ["机器人情绪表达在康复训练中如何影响坚持度？", "Robot Emotion", "Longitudinal Study", "参与频次、情绪反馈", "长期 HRI 设计", "论文"],
    ["语音澄清策略如何影响用户对机器人智能的感知？", "Voice Interaction", "Wizard-of-Oz", "perceived intelligence、任务成功", "对话修复设计", "作品集"],
    ["GraphRAG 是否能帮助设计师更系统地产生 HRI 机会点？", "LLM Reuse", "Design Study", "机会质量评分、访谈", "知识库辅助设计方法", "论文"],
    ["服务蓝图能否帮助发现机器人部署中的非界面问题？", "Design Research", "Case Study", "触点问题、利益相关者反馈", "机器人服务设计方法论", "作品集"],
]


GLOSSARY = [
    ["Human-Robot Interaction", "人机机器人交互", "研究人与机器人之间的物理、认知、社会和组织互动。", "HCI; Robotics; Human Factors", "为机器人设计提供跨学科框架。", "医院导诊机器人"],
    ["Human-Computer Interaction", "人机交互", "研究人与计算系统之间的交互体验和影响。", "UX; Usability; Interaction Design", "提供用户研究与界面评估方法。", "机器人控制界面"],
    ["Intelligent Interaction Design", "智能交互设计", "面向具备感知、推理或自主能力系统的交互设计。", "AI; HCI; HRI", "关注不确定性、解释和人机协作。", "LLM 机器人任务协商"],
    ["Robotics", "机器人学", "研究能感知、决策并行动的物理系统。", "Control; Perception; Planning", "帮助设计师理解系统边界。", "移动操作机器人"],
    ["Embodied AI", "具身智能", "通过身体、环境和行动实现智能的 AI/机器人研究方向。", "VLA; Affordance; Grounding", "把语言任务转成可执行行动。", "家庭机器人执行自然语言任务"],
    ["Embodied Interaction", "具身交互", "强调身体、行动和情境参与交互意义生成。", "Tangible UI; Situated Action", "提示关注空间、动作、材料。", "协作机械臂路径表达"],
    ["Social Robotics", "社交机器人", "关注机器人作为社会互动对象的表达与关系。", "Anthropomorphism; Social Presence", "帮助设计人格和情感边界。", "陪护机器人"],
    ["Service Robot", "服务机器人", "在非制造场景为人或组织提供服务的机器人。", "Delivery; Guidance; Cleaning", "需要融入服务流程。", "酒店配送机器人"],
    ["Collaborative Robot", "协作机器人", "与人共享工作空间并协同完成任务的机器人。", "Cobot; Safety; Handover", "强调安全和意图理解。", "协作装配"],
    ["Shared Autonomy", "共享自主性", "人和机器人共同控制任务的自主方式。", "Human-in-the-loop; Intent Recognition", "平衡辅助与控制感。", "共享控制机械臂"],
    ["Teleoperation", "远程操作", "人远程控制或监督机器人。", "Latency; Situation Awareness", "需要强反馈和低负荷界面。", "灾害救援机器人"],
    ["Multimodal Interaction", "多模态交互", "组合多种输入输出模态。", "Voice; Gesture; Haptic; AR", "降低单一模态局限。", "语音+AR 路径提示"],
    ["Voice Interaction", "语音交互", "通过语音命令、对话和澄清完成任务。", "NLP; Dialogue Repair", "适合目标表达但需处理歧义。", "家庭机器人命令"],
    ["Gesture Interaction", "手势交互", "通过身体动作或指向传达意图。", "Computer Vision; Spatial Reference", "适合空间目标。", "指向桌上物体"],
    ["Gaze Interaction", "视线交互", "用注视方向建立注意和意图线索。", "Joint Attention; Social Cue", "增强社会性与导览。", "博物馆机器人"],
    ["Haptic Interaction", "触觉交互", "用力、震动、接触提供反馈。", "Force Feedback; Comfort", "提升远程操作和康复体验。", "远程机械臂"],
    ["Tangible Interaction", "实体交互", "用物理物件参与信息操作。", "Affordance; Embodiment", "让抽象任务可触摸。", "任务编排卡片"],
    ["AR/MR Interface", "增强/混合现实界面", "在真实环境叠加虚拟信息。", "VAM-HRI; Path Visualization", "显示机器人不可见计划。", "AR 安全区"],
    ["Robot Autonomy", "机器人自主性", "机器人独立感知、决策和行动的程度。", "Levels of Automation; Agency", "影响信任、责任和接管。", "自主配送机器人"],
    ["Trust Calibration", "信任校准", "让用户信任程度匹配系统真实能力。", "Trust; Transparency", "避免过度信任和不用。", "解释机器人局限"],
    ["Transparency", "透明性", "系统状态、逻辑和限制可被理解的程度。", "Explainability; Visibility", "支持接管和信任。", "任务置信度显示"],
    ["Explainability", "可解释性", "系统能给出任务相关解释。", "XAI; Robot Planning", "帮助理解失败与决策。", "机器人说明绕路原因"],
    ["Legibility", "可读性", "人能从部分动作推断机器人目标。", "Motion Planning; Intent", "提升协作流畅性。", "机械臂朝目标移动"],
    ["Predictability", "可预测性", "机器人行为符合人的预期。", "Safety; Motion", "减少惊吓与风险。", "移动机器人避让"],
    ["Situation Awareness", "情境感知", "理解环境状态、意义和未来变化。", "Teleoperation; AR", "远程和复杂场景关键指标。", "巡检仪表盘"],
    ["Workload", "工作负荷", "任务对认知、身体和时间资源的要求。", "NASA-TLX", "评估界面是否减负。", "多模态控制对比"],
    ["Usability", "可用性", "任务完成的效率、效果与满意度。", "SUS; Task Success", "基础交互质量指标。", "机器人 app"],
    ["Acceptance", "接受度", "用户愿意采用机器人的程度。", "Almere Model; UTAUT", "服务机器人部署关键。", "养老机器人"],
    ["Social Presence", "社会临场感", "机器人被感知为社会参与者的程度。", "Anthropomorphism; Emotion", "影响陪伴和导览体验。", "儿童教育机器人"],
    ["Anthropomorphism", "拟人化", "将人类特质归因给机器人。", "Godspeed; Social Robot", "既能亲近也会误导。", "表情机器人"],
    ["Wizard-of-Oz", "绿野仙踪法", "由人隐藏模拟系统智能的原型测试方法。", "Prototype; HRI", "早期验证智能交互。", "语音机器人测试"],
    ["Research through Design", "通过设计进行研究", "通过设计产物与反思生成知识。", "RtD; Annotated Portfolio", "适合作品集和设计研究。", "机器人未来交互原型"],
    ["Service Blueprint", "服务蓝图", "映射用户、前台、后台与支持流程。", "Service Design; Scenario", "发现非界面问题。", "酒店机器人服务"],
    ["GraphRAG", "图谱增强检索生成", "结合知识图谱关系和文本检索的 LLM 复用方式。", "Knowledge Graph; RAG", "支持研究助手和机会生成。", "HRI 设计问答"],
    ["Knowledge Triple", "知识三元组", "Subject-Predicate-Object 关系表达。", "Ontology; Graph", "机器可读和可扩展。", "Trust -- measured_by --> Questionnaire"],
    ["Ontology", "本体", "定义领域中类目、关系和约束的结构。", "Schema; Taxonomy", "保证知识库一致性。", "HRI 顶层本体"],
    ["Node", "节点", "知识图谱中的实体或概念。", "Relation; Evidence", "承载定义和证据。", "Shared Autonomy 节点"],
    ["Relation", "关系", "节点之间的语义连接。", "Triple; Predicate", "表达因果、从属和应用。", "AR enables Guidance"],
    ["Evidence", "证据", "支持节点或关系的来源。", "Paper; Standard; Case", "保证可回溯。", "DOI 链接"],
    ["Design Opportunity", "设计机会", "可转化为项目、原型或研究的问题空间。", "Research Question; Prototype", "连接图谱与作品集。", "失败恢复系统"],
    ["Research Question", "研究问题", "可被方法和数据回答的问题。", "Method; Metric", "连接研究和输出。", "AR 提示是否提升意图理解"],
    ["Robotiquette", "机器人礼仪", "机器人在人类社会场景中的行为规范。", "Social Norms; Comfort", "公共空间部署关键。", "避让和打招呼"],
    ["Human Agency", "人类能动性", "人保有选择、控制和影响系统的能力感。", "Control; Autonomy", "防止智能系统越权。", "接管按钮"],
    ["Failure Recovery", "失败恢复", "系统识别、解释和补救失败的能力。", "Error Recovery; Trust", "决定服务体验韧性。", "配送失败改派"],
    ["Role Allocation", "角色分配", "人与机器人之间的任务、权力和责任划分。", "Autonomy; Task", "影响协作效率与责任。", "人确认机器人执行"],
    ["Handover", "交接", "人与机器人交换物体、任务或责任。", "Cobot; Service", "高频且高风险接触点。", "药品交接"],
    ["Status Visibility", "状态可见性", "用户能否知道系统当前和未来状态。", "Transparency; Feedback", "降低不确定性。", "等待进度显示"],
    ["Perception", "感知", "机器人获取环境、人和物体信息的能力。", "Sensors; Scene Understanding", "决定反馈和错误解释。", "识别障碍物"],
    ["Planning", "规划", "机器人选择动作序列以达成目标。", "Motion Planning; Decision", "影响路径和意图可读性。", "绕路规划"],
    ["Intention Recognition", "意图识别", "系统推断人的目标或意图。", "Shared Autonomy; Gesture", "支持主动辅助。", "识别用户指向"],
    ["Human Safety", "人体安全", "避免身体伤害和心理不适。", "ISO; Risk", "设计底线。", "安全速度限制"],
]


def node(
    node_id: str,
    label: str,
    zh_label: str,
    node_type: str,
    definition: str,
    parent: str = "",
    related: list[str] | None = None,
    evidence: list[str] | None = None,
    scenarios: list[str] | None = None,
    questions: list[str] | None = None,
    relevance: str = "",
    portfolio: str = "",
    confidence: str = "medium",
) -> dict:
    return {
        "id": node_id,
        "label": label,
        "zh_label": zh_label,
        "type": node_type,
        "definition": definition,
        "parent": parent,
        "children": [],
        "related_nodes": related or [],
        "evidence": evidence or [],
        "design_relevance": relevance,
        "application_scenarios": scenarios or [],
        "research_questions": questions or [],
        "portfolio_potential": portfolio,
        "confidence_level": confidence,
    }


NODES = [
    node("discipline_hri", "Human-Robot Interaction", "人机机器人交互", "Discipline", "研究人与机器人之间的物理、认知、社会和组织互动。", evidence=["S01", "S23", "S33"], relevance="作为整个知识图谱的中心学科。", confidence="high"),
    node("discipline_hci", "Human-Computer Interaction", "人机交互", "Discipline", "研究人与计算系统的交互体验、方法和社会影响。", evidence=["S14", "S24"], confidence="high"),
    node("discipline_robotics", "Robotics", "机器人学", "Discipline", "研究能感知、决策并在物理世界行动的系统。", evidence=["S25", "S26"], confidence="high"),
    node("discipline_design_research", "Design Research", "设计研究", "Discipline", "通过研究方法和设计实践生成设计知识。", evidence=["S14", "S15"], confidence="high"),
    node("discipline_human_factors", "Human Factors", "人因工程", "Discipline", "研究人类能力、限制和系统绩效之间的关系。", evidence=["S05", "S06", "S19", "S20"], confidence="high"),
    node("discipline_embodied_ai", "Embodied AI", "具身智能", "Discipline", "关注智能体在环境中的感知、行动和 grounding。", evidence=["S27", "S28", "S29"], relevance="连接 AI 与机器人实际行动。", confidence="medium"),
    node("concept_intelligent_interaction_design", "Intelligent Interaction Design", "智能交互设计", "Concept", "面向具备感知、推理、学习或自主能力系统的交互设计。", related=["discipline_hci", "discipline_hri"], relevance="本课题的设计学入口。", confidence="medium"),
    node("concept_embodied_interaction", "Embodied Interaction", "具身交互", "Concept", "行动、身体、空间和情境共同构成交互意义。", evidence=["S16"], relevance="帮助设计师关注机器人身体和动作。", confidence="high"),
    node("theory_situated_action", "Situated Action", "情境行动", "Theory", "行动不是计划的机械执行，而是在情境中不断调整。", evidence=["S17"], confidence="high"),
    node("theory_levels_automation", "Levels of Automation", "自动化等级理论", "Theory", "自动化可分布在信息获取、分析、决策和行动等功能中。", evidence=["S07"], confidence="high"),
    node("theory_rtd", "Research through Design", "通过设计进行研究", "Theory", "设计产物和反思可以生成 HCI/设计研究知识。", evidence=["S14", "S15"], confidence="high"),
    node("concept_robot_autonomy", "Robot Autonomy", "机器人自主性", "Concept", "机器人独立感知、决策和行动的程度。", evidence=["S07", "S09"], relevance="决定控制权和责任分配。", confidence="high"),
    node("concept_shared_autonomy", "Shared Autonomy", "共享自主性", "Concept", "人与机器人共同完成控制和决策。", parent="concept_robot_autonomy", related=["concept_human_agency", "tech_intention_recognition"], relevance="适合远程操作、辅助控制和复杂服务任务。", confidence="medium"),
    node("concept_human_agency", "Human Agency", "人类能动性", "Concept", "用户保有选择、控制和影响系统行为的能力感。", related=["concept_robot_autonomy"], relevance="防止智能系统越权。", confidence="medium"),
    node("concept_trust_calibration", "Trust Calibration", "信任校准", "Concept", "让用户信任程度匹配机器人真实能力。", evidence=["S05", "S06"], relevance="HRI 设计不能只追求更高信任。", confidence="high"),
    node("concept_transparency", "Transparency", "透明性", "Concept", "系统状态、逻辑、边界和不确定性可被用户理解的程度。", evidence=["S06"], relevance="支持接管、责任和信任校准。", confidence="high"),
    node("concept_explainability", "Explainability", "可解释性", "Concept", "机器人或 AI 给出与任务相关的理由、限制和不确定性。", evidence=["S06", "S27"], relevance="连接 LLM agent 与 HRI 责任。", confidence="medium"),
    node("concept_legible_motion", "Legible Motion", "可读运动", "Concept", "机器人动作能让人快速推断目标。", evidence=["S13"], relevance="对协作机器人和公共空间机器人非常关键。", confidence="high"),
    node("concept_predictability", "Predictability", "可预测性", "Concept", "机器人行为符合用户预期。", evidence=["S13"], confidence="high"),
    node("concept_situation_awareness", "Situation Awareness", "情境感知", "Concept", "用户理解当前环境、意义和未来变化。", evidence=["S20"], confidence="high"),
    node("concept_social_presence", "Social Presence", "社会临场感", "Concept", "机器人被感知为社会参与者的程度。", evidence=["S02", "S03", "S04"], confidence="high"),
    node("concept_anthropomorphism", "Anthropomorphism", "拟人化", "Concept", "用户将人类特质归因给机器人。", evidence=["S04"], confidence="high"),
    node("concept_failure_recovery", "Failure Recovery", "失败恢复", "Concept", "系统识别、解释并补救失败的能力。", related=["concept_transparency", "metric_error_recovery"], relevance="决定服务体验是否有韧性。", confidence="medium"),
    node("concept_multimodal_feedback", "Multimodal Feedback", "多模态反馈", "Concept", "通过视觉、语音、触觉、动作等多通道反馈状态和意图。", evidence=["S08"], confidence="medium"),
    node("concept_affordance", "Affordance", "可供性", "Concept", "环境或系统向行动者提供的可行动可能。", related=["concept_embodied_interaction"], relevance="帮助解释机器人任务可执行性。", confidence="medium"),
    node("concept_role_allocation", "Role Allocation", "角色分配", "Concept", "在人、AI 和机器人之间划分任务、权限和责任。", evidence=["S07", "S09"], confidence="high"),
    node("concept_graph_rag", "GraphRAG", "图谱增强检索生成", "Concept", "结合图谱关系和文档检索进行 LLM 推理与生成。", relevance="本知识库的长期复用方式。", confidence="medium"),
    node("method_wizard_of_oz", "Wizard-of-Oz Prototyping", "绿野仙踪原型", "Method", "由人隐藏控制机器人或智能表现来测试交互。", relevance="适合本科阶段快速验证 HRI 概念。", confidence="high"),
    node("method_participatory_design", "Participatory Design", "参与式设计", "Method", "让用户和利益相关者参与问题定义和方案生成。", confidence="high"),
    node("method_contextual_inquiry", "Contextual Inquiry", "情境访查", "Method", "在真实场景中观察并询问使用者。", confidence="high"),
    node("method_controlled_experiment", "Controlled Experiment", "控制实验", "Method", "操纵变量并测量因果影响。", confidence="high"),
    node("method_longitudinal_study", "Longitudinal Study", "长期研究", "Method", "研究长期使用、关系和采纳。", confidence="high"),
    node("method_research_through_design", "Research through Design", "通过设计进行研究", "Method", "通过原型、反思和注释作品集生成知识。", evidence=["S14", "S15"], confidence="high"),
    node("tech_ar_mr_interface", "AR/MR Interface", "AR/MR 机器人界面", "Technology", "用增强或混合现实显示机器人路径、状态和风险。", evidence=["S12", "S30"], relevance="把不可见计划转成可见线索。", confidence="high"),
    node("tech_llm_agent_layer", "LLM Agent Layer", "大模型代理中间层", "Technology", "在用户语言和机器人可执行动作之间进行解释、规划和澄清。", evidence=["S27", "S28", "S29"], confidence="medium"),
    node("tech_perception", "Perception", "机器人感知", "Technology", "通过传感器理解人、物体和环境。", confidence="medium"),
    node("tech_navigation", "Navigation", "定位与导航", "Technology", "机器人在空间中定位、规划路径并移动。", confidence="medium"),
    node("tech_motion_planning", "Motion Planning", "运动规划", "Technology", "生成安全、可执行并可理解的运动。", evidence=["S13"], confidence="high"),
    node("tech_intention_recognition", "Intention Recognition", "意图识别", "Technology", "推断人或机器人目标。", confidence="medium"),
    node("tech_haptic_feedback", "Haptic Feedback", "触觉反馈", "Technology", "通过力或震动反馈状态。", confidence="medium"),
    node("tech_speech_interface", "Speech Interface", "语音界面", "Technology", "支持语音命令、反馈和澄清。", confidence="medium"),
    node("tech_gesture_recognition", "Gesture Recognition", "手势识别", "Technology", "识别人类手势和指向。", confidence="medium"),
    node("modality_voice", "Voice Interaction", "语音交互", "Interaction Modality", "通过语音命令和对话互动。", confidence="medium"),
    node("modality_gesture", "Gesture Interaction", "手势交互", "Interaction Modality", "通过手势、身体动作或指向互动。", confidence="medium"),
    node("modality_gaze", "Gaze Interaction", "视线交互", "Interaction Modality", "通过视线和共同注意互动。", confidence="medium"),
    node("modality_haptic", "Haptic Interaction", "触觉交互", "Interaction Modality", "通过触觉反馈和接触互动。", confidence="medium"),
    node("modality_tangible", "Tangible Interaction", "实体交互", "Interaction Modality", "通过实体物件和空间布局互动。", evidence=["S16"], confidence="medium"),
    node("modality_visual_ar", "Visual AR Feedback", "AR 视觉反馈", "Interaction Modality", "用 AR 视觉元素展示状态、路径和风险。", evidence=["S12"], confidence="high"),
    node("robot_service", "Service Robot", "服务机器人", "Robot Type", "在服务场景为人或组织执行任务的机器人。", evidence=["S26"], scenarios=["酒店", "医院", "公共空间"], confidence="medium"),
    node("robot_social", "Social Robot", "社交机器人", "Robot Type", "以社会交互为关键功能的机器人。", evidence=["S02", "S03", "S32"], confidence="high"),
    node("robot_cobot", "Collaborative Robot", "协作机器人", "Robot Type", "与人共享工作空间协同工作的机器人。", evidence=["S10", "S11", "S22"], confidence="high"),
    node("robot_mobile_manipulator", "Mobile Manipulator", "移动操作机器人", "Robot Type", "结合移动底盘和机械臂的机器人。", evidence=["S27", "S29"], confidence="medium"),
    node("robot_telepresence", "Telepresence Robot", "远程临场机器人", "Robot Type", "支持远程在场和操作的机器人。", related=["concept_situation_awareness"], confidence="medium"),
    node("scenario_hotel_delivery", "Hotel Delivery", "酒店配送", "Scenario", "机器人在酒店中执行送物、通知和引导。", scenarios=["酒店"], confidence="medium"),
    node("scenario_hospital_guidance", "Hospital Guidance", "医院导诊", "Scenario", "机器人在医院中提供导航、排队和信息说明。", confidence="medium"),
    node("scenario_elderly_care", "Elderly Care", "养老陪护", "Scenario", "机器人支持提醒、陪伴和护理协作。", evidence=["S18"], confidence="medium"),
    node("scenario_industrial_assembly", "Industrial Assembly", "工业装配", "Scenario", "人与协作机器人共同完成装配。", evidence=["S11", "S22"], confidence="high"),
    node("scenario_public_cleaning", "Public Space Cleaning", "公共空间清洁", "Scenario", "机器人在人群共享空间执行清洁任务。", confidence="medium"),
    node("scenario_home_assistant", "Home Assistant", "家庭助理", "Scenario", "机器人在家庭环境完成提醒、清洁和轻服务。", evidence=["S27"], confidence="medium"),
    node("scenario_museum_guide", "Museum Guide", "博物馆导览", "Scenario", "机器人在展馆中讲解、引导和答疑。", confidence="medium"),
    node("scenario_rehab_training", "Rehabilitation Training", "康复训练", "Scenario", "机器人辅助患者进行身体训练。", confidence="medium"),
    node("scenario_remote_inspection", "Remote Inspection", "远程巡检", "Scenario", "操作者远程监督机器人巡检。", related=["concept_situation_awareness"], confidence="medium"),
    node("metric_usability", "Usability", "可用性", "Evaluation Metric", "衡量任务效率、效果和满意度。", confidence="high"),
    node("metric_trust", "Trust", "信任", "Evaluation Metric", "衡量用户对机器人能力和可靠性的依赖。", evidence=["S05", "S06"], confidence="high"),
    node("metric_workload", "Workload", "工作负荷", "Evaluation Metric", "衡量认知、身体和时间负荷。", evidence=["S19"], confidence="high"),
    node("metric_acceptance", "Acceptance", "接受度", "Evaluation Metric", "衡量用户采纳和使用意愿。", evidence=["S18"], confidence="high"),
    node("metric_safety", "Safety", "安全", "Evaluation Metric", "衡量物理和心理风险控制。", evidence=["S10", "S21", "S22"], confidence="high"),
    node("metric_situation_awareness", "Situation Awareness", "情境感知", "Evaluation Metric", "衡量用户对当前和未来状态的理解。", evidence=["S20"], confidence="high"),
    node("metric_social_presence", "Social Presence", "社会临场感", "Evaluation Metric", "衡量机器人被感知为社会参与者的程度。", evidence=["S04"], confidence="high"),
    node("metric_perceived_intelligence", "Perceived Intelligence", "感知智能", "Evaluation Metric", "衡量用户认为机器人聪明和有能力的程度。", evidence=["S04"], confidence="high"),
    node("metric_error_recovery", "Error Recovery", "错误恢复", "Evaluation Metric", "衡量失败后的解释、修复和恢复表现。", confidence="medium"),
    node("opportunity_ar_path_guidance", "AR Path and Intent Guidance", "AR 路径与意图可视化", "Design Opportunity", "通过 AR/MR 展示机器人路径、目标和风险区域。", evidence=["S12", "S13"], portfolio="适合做可视化原型和对比实验。", confidence="high"),
    node("opportunity_failure_recovery", "Service Robot Failure Recovery", "服务机器人失败恢复体验", "Design Opportunity", "设计机器人失败时的解释、补救和人工转接。", portfolio="适合服务设计作品集。", confidence="medium"),
    node("opportunity_llm_robot_mediator", "LLM-Robot Mediator", "LLM 机器人任务协商中间层", "Design Opportunity", "用 LLM 把自然语言需求转成可执行、可确认的机器人任务。", evidence=["S27", "S28", "S29"], confidence="medium"),
    node("opportunity_cobot_intent_ui", "Cobot Intent UI", "协作机器人意图界面", "Design Opportunity", "显示机械臂下一步动作、目标和安全区。", evidence=["S11", "S13"], confidence="high"),
    node("rq_trust_autonomy", "How does autonomy affect trust and control?", "自主性如何影响信任与控制感？", "Research Question", "研究不同自主性等级对信任、控制感和责任归属的影响。", evidence=["S07", "S09"], confidence="high"),
    node("rq_ar_intent", "Does AR improve robot intent understanding?", "AR 是否提升机器人意图理解？", "Research Question", "比较 AR 路径提示与传统状态提示的效果。", evidence=["S12", "S13"], confidence="high"),
    node("source_goodrich_schultz", "Goodrich and Schultz 2007", "Goodrich 与 Schultz 2007", "Paper / Source", "HRI survey source.", evidence=["S01"], confidence="high"),
    node("source_bartneck_godspeed", "Bartneck et al. 2009", "Bartneck 等 2009", "Paper / Source", "Godspeed measurement source.", evidence=["S04"], confidence="high"),
    node("source_lasota_safe_hri", "Lasota et al. 2017", "Lasota 等 2017", "Paper / Source", "Safe HRI survey source.", evidence=["S10"], confidence="high"),
    node("source_walker_vam_hri", "Walker et al. 2023", "Walker 等 2023", "Paper / Source", "VAM-HRI taxonomy source.", evidence=["S12"], confidence="high"),
]


def rel(source: str, relation_type: str, target: str, description: str, evidence: list[str] | None = None, design: str = "", confidence: str = "medium") -> dict:
    return {
        "source": source,
        "target": target,
        "relation_type": relation_type,
        "description": description,
        "evidence": evidence or [],
        "directionality": "directed",
        "confidence_level": confidence,
        "design_implication": design,
    }


RELATIONS = [
    rel("discipline_hri", "related_to", "discipline_hci", "HRI shares methods and theories with HCI.", ["S01", "S24"], "HCI 方法可迁移到机器人交互。", "high"),
    rel("discipline_hri", "related_to", "discipline_robotics", "HRI connects interaction research with robotics systems.", ["S01", "S23"], "设计需要理解机器人能力边界。", "high"),
    rel("discipline_hri", "related_to", "discipline_human_factors", "HRI uses human factors metrics and safety thinking.", ["S05", "S33"], "信任、负荷、安全需要量化。", "high"),
    rel("concept_intelligent_interaction_design", "extends", "discipline_hci", "Intelligent interaction design extends HCI toward AI-enabled systems.", [], "设计对象从界面扩展到智能行为。"),
    rel("concept_intelligent_interaction_design", "applied_to", "discipline_hri", "The design lens is applied to HRI problems.", [], "将 HRI 技术模块转译成体验问题。"),
    rel("concept_embodied_interaction", "derived_from", "theory_situated_action", "Embodied interaction is aligned with situated action.", ["S16", "S17"], "交互分析应包含现场行为。", "high"),
    rel("concept_affordance", "related_to", "concept_embodied_interaction", "Affordance explains action possibilities in embodied contexts.", ["S16"], "设计机器人任务可供性。"),
    rel("concept_robot_autonomy", "derived_from", "theory_levels_automation", "Robot autonomy can be analyzed through levels of automation.", ["S07", "S09"], "不要把自主性当成单一开关。", "high"),
    rel("concept_shared_autonomy", "is_part_of", "concept_robot_autonomy", "Shared autonomy is a mode within autonomy design.", ["S09"], "适合可调控制权。", "high"),
    rel("concept_shared_autonomy", "depends_on", "tech_intention_recognition", "Shared autonomy often needs inference of human goals.", [], "意图识别错误需要可恢复机制。"),
    rel("concept_shared_autonomy", "improves", "concept_human_agency", "When designed well, shared autonomy can preserve human agency.", [], "辅助强度需可调。"),
    rel("concept_robot_autonomy", "influences", "metric_trust", "Autonomy influences how users trust and rely on robots.", ["S05", "S09"], "需要信任校准而不是盲目信任。", "high"),
    rel("concept_robot_autonomy", "conflicts_with", "concept_human_agency", "High autonomy may reduce perceived human control.", ["S07"], "设计接管和确认。"),
    rel("concept_trust_calibration", "derived_from", "metric_trust", "Trust calibration refines the trust construct toward appropriate reliance.", ["S06"], "信任过高和过低都是风险。", "high"),
    rel("concept_transparency", "improves", "concept_trust_calibration", "Transparency can help users form calibrated trust.", ["S06"], "说明系统能力和限制。", "high"),
    rel("concept_explainability", "supports", "concept_transparency", "Explanations support transparency when task-relevant.", ["S06"], "解释应围绕用户决策。"),
    rel("concept_explainability", "influences", "metric_trust", "Explanations can influence perceived trust.", ["S06"], "需要避免过度解释。"),
    rel("concept_legible_motion", "related_to", "concept_predictability", "Legibility and predictability are related but distinct motion qualities.", ["S13"], "意图清晰不等同于轨迹常规。", "high"),
    rel("concept_legible_motion", "improves", "metric_safety", "Legible motion can improve perceived safety and coordination.", ["S13"], "让目标更易推断。"),
    rel("tech_motion_planning", "enables", "concept_legible_motion", "Motion planning can optimize for legibility.", ["S13"], "规划目标需包含人类推断。", "high"),
    rel("tech_ar_mr_interface", "enables", "modality_visual_ar", "AR/MR interfaces provide visual augmentation.", ["S12", "S30"], "可视化路径和安全区。", "high"),
    rel("tech_ar_mr_interface", "improves", "concept_situation_awareness", "AR can make robot state and plans visible.", ["S12"], "用于远程操作和协作工位。"),
    rel("tech_ar_mr_interface", "used_in", "scenario_industrial_assembly", "AR/MR can support collaborative workstations.", ["S11", "S12"], "显示安全区和下一步动作。"),
    rel("tech_ar_mr_interface", "used_in", "scenario_public_cleaning", "AR concepts can support public understanding of robot paths.", ["S12"], "公共演示可用移动 AR。"),
    rel("modality_visual_ar", "measured_by", "metric_situation_awareness", "AR feedback can be evaluated through situation awareness.", ["S20"], "评估用户是否理解未来路径。"),
    rel("tech_llm_agent_layer", "enables", "opportunity_llm_robot_mediator", "LLM layer enables natural-language task mediation.", ["S27", "S28", "S29"], "必须加入可执行性和安全确认。", "medium"),
    rel("tech_llm_agent_layer", "challenges", "concept_explainability", "LLM mediation introduces opacity and accountability issues.", ["S27"], "需要显示来源、计划和置信度。"),
    rel("tech_llm_agent_layer", "depends_on", "concept_affordance", "LLM robot plans must be grounded in robot affordances.", ["S27"], "把“能说”限制为“能做”。", "high"),
    rel("discipline_embodied_ai", "extends", "discipline_robotics", "Embodied AI extends robotics with foundation model reasoning.", ["S27", "S28", "S29"], "前沿方向但需要标注证据成熟度。"),
    rel("robot_service", "used_in", "scenario_hotel_delivery", "Service robots are used in hotel delivery.", [], "适合服务蓝图分析。"),
    rel("robot_service", "used_in", "scenario_hospital_guidance", "Service robots can guide patients in hospitals.", [], "需要低负荷和隐私保护。"),
    rel("robot_service", "used_in", "scenario_public_cleaning", "Service robots operate in public cleaning scenarios.", [], "需要社会规范和状态表达。"),
    rel("robot_social", "related_to", "concept_social_presence", "Social robots rely on social presence.", ["S02", "S03"], "设计社会线索要适度。", "high"),
    rel("robot_social", "related_to", "concept_anthropomorphism", "Social robots often trigger anthropomorphism.", ["S04"], "避免过度拟人。", "high"),
    rel("concept_anthropomorphism", "measured_by", "metric_social_presence", "Anthropomorphism relates to social perception measures.", ["S04"], "选择 Godspeed 维度时需说明原因。"),
    rel("metric_perceived_intelligence", "derived_from", "source_bartneck_godspeed", "Godspeed includes perceived intelligence.", ["S04"], "社交机器人可用此量表。", "high"),
    rel("metric_social_presence", "related_to", "source_bartneck_godspeed", "Godspeed supports social perception evaluation.", ["S04"], "可作为作品集评估工具。"),
    rel("robot_cobot", "requires", "metric_safety", "Cobots require safety evaluation.", ["S10", "S22"], "必须先考虑风险。", "high"),
    rel("robot_cobot", "used_in", "scenario_industrial_assembly", "Cobots are typical in industrial assembly.", ["S11"], "适合意图表达项目。", "high"),
    rel("scenario_industrial_assembly", "requires", "concept_legible_motion", "Collaborative assembly requires understandable robot motion.", ["S13"], "降低惊吓与误判。"),
    rel("scenario_industrial_assembly", "requires", "concept_role_allocation", "Human and robot roles must be clear in collaborative tasks.", ["S07", "S09"], "用任务矩阵定义责任。"),
    rel("scenario_hotel_delivery", "requires", "concept_failure_recovery", "Hotel service needs recovery when robots fail.", [], "服务失败是设计机会。"),
    rel("scenario_hotel_delivery", "evaluated_by", "metric_trust", "Hotel robot experience can be evaluated by trust.", ["S05"], "关注用户是否愿意再次使用。"),
    rel("scenario_elderly_care", "evaluated_by", "metric_acceptance", "Elderly care robots should be evaluated by acceptance.", ["S18"], "纳入社交和有用性变量。", "high"),
    rel("scenario_elderly_care", "requires", "concept_transparency", "Elderly care robots require transparency about data and limits.", [], "避免误导和隐私焦虑。"),
    rel("scenario_remote_inspection", "requires", "concept_situation_awareness", "Remote inspection depends on operator situation awareness.", ["S20"], "界面要整合空间、风险、未来动作。", "high"),
    rel("scenario_remote_inspection", "evaluated_by", "metric_workload", "Remote inspection can impose high workload.", ["S19"], "用 NASA-TLX 对比界面。"),
    rel("method_wizard_of_oz", "used_in", "robot_social", "Wizard-of-Oz is useful for social robot behavior prototyping.", [], "快速测试对话与表达。"),
    rel("method_wizard_of_oz", "used_in", "modality_voice", "Wizard-of-Oz can simulate speech intelligence.", [], "避免早期开发成本。"),
    rel("method_research_through_design", "derived_from", "theory_rtd", "RtD method follows RtD theory.", ["S14", "S15"], "作品集可作为研究产物。", "high"),
    rel("method_research_through_design", "supports", "opportunity_ar_path_guidance", "RtD can explore AR path guidance concepts.", ["S14", "S15"], "通过原型生成知识。"),
    rel("method_contextual_inquiry", "used_in", "scenario_hospital_guidance", "Contextual inquiry reveals hospital workflow constraints.", [], "先研究流程再设计机器人。"),
    rel("method_participatory_design", "used_in", "scenario_elderly_care", "Participatory design can involve older adults and caregivers.", ["S18"], "避免替用户想象需求。"),
    rel("method_controlled_experiment", "evaluated_by", "metric_workload", "Controlled experiments can measure workload differences.", ["S19"], "用于多模态对比。"),
    rel("method_longitudinal_study", "evaluated_by", "metric_acceptance", "Longitudinal studies reveal adoption over time.", ["S18"], "服务机器人不是一次性体验。"),
    rel("metric_workload", "measured_by", "source_goodrich_schultz", "HRI surveys emphasize task and interaction workload as issues.", ["S01"], "需结合 NASA-TLX 等工具。"),
    rel("metric_workload", "derived_from", "discipline_human_factors", "Workload is a human factors metric.", ["S19"], "评估认知负担。"),
    rel("metric_trust", "derived_from", "discipline_human_factors", "Trust is central in human factors automation research.", ["S05", "S06"], "用于自主系统评估。", "high"),
    rel("metric_situation_awareness", "derived_from", "discipline_human_factors", "Situation awareness is a human factors construct.", ["S20"], "适合动态系统。", "high"),
    rel("metric_safety", "derived_from", "source_lasota_safe_hri", "Safe HRI survey structures safety methods.", ["S10"], "设计要映射风险控制。", "high"),
    rel("source_lasota_safe_hri", "related_to", "metric_safety", "Lasota et al. survey safety methods.", ["S10"], "作为安全模块核心参考。", "high"),
    rel("source_walker_vam_hri", "related_to", "tech_ar_mr_interface", "Walker et al. propose VAM-HRI taxonomy.", ["S12"], "作为 AR/MR 模块核心参考。", "high"),
    rel("source_goodrich_schultz", "related_to", "discipline_hri", "Goodrich and Schultz provide HRI survey.", ["S01"], "作为主报告背景引用。", "high"),
    rel("opportunity_ar_path_guidance", "derived_from", "tech_ar_mr_interface", "AR path guidance derives from VAM-HRI interface concepts.", ["S12"], "视觉化不可见计划。"),
    rel("opportunity_ar_path_guidance", "evaluated_by", "metric_situation_awareness", "AR path guidance should be evaluated by situation awareness.", ["S20"], "测量理解而非只看美观。"),
    rel("opportunity_ar_path_guidance", "evaluated_by", "metric_workload", "AR may reduce or increase workload.", ["S19"], "比较遮挡和负荷。"),
    rel("opportunity_failure_recovery", "derived_from", "concept_failure_recovery", "Service recovery opportunity derives from failure recovery.", [], "设计失败解释和人工转接。"),
    rel("opportunity_failure_recovery", "evaluated_by", "metric_error_recovery", "Failure recovery design should be evaluated by recovery metrics.", [], "记录恢复时间和满意度。"),
    rel("opportunity_failure_recovery", "evaluated_by", "metric_trust", "Failure recovery affects trust.", ["S05", "S06"], "失败后信任变化很关键。"),
    rel("opportunity_llm_robot_mediator", "depends_on", "tech_llm_agent_layer", "The mediator opportunity depends on LLM agent layer.", ["S27", "S28"], "任务要经过可执行性检查。"),
    rel("opportunity_llm_robot_mediator", "requires", "concept_transparency", "LLM robot mediator requires transparent plan and limits.", [], "显示为何不能执行。"),
    rel("opportunity_cobot_intent_ui", "derived_from", "concept_legible_motion", "Cobot intent UI derives from legibility concerns.", ["S13"], "把目标和下一步动作可视化。"),
    rel("opportunity_cobot_intent_ui", "requires", "metric_safety", "Cobot intent UI must respect safety constraints.", ["S10", "S22"], "设计不能鼓励危险靠近。"),
    rel("rq_trust_autonomy", "derived_from", "concept_robot_autonomy", "Research question follows autonomy-trust relationship.", ["S05", "S09"], "适合实验研究。"),
    rel("rq_ar_intent", "derived_from", "opportunity_ar_path_guidance", "Research question follows AR path guidance opportunity.", ["S12", "S13"], "适合 poster。"),
    rel("concept_graph_rag", "extends", "concept_intelligent_interaction_design", "GraphRAG extends design knowledge reuse with graph structure.", [], "让 LLM 根据关系生成机会。"),
    rel("concept_graph_rag", "supports", "opportunity_ar_path_guidance", "GraphRAG can retrieve related concepts and sources for AR opportunities.", [], "提升机会生成可追溯性。"),
    rel("concept_graph_rag", "supports", "rq_trust_autonomy", "GraphRAG can generate research questions from autonomy and trust relations.", [], "辅助论文选题。"),
    rel("theory_situated_action", "applied_to", "scenario_hotel_delivery", "Situated action frames service workflows as adaptive rather than fixed scripts.", ["S17"], "机器人要处理现场变化。"),
    rel("concept_embodied_interaction", "applied_to", "robot_cobot", "Embodied interaction applies to physical collaboration with cobots.", ["S16"], "动作和空间本身是界面。"),
    rel("concept_multimodal_feedback", "improves", "metric_situation_awareness", "Multimodal feedback can improve awareness if well integrated.", ["S08", "S20"], "避免信息过载。"),
    rel("modality_voice", "used_in", "scenario_home_assistant", "Voice is common in home assistant scenarios.", ["S27"], "必须处理澄清和隐私。"),
    rel("modality_gesture", "used_in", "scenario_industrial_assembly", "Gesture can support spatial instructions in assembly.", [], "嘈杂场景中补充语音。"),
    rel("modality_haptic", "used_in", "scenario_remote_inspection", "Haptic feedback can support remote inspection and teleoperation.", [], "提示接触和风险。"),
    rel("modality_tangible", "supports", "concept_affordance", "Tangible interfaces materialize affordances.", ["S16"], "让任务边界可触摸。"),
    rel("tech_perception", "depends_on", "tech_intention_recognition", "Intention recognition depends on perception data.", [], "识别错误应可解释。"),
    rel("tech_navigation", "influences", "metric_safety", "Navigation behavior influences safety and comfort.", ["S10"], "路径和速度是交互变量。"),
    rel("tech_navigation", "requires", "concept_transparency", "Users need to understand navigation decisions in shared spaces.", [], "显示绕路和等待原因。"),
    rel("tech_perception", "challenges", "concept_transparency", "Perception uncertainty is hard for users to see.", [], "需要状态和置信度表达。"),
    rel("scenario_museum_guide", "requires", "modality_gaze", "Museum guidance can use gaze cues for joint attention.", ["S03"], "帮助游客跟随讲解。"),
    rel("scenario_rehab_training", "requires", "modality_haptic", "Rehabilitation training benefits from haptic/physical feedback.", [], "反馈需舒适和安全。"),
    rel("scenario_home_assistant", "requires", "concept_human_agency", "Home assistants need user agency and privacy controls.", [], "家庭场景要可拒绝和可关闭。"),
]


def write_text(path: str, content: str) -> None:
    target = BASE / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def write_csv(path: str, headers: list[str], rows: list[list[str]]) -> None:
    target = BASE / path
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def write_json(path: str, data: object) -> None:
    target = BASE / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sources_markdown() -> str:
    rows = []
    for s in SOURCES:
        rows.append(
            f"### {s['id']} {s['title']}\n"
            f"- 作者/机构：{s['authors']}\n"
            f"- 年份：{s['year']}\n"
            f"- 出处：{s['venue']}\n"
            f"- 类型：{s['type']}\n"
            f"- 链接：[{s['url']}]({s['url']})\n"
            f"- 用途：{s['note']}\n"
        )
    return "\n".join(rows)


def ontology_markdown() -> str:
    blocks = []
    for item in ONTOLOGY:
        blocks.append(
            f"## {item['name']}\n"
            f"- 定义：{item['definition']}\n"
            f"- 关键子类：{item['subclasses']}\n"
            f"- 与其他本体的关系：{item['relations']}\n"
            f"- 对设计研究的意义：{item['design']}\n"
            f"- 典型研究问题：{item['questions']}\n"
            f"- 典型应用场景：{item['scenarios']}\n"
            f"- 可延伸作品集方向：{item['portfolio']}\n"
        )
    return "\n".join(blocks)


def themes_markdown() -> str:
    blocks = []
    for name, definition, concepts, disciplines, questions, methods, relevance, scenarios, nodes, refs, portfolio, rq, prototype in THEMES:
        ref_links = ", ".join(source_link(r.strip()) for r in refs.split(";") if r.strip() in SOURCE_BY_ID)
        blocks.append(
            f"# {name}\n"
            f"## Definition\n{definition}\n"
            f"## Key Concepts\n{concepts}\n"
            f"## Related Disciplines\n{disciplines}\n"
            f"## Important Questions\n{questions}\n"
            f"## Typical Methods\n{methods}\n"
            f"## Design Relevance\n{relevance}\n"
            f"## Application Scenarios\n{scenarios}\n"
            f"## Related Knowledge Graph Nodes\n{nodes}\n"
            f"## Important References\n{ref_links if ref_links else refs}\n"
            f"## Possible Portfolio Directions\n{portfolio}\n"
            f"## Possible Research Questions\n{rq}\n"
            f"## Possible Prototype Directions\n{prototype}\n"
            f"## Data Representation\n可作为 `Concept`、`Scenario`、`Method`、`Evaluation Metric` 和 `Design Opportunity` 节点组合进入 GraphRAG。\n"
        )
    return "\n\n---\n\n".join(blocks)


def relation_examples_markdown() -> str:
    blocks = []
    for rel_type, zh, usage, example in RELATION_TYPE_ROWS:
        generated = [r for r in RELATIONS if r["relation_type"] == rel_type][:3]
        examples = [example]
        for r in generated:
            examples.append(f"{r['source']} -- {r['relation_type']} --> {r['target']}")
        while len(examples) < 3:
            examples.append(example)
        blocks.append(
            f"## {rel_type}\n"
            f"- 中文解释：{zh}\n"
            f"- 使用场景：{usage}\n"
            f"- 示例三元组：\n"
            + "\n".join(f"  - {e}" for e in examples[:3])
        )
    return "\n\n".join(blocks)


def tree_markdown() -> str:
    lines = ["# 文字版知识图谱总树", ""]
    for item in ONTOLOGY:
        lines.append(f"- {item['name']}")
        for sub in item["subclasses"].split(", "):
            lines.append(f"  - {sub}")
    return "\n".join(lines)


def triples() -> list[str]:
    label = {n["id"]: n["label"] for n in NODES}
    items = [f"{label.get(r['source'], r['source'])} -- {r['relation_type']} --> {label.get(r['target'], r['target'])}" for r in RELATIONS]
    extra = [
        "Robot Transparency -- improves --> Trust Calibration",
        "AR Interface -- enables --> Spatial Robot Guidance",
        "Failure Recovery -- supports --> Service Experience",
        "Multimodal Feedback -- improves --> Situation Awareness",
        "Robot Autonomy -- influences --> Human Trust",
        "Shared Autonomy -- requires --> Intention Recognition",
        "Legible Motion -- supports --> Human-Robot Collaboration",
        "Predictable Motion -- improves --> Perceived Safety",
        "Wizard-of-Oz -- used_in --> Social Robot Prototyping",
        "Research through Design -- supports --> Portfolio Translation",
        "Service Blueprint -- supports --> Service Robot Experience Design",
        "NASA-TLX -- measured_by --> Workload",
        "Godspeed Questionnaire -- measured_by --> Anthropomorphism",
        "Almere Model -- measured_by --> Acceptance",
        "Situation Awareness -- measured_by --> SAGAT",
        "ISO/TS 15066 -- constrains --> Collaborative Robot Workspace",
        "ISO 10218-1 -- constrains --> Industrial Robot Design",
        "LLM Agent -- challenges --> Accountability",
        "VLA Model -- extends --> Embodied AI",
        "SayCan -- depends_on --> Robotic Affordances",
        "PaLM-E -- extends --> Embodied Multimodal Reasoning",
        "RT-2 -- extends --> Vision-Language-Action Models",
        "Robotiquette -- supports --> Public Space Comfort",
        "Robot Personality -- influences --> Social Presence",
        "Anthropomorphism -- conflicts_with --> Accountability Clarity",
        "Transparency -- mediates --> Autonomy and Trust",
        "Gaze Cue -- supports --> Joint Attention",
        "Haptic Feedback -- improves --> Remote Operation Feedback",
        "Tangible UI -- supports --> Task Planning",
        "Contextual Inquiry -- used_in --> Hospital Workflow Research",
        "Participatory Design -- designed_for --> Vulnerable User Groups",
        "Controlled Experiment -- evaluated_by --> Trust and Workload Metrics",
        "Longitudinal Study -- measured_by --> Long-Term Adoption",
        "Case Study -- used_in --> Service Robot Research",
        "Taxonomy Building -- supports --> Ontology Construction",
        "Knowledge Graph -- supports --> Research Question Generation",
        "Knowledge Graph -- supports --> Design Opportunity Discovery",
        "GraphRAG -- enables --> Evidence-Aware Design Ideation",
        "Node Schema -- constrains --> Knowledge Graph Data",
        "Relation Schema -- constrains --> Knowledge Graph Data",
        "Design Opportunity Card -- derived_from --> Knowledge Graph Path",
        "Conference Poster -- derived_from --> Research Question",
        "Portfolio Case Study -- derived_from --> Design Opportunity",
        "Robot Navigation -- influences --> User Comfort",
        "Motion Planning -- influences --> Legibility",
        "Scene Understanding -- supports --> Failure Recovery",
        "Human Intervention -- supports --> Safety",
        "Robot State Feedback -- improves --> Status Visibility",
        "Explainable Interface -- supports --> Human Agency",
        "Voice Interaction -- challenges --> Ambiguity",
        "Gesture Interaction -- supports --> Spatial Reference",
        "AR Safety Zone -- improves --> Perceived Safety",
        "Service Robot -- requires --> Service Blueprint",
        "Hospital Robot -- requires --> Privacy Protection",
        "Elderly Care Robot -- requires --> Consent Mechanism",
        "Public Cleaning Robot -- requires --> Social Norm Awareness",
        "Collaborative Assembly -- requires --> Role Allocation",
        "Remote Inspection -- requires --> Situation Awareness",
        "Rehabilitation Robot -- requires --> Comfort",
        "Museum Guide Robot -- requires --> Engagement",
        "Home Robot -- requires --> Human Agency",
        "LLM-Robot Mediator -- requires --> Grounding Check",
        "Trust Calibration -- measured_by --> Trust Questionnaire",
        "Error Recovery -- measured_by --> Recovery Time",
        "Legibility -- measured_by --> Goal Inference Accuracy",
        "Workload -- measured_by --> NASA-TLX",
        "Acceptance -- measured_by --> Almere Model",
        "Safety -- measured_by --> Near-Miss Events",
        "Usability -- measured_by --> Task Success Rate",
        "Social Presence -- measured_by --> Social Presence Scale",
        "Perceived Intelligence -- measured_by --> Godspeed Questionnaire",
    ]
    items.extend(extra)
    # De-duplicate while preserving order.
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique[:130]


def node_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "HRI Knowledge Graph Node",
        "type": "object",
        "required": [
            "id", "label", "zh_label", "type", "definition", "parent", "children",
            "related_nodes", "evidence", "design_relevance", "application_scenarios",
            "research_questions", "portfolio_potential", "confidence_level",
        ],
        "properties": {
            "id": {"type": "string"},
            "label": {"type": "string"},
            "zh_label": {"type": "string"},
            "type": {"enum": [row[0] for row in NODE_TYPE_ROWS]},
            "definition": {"type": "string"},
            "parent": {"type": "string"},
            "children": {"type": "array", "items": {"type": "string"}},
            "related_nodes": {"type": "array", "items": {"type": "string"}},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "design_relevance": {"type": "string"},
            "application_scenarios": {"type": "array", "items": {"type": "string"}},
            "research_questions": {"type": "array", "items": {"type": "string"}},
            "portfolio_potential": {"type": "string"},
            "confidence_level": {"enum": ["low", "medium", "high"]},
        },
    }


def relation_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "HRI Knowledge Graph Relation",
        "type": "object",
        "required": ["source", "target", "relation_type", "description", "evidence", "directionality", "confidence_level", "design_implication"],
        "properties": {
            "source": {"type": "string"},
            "target": {"type": "string"},
            "relation_type": {"enum": [row[0] for row in RELATION_TYPE_ROWS]},
            "description": {"type": "string"},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "directionality": {"enum": ["directed", "bidirectional"]},
            "confidence_level": {"enum": ["low", "medium", "high"]},
            "design_implication": {"type": "string"},
        },
    }


def knowledge_graph_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "HRI Knowledge Graph",
        "type": "object",
        "required": ["metadata", "node_types", "relation_types", "nodes", "relations", "sources"],
        "properties": {
            "metadata": {"type": "object"},
            "node_types": {"type": "array"},
            "relation_types": {"type": "array"},
            "nodes": {"type": "array", "items": node_schema()},
            "relations": {"type": "array", "items": relation_schema()},
            "sources": {"type": "array"},
        },
    }


def kg_sample() -> dict:
    return {
        "metadata": {
            "title": "Intelligent Interaction Design x Robotics HRI Knowledge Graph Sample",
            "language": "zh-CN with English terms",
            "created": "2026-06-19",
            "scope": "HRI-oriented design research, knowledge graph reuse, portfolio ideation",
            "note": "Seed graph, not exhaustive. Evidence links point to literature/source registry.",
        },
        "node_types": [row[0] for row in NODE_TYPE_ROWS],
        "relation_types": [row[0] for row in RELATION_TYPE_ROWS],
        "nodes": NODES,
        "relations": RELATIONS,
        "sources": SOURCES,
    }


def main_report() -> str:
    return f"""
    # 智能交互设计 × 机器人：面向 HRI 设计研究的知识图谱框架

    ## 摘要

    [Fact] Human-Robot Interaction / 人机机器人交互已经形成跨 robotics、HCI、human factors、AI、工程与社会行为科学的研究共同体，ACM/IEEE HRI 官方说明也强调其跨学科属性 {source_link('S23')}。机器人正在进入制造、服务、医疗、家庭和公共空间，IFR World Robotics 报告提供了全球机器人市场统计入口 {source_link('S26')}。

    [Explanation] 对智能交互设计而言，机器人不是“带屏幕的产品”，而是会移动、感知、决策、失败并影响人类安全与责任感的具身系统。本研究把 HRI 视为设计研究、机器人系统、人因评估与知识图谱建模的交叉领域。

    [Inference] 如果把机器人技术模块转换为可查询的知识节点和关系，设计师就可以从“感知、导航、自主性、解释、反馈、场景、评估指标”之间发现设计机会，而不是只做形式或 UI 包装。

    [Design Implication] 本文档包建立一个中文研究报告、知识图谱 ontology、节点/关系 schema、表格数据、三元组、JSON 示例和作品集/Poster 转化模板，用于后续 RAG / GraphRAG、作品集项目和论文选题生成。

    ## 关键词

    Human-Robot Interaction / 人机机器人交互；Intelligent Interaction Design / 智能交互设计；Embodied AI / 具身智能；Embodied Interaction / 具身交互；Social Robotics / 社交机器人；Collaborative Robots / 协作机器人；AR/MR Interfaces / 增强与混合现实界面；Trust Calibration / 信任校准；Research through Design / 通过设计进行研究；Knowledge Graph / 知识图谱。

    ## 研究背景

    [Fact] HRI 经典综述 Goodrich & Schultz 将该领域组织为人与机器人之间感知、行动、任务、角色和系统评估的综合问题 {source_link('S01')}。社会机器人综述则强调，当社会互动本身成为机器人功能的一部分时，设计者需要考虑表达、人格、社会规范和长期影响 {source_link('S02')}。

    [Explanation] 智能交互设计介入机器人时，核心不是“让机器人更像人”，而是让人的意图、机器人能力、场景约束和风险边界能够互相理解。服务机器人需要服务蓝图；协作机器人需要安全和可读运动；社交机器人需要拟人化边界；LLM 机器人需要 grounding、解释和责任链。

    [Fact] 信任是 HRI 的核心评价变量之一。Hancock 等人的元分析把人、机器人和环境因素纳入 HRI 信任研究 {source_link('S05')}；Lee & See 则从自动化角度强调“适当依赖”而非单纯提高信任 {source_link('S06')}。

    [Design Implication] 因此，本课题以“设计研究型知识操作系统”为目标：让概念能被查询，关系能被追溯，机会能被推导，评估能被设计进项目。

    ## 核心研究问题

    1. 智能交互设计如何介入机器人系统，而不是停留在视觉或外观层？
    2. HRI 中哪些理论、方法和评估指标最值得设计学生优先掌握？
    3. 感知、导航、规划、自主性、失败恢复等机器人模块如何转化为交互设计问题？
    4. 如何建立一个能被 LLM/RAG/GraphRAG 复用的 HRI 知识图谱？
    5. AR/MR、多模态反馈和可解释界面如何改善机器人意图理解与情境感知？
    6. 机器人自主性如何影响信任、控制感、责任归属和安全体验？
    7. 如何从图谱路径中生成作品集项目、conference poster 和论文雏形？

    ## 研究目标

    - 建立一个面向 HRI 设计研究的领域知识框架。
    - 建立顶层 ontology、节点类型、关系类型和机器可读 JSON schema。
    - 建立方法与评估指标系统，支撑后续实验和作品集叙事。
    - 建立设计机会库和研究问题库。
    - 建立可进入 RAG / GraphRAG 的来源、三元组和样例知识图谱。

    ## 研究范围与边界

    ### 纳入内容

    HRI、HCI、机器人交互、服务机器人、社交机器人、协作机器人、多模态交互、AR/MR 机器人界面、机器人自主性、共享自主性、远程操作、信任与可解释性、设计研究方法、HRI 评估方法、AI agent/LLM 与机器人中间层。

    ### 排除内容

    过于底层的控制算法推导、与交互体验无关的机械结构细节、纯 AI 模型训练细节、与人机交互无关的工业自动化流程、未能转化为人类理解/控制/安全/体验问题的技术细节。

    ## 方法

    本研究采用文献综述、关键词检索、主题编码、本体构建、知识图谱建模、设计机会推导和作品集转化。外部来源包括 ACM/IEEE HRI、CHI、ACM THRI、Human Factors、International Journal of Social Robotics、IEEE/ISO/IFR 官方资料和 arXiv/PMLR 中与 LLM robotics 相关的前沿文献；所有已使用来源见 `appendix/来源与检索记录.md`。

    ## 核心本体框架

    本图谱采用 10 个一级本体：Human、Robot、Interaction、Intelligence、Embodiment、Interface、Context、Task、Evaluation、Ethics & Society。它们共同形成一个从人类行动者到机器人系统、从场景任务到评估伦理的设计研究闭环。

    {ontology_markdown()}

    ## 关键知识判断

    ### 判断 1：机器人交互不是普通界面交互的延伸，而是具身行动系统的协作问题

    [Fact] Dourish 的 embodied interaction 强调行动和情境在交互中的基础地位 {source_link('S16')}；Suchman 的 situated action 批评把行动理解为计划的直接执行 {source_link('S17')}。

    [Inference] 机器人在真实空间中行动，因此设计对象不只是屏幕，而包括路径、速度、姿态、距离、接触、失败和接管。

    [Design Implication] 作品集应展示“机器人系统模块 × 用户理解 × 场景流程 × 评估指标”的映射，而不是只展示一个 app 界面。

    ### 判断 2：自主性需要被设计为可协商的角色分配

    [Fact] Parasuraman 等提出自动化可以分布在信息获取、分析、决策和行动等不同功能中 {source_link('S07')}；Beer 等进一步面向 HRI 讨论机器人自主性等级 {source_link('S09')}。

    [Explanation] 自主性不是越高越好。它会改变人类控制感、责任归属和信任校准。

    [Design Implication] 设计机会包括可调自主性面板、接管机制、任务确认、计划预览和失败转人工。

    ### 判断 3：信任设计的目标是校准，而不是“让用户更相信机器人”

    [Fact] HRI 信任元分析说明信任受机器人、人和环境因素共同影响 {source_link('S05')}；自动化信任研究强调 appropriate reliance / 适当依赖 {source_link('S06')}。

    [Inference] 机器人如果表现得过于自信，可能制造过度信任；如果状态不透明，又可能导致用户拒绝使用。

    [Design Implication] 关键设计变量是透明性、解释粒度、置信度表达、失败恢复和用户接管。

    ### 判断 4：AR/MR 是机器人意图可视化的重要界面层

    [Fact] Walker 等对 VAM-HRI 建立了虚拟设计元素分类 {source_link('S12')}；Milgram 与 Kishino 的 mixed reality taxonomy 是 MR 研究基础 {source_link('S30')}。

    [Inference] AR/MR 的设计价值不是炫技，而是把机器人不可见的路径、目标、安全区和不确定性变成可理解线索。

    [Design Implication] 可发展为 AR 路径提示、安全区可视化、远程操作状态叠加、协作机械臂动作预览。

    ### 判断 5：LLM agent 能扩展机器人交互，但必须被 grounding、安全和责任链约束

    [Fact] SayCan 把语言模型建议与机器人可供性/value functions 结合 {source_link('S27')}；PaLM-E 和 RT-2 代表了具身多模态和 VLA 方向 {source_link('S28')} {source_link('S29')}。

    [Inference] LLM 可以成为“任务协商中间层”，但语言能力不等于物理可执行能力。

    [Design Implication] 需要设计可执行性检查、计划预览、用户确认、风险提示、失败解释和日志追溯。

    ## 设计转化框架

    `文献证据 -> 概念节点 -> 关系路径 -> 场景约束 -> 设计问题 -> 原型方向 -> 评估指标 -> 作品集/论文输出`

    示例路径：

    `Robot Autonomy -> influences -> Trust -> measured_by -> Trust Questionnaire -> applied_to -> Hotel Delivery Robot -> derived_from -> Failure Recovery Design`

    这条路径可以生成一个作品集项目：酒店配送机器人失败恢复体验系统；也可以生成研究问题：失败解释粒度是否影响用户再次使用意愿？

    ## 局限

    - 本文档包是 seed repository，不是系统综述最终稿。
    - LLM robotics 相关来源中部分为 preprint 或快速发展方向，已在来源表中标注。
    - 具体 DOI、引用量和量表适用性在投稿前仍需二次核验。
    - 机器人标准主要覆盖工业/协作机器人，不能直接替代医疗、家庭或公共服务机器人的伦理与安全审查。

    ## 结论

    这个知识图谱的核心贡献，是把“智能交互设计 × 机器人”从资料汇总转化为可查询、可扩展、可复用、可设计转化的研究系统。它能帮助设计学生建立 HRI 系统理解，把机器人技术模块转译为交互问题，并把研究证据连接到作品集、poster、论文和个人 AI 研究助手。
    """


def kg_framework_doc() -> str:
    return f"""
    # 知识图谱框架说明

    ## 目标

    本知识图谱用于连接 HRI / Robotics / HCI / Design Research 中的概念、方法、技术、场景、评价指标和设计机会。它不是普通思维导图，而是可被 LLM、RAG 和 GraphRAG 调用的结构化知识系统。

    ## 顶层本体

    {ontology_markdown()}

    ## 节点类型

    | 节点类型 | 中文 | 定义 | 用途 |
    |---|---|---|---|
    """ + "\n".join(f"| {r[0]} | {r[1]} | {r[2]} | {r[5]} |" for r in NODE_TYPE_ROWS) + f"""

    ## 关系类型

    | 关系 | 中文解释 | 使用场景 | 示例 |
    |---|---|---|---|
    """ + "\n".join(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |" for r in RELATION_TYPE_ROWS) + f"""

    ## 应用场景

    - 中文研究报告：按 ontology 和主题模块组织章节。
    - 作品集项目：从 `Design Opportunity` 节点出发，追溯 `Concept`、`Scenario`、`Metric` 和 `Paper / Source`。
    - Poster / 论文：从 `Research Question` 节点出发，匹配方法、数据和评估指标。
    - LLM 复用：把 Markdown 分块进入 RAG，把 JSON nodes/relations 进入 GraphRAG。

    ## 证据策略

    每个重要节点优先连接文献或官方来源。示例：HRI 总览连接 Goodrich & Schultz {source_link('S01')} 和 HRI 官方会议说明 {source_link('S23')}；AR/MR 模块连接 VAM-HRI survey {source_link('S12')}；安全模块连接 safe HRI survey {source_link('S10')} 与 ISO 标准 {source_link('S21')} {source_link('S22')}。
    """


def robot_system_doc() -> str:
    modules = [
        ("感知 Perception", "感知决定机器人知道什么，也决定用户需要看到哪些不确定性。设计问题：当机器人没有看见人、识别错物体或置信度低时，应如何表达？"),
        ("定位与导航 Localization and Navigation", "导航不仅是路径规划，也是公共空间中的社会行为。设计问题：路径、等待、绕行和让路如何被人理解？"),
        ("环境理解 Scene Understanding", "环境理解影响机器人对障碍物、人群、物体和区域的判断。设计问题：系统是否需要展示环境地图和识别边界？"),
        ("意图识别 Intention Recognition", "意图识别支持主动帮助和共享自主，但误判会损害控制感。设计问题：机器人何时应询问而不是猜测？"),
        ("决策 Planning and Decision-Making", "决策模块决定下一步做什么。设计问题：人是否能看到计划、理由和替代选项？"),
        ("动作执行 Actuation", "执行层让算法变成物理动作。设计问题：速度、力度、距离和停止方式如何传递安全感？"),
        ("运动规划 Motion Planning", f"运动规划可服务于可读性与可预测性，Dragan 等区分了 legibility 和 predictability {source_link('S13')}。设计问题：机器人动作是否让目标可推断？"),
        ("人体安全 Human Safety", f"安全是机器人设计底线，safe HRI 综述和 ISO 标准可作为入口 {source_link('S10')} {source_link('S21')} {source_link('S22')}。设计问题：风险如何被用户看见？"),
        ("反馈 Feedback", "反馈包括声音、灯光、屏幕、触觉、动作和 AR。设计问题：反馈是否及时、低负荷且不打扰？"),
        ("表达 Expression", "表达影响社会临场感、人格和情绪理解。设计问题：表达是否超出机器人真实能力？"),
        ("失败恢复 Failure Recovery", "失败恢复决定服务体验韧性。设计问题：机器人如何解释、道歉、请求帮助或转人工？"),
        ("可解释性 Explainability", "解释应服务用户决策，而不是展示所有系统细节。设计问题：解释粒度如何匹配风险和用户角色？"),
        ("自主性 Autonomy", "自主性改变控制权、责任和信任。设计问题：哪些步骤自动化，哪些步骤保留人类确认？"),
        ("人类介入 Human Intervention", "人类介入是安全、责任和服务连续性的关键机制。设计问题：接管入口是否清晰且不迟到？"),
        ("多机器人系统 Multi-Robot Systems", "多机器人系统引入群体行为、调度和可理解性问题。设计问题：用户如何理解多个机器人的优先级和路径？"),
    ]
    return "# 机器人系统视角\n\n" + "\n\n".join(f"## {name}\n{text}" for name, text in modules)


def interaction_design_doc() -> str:
    modules = [
        ("用户研究", "识别不同用户的能力、心理模型、风险感知和接受条件。连接机器人系统：用户研究决定状态反馈、控制权和解释粒度。"),
        ("场景分析", "分析空间、流程、社会规范和组织约束。连接机器人系统：导航、安全区和任务调度必须适配场景。"),
        ("任务流", "拆解目标、步骤、交接、失败点和责任。连接机器人系统：规划、执行和恢复都应映射到任务流。"),
        ("人机角色分配", "决定人、机器人和 AI agent 各自负责什么。连接机器人系统：自主性等级和接管机制。"),
        ("信息架构", "组织状态、任务、解释和控制信息。连接机器人系统：把感知、规划和错误状态转为可理解界面。"),
        ("多模态输入", "语音、手势、触摸、实体控制等。连接机器人系统：输入需要意图识别和确认。"),
        ("多模态反馈", "视觉、听觉、触觉、动作、AR/MR。连接机器人系统：反馈来源于状态、规划和传感。"),
        ("状态可见性", "让用户知道机器人当前状态和下一步。连接机器人系统：感知、计划、执行状态需要可视化。"),
        ("意图表达", "通过路径、姿态、灯光、声音或 AR 表达目标。连接机器人系统：运动规划和任务规划要考虑人类推断。"),
        ("可解释界面", "展示理由、置信度、限制和替代方案。连接机器人系统：决策模块和 LLM agent 的输出需要解释层。"),
        ("错误恢复", "提供失败解释、补救选项和人工转接。连接机器人系统：失败检测、诊断和回滚策略。"),
        ("信任建立", "通过可靠表现、透明边界和一致行为建立适当信任。连接机器人系统：自主性、感知可靠性和反馈一致性。"),
        ("长期使用体验", "关注习惯、维护、情感依赖和持续价值。连接机器人系统：日志、个性化、隐私和更新策略。"),
        ("情感与社会性设计", "控制人格、语气、表情和礼仪。连接机器人系统：表达模块和行为策略。"),
        ("服务蓝图", "连接用户触点、后台流程和机器人任务。连接机器人系统：调度、人类介入和服务失败恢复。"),
        ("原型设计", "用 WoZ、视频原型、AR mockup、硬件原型模拟交互。连接机器人系统：先验证交互假设，再投入工程实现。"),
        ("可用性测试", "验证任务是否能被理解和完成。连接机器人系统：测试界面、控制和反馈。"),
        ("HRI 实验设计", "设置变量、指标和任务场景。连接机器人系统：自主等级、反馈模态、解释粒度等可作为自变量。"),
        ("Research through Design", f"通过设计产物和反思生成知识 {source_link('S14')} {source_link('S15')}。连接机器人系统：原型成为研究假设的物化形式。"),
    ]
    return "# 交互设计视角\n\n" + "\n\n".join(f"## {name}\n{text}" for name, text in modules)


def methods_metrics_doc() -> str:
    methods_table = "\n".join(f"| {m[1]} | {m[0]} | {m[2]} | {m[3]} | {m[4]} | {m[5]} | {m[6]} |" for m in METHODS)
    metrics_table = "\n".join(f"| {m[1]} | {m[0]} | {m[2]} | {m[3]} | {m[4]} | {m[5]} |" for m in METRICS)
    return f"""
    # 研究方法与评估指标

    ## 方法表

    | 方法名称 | 英文名称 | 定义 | 适用阶段 | 优点 | 局限 | 适合项目 |
    |---|---|---|---|---|---|---|
    {methods_table}

    ## 指标表

    | 指标名称 | 英文名称 | 定义 | 测量方式 | 适用场景 | 相关设计问题 |
    |---|---|---|---|---|---|
    {metrics_table}

    ## 选型建议

    - 如果项目是早期概念：优先使用 contextual inquiry、Wizard-of-Oz、prototype testing。
    - 如果项目要做 poster：选择一个清晰自变量，例如解释粒度、AR 提示、有无触觉反馈，再配 2-3 个指标。
    - 如果项目要做作品集：组合 `用户研究 -> 图谱推导 -> 原型 -> 轻量评估`。
    - 如果项目要做论文：补充系统检索、明确假设、控制实验或长期研究。
    """


def design_opportunities_doc() -> str:
    rows = "\n".join(f"| {o[0]} | {o[1]} | {o[2]} | {o[3]} | {o[4]} | {o[5]} | {o[6]} | {o[7]} |" for o in OPPORTUNITIES)
    return f"""
    # 设计机会与作品集方向

    | 方向标题 | 目标用户 | 场景 | 核心问题 | 相关知识节点 | 原型形式 | 评估方法 | 作品集价值 |
    |---|---|---|---|---|---|---|---|
    {rows}

    ## 作品集叙事建议

    1. 用图谱路径开场：说明你不是凭空想概念，而是从文献、场景和评估指标推导机会。
    2. 展示机器人系统视角：把感知、导航、规划、自主性、失败恢复转译为体验问题。
    3. 展示研究方法：访谈、观察、服务蓝图、WoZ 或可用性测试。
    4. 展示评估指标：至少选择 trust、workload、situation awareness、usability 中的 1-2 个。
    5. 反思边界：安全、隐私、责任和长期采纳。
    """


def topics_doc() -> str:
    poster = [
        "AR 路径提示如何影响用户对移动机器人意图的理解？",
        "服务机器人失败解释粒度对信任校准的影响",
        "协作机械臂可读运动与工作负荷的关系",
        "LLM 机器人中间层的可执行性反馈设计",
        "公共空间 robotiquette 的设计模式研究",
        "老年陪护机器人隐私边界的参与式设计",
        "多模态反馈对远程巡检情境感知的影响",
        "酒店配送机器人等待状态表达研究",
        "机器人人格强度对服务失败容忍度的影响",
        "GraphRAG 辅助 HRI 设计机会生成的初步研究",
    ]
    papers = [
        "From Robot Autonomy to Human Agency: A Design Framework for Calibrated Control",
        "Designing Failure Recovery for Service Robots in Hospitality Contexts",
        "AR-mediated Legibility in Human-Robot Collaboration",
        "Grounded LLM Mediation for Human-AI-Robot Task Negotiation",
        "Robotiquette in Public Space Service Robotics",
        "Designing Explainable Status Feedback for Autonomous Service Robots",
        "Multimodal Feedback and Workload in Robot Teleoperation",
        "A Knowledge Graph Framework for HRI-Oriented Design Research",
        "Anthropomorphism Boundaries in Elderly Care Robots",
        "Service Blueprinting as a Method for Robotic Experience Design",
    ]
    rtd = [
        "用可调人格机器人原型探索拟人化边界",
        "用 AR 原型探索机器人不可见计划的可视化",
        "用实体任务卡探索家庭机器人可供性",
        "用未来服务蓝图探索医院机器人责任链",
        "用设计虚构探索 LLM 机器人物理行动风险",
        "用 WoZ 原型探索机器人澄清对话",
        "用触觉原型探索远程操作安全感",
        "用注释作品集整理 HRI 失败恢复模式",
        "用低保真机器人行为剧本探索 public robotiquette",
        "用 GraphRAG 工具探索设计师如何生成 HRI 机会点",
    ]
    return f"""
    # 论文与 Poster 选题

    ## 10 个 Conference Poster 选题
    """ + "\n".join(f"{i+1}. {x}" for i, x in enumerate(poster)) + """

    ## 10 个论文雏形选题
    """ + "\n".join(f"{i+1}. {x}" for i, x in enumerate(papers)) + """

    ## 20 个设计研究问题
    """ + "\n".join(f"{i+1}. {rq[0]} 方法：{rq[2]}；可能数据：{rq[3]}；预期贡献：{rq[4]}。" for i, rq in enumerate(RESEARCH_QUESTIONS)) + """

    ## 10 个 Research through Design 方向
    """ + "\n".join(f"{i+1}. {x}" for i, x in enumerate(rtd)) + """

    ## 投稿/展示理由

    这些选题适合 HRI、CHI LBW / poster、设计学院作品集和本科/研究生研究计划，因为它们都具备：明确场景、可操作原型、可测量指标、文献来源和设计贡献。
    """


def llm_reuse_doc() -> str:
    return f"""
    # 大模型复用与知识库结构

    ## RAG

    把 Markdown 文档按标题层级切分。推荐 chunk metadata 包含：`doc_path`、`section_title`、`ontology_category`、`node_type`、`source_ids`、`confidence_level`。查询例子：

    - “给我生成一个关于医院服务机器人的设计机会。”
    - “找出与 trust calibration 相关的评估指标和论文。”
    - “AR/MR 机器人界面有哪些适合 poster 的问题？”

    ## GraphRAG

    把 `data/graph/nodes.json` 与 `data/graph/relations.json` 导入图数据库或轻量图结构。GraphRAG 的核心不是只检索相似文本，而是沿关系查询：

    `Scenario -> requires -> Concept -> measured_by -> Metric -> derived_from -> Source`

    示例：

    `Industrial Assembly -> requires -> Legible Motion -> measured_by -> Goal Inference Accuracy -> derived_from -> Dragan et al. {source_link('S13')}`

    ## 设计机会生成 Prompt 结构

    1. 输入场景：如“酒店配送机器人”。
    2. 检索相关节点：Service Robot、Failure Recovery、Trust、Status Visibility。
    3. 沿关系获取证据：HRI survey、trust meta-analysis、service scenario。
    4. 输出机会卡：目标用户、核心问题、原型形式、评估指标、参考文献。

    ## 研究问题生成 Prompt 结构

    1. 选择一个关系：`Robot Autonomy -- influences --> Trust`。
    2. 添加场景：医院导诊或工业协作。
    3. 添加方法：controlled experiment / Wizard-of-Oz。
    4. 添加指标：trust、workload、situation awareness。
    5. 生成可检验研究问题和实验设计。

    ## 持续更新流程

    - 新文献进入 `appendix/参考文献整理模板.md`。
    - 提炼概念写入 `data/graph/nodes.json`。
    - 提炼关系写入 `data/graph/relations.json`。
    - 新术语进入 `tables/术语表.csv`。
    - 运行 `python scripts/validate_graph.py` 检查图谱一致性。
    """


def conclusion_doc() -> str:
    return """
    # 结论与未来工作

    ## 核心贡献

    本文档包把“智能交互设计 × 机器人”组织为一个可读、可检索、可扩展、可被大模型复用的研究系统。它包含中文研究报告、ontology、节点/关系 schema、主题模块、方法与评估指标、设计机会、研究问题、三元组、JSON 示例和作品集/poster 模板。

    ## 对智能交互设计的意义

    它帮助设计学习者从“界面和视觉”进入“智能行为、具身行动、责任边界和评估证据”的层面。智能交互设计不再只是给 AI 或机器人做 UI，而是设计人、AI、机器人和场景之间的协作条件。

    ## 对 HRI 学习的意义

    通过顶层 ontology 和主题模块，你可以系统学习 HRI 的学科结构：人、机器人、交互、智能、具身、界面、场景、任务、评估和伦理。通过三元组，你可以看到概念之间的因果、依赖和设计转化路径。

    ## 对作品集和研究的意义

    设计机会表和研究问题表可以直接转化为作品集 brief、conference poster、论文雏形或研究计划。关键是每个项目都要保留“来源 -> 图谱路径 -> 设计假设 -> 原型 -> 评估”的证据链。

    ## 后续扩展

    1. 选择 3 个最感兴趣的场景，补充真实案例和用户研究。
    2. 为 10 篇核心论文写 literature note。
    3. 把 nodes/relations 导入图数据库或 Obsidian/Neo4j。
    4. 选择 1 个机会点做低保真原型和 WoZ 测试。
    5. 把测试结果回写为新的证据节点和设计原则。
    """


def simple_doc(title: str, body: str) -> str:
    return f"# {title}\n\n{body.strip()}\n"


def scripts() -> dict[str, str]:
    return {
        "scripts/validate_graph.py": r'''
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
''',
        "scripts/convert_triples_to_json.py": r'''
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
''',
        "scripts/export_glossary.py": r'''
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
''',
        "scripts/generate_opportunity_cards.py": r'''
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
''',
    }


def write_all() -> None:
    # Main docs.
    write_text("README.md", f"""
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
    - `tables/`：适合 Excel 的 CSV 表格。
    - `appendix/`：三元组、JSON 示例、来源记录和模板。
    - `data/`：schema、nodes、relations 和 graph sample。
    - `scripts/`：验证和转换脚本。

    ## 来源策略

    文档引用使用 `Sxx` 编号，并在 `appendix/来源与检索记录.md` 中保留作者、年份、出处、链接和用途。核心来源包括 Goodrich & Schultz 的 HRI survey {source_link('S01')}、Fong 等社会机器人综述 {source_link('S02')}、HRI trust 元分析 {source_link('S05')}、VAM-HRI survey {source_link('S12')}、RtD 经典文献 {source_link('S14')} {source_link('S15')}、ISO 机器人安全标准 {source_link('S21')} {source_link('S22')}。

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
    """)
    write_text("01_主研究报告.md", main_report())
    write_text("02_知识图谱框架说明.md", kg_framework_doc())
    write_text("03_顶层本体与领域边界.md", f"""
    # 顶层本体与领域边界

    ## Scope Statement

    本知识图谱研究“智能交互设计 × 机器人”交叉领域，重点关注 HRI 中与人类理解、控制、信任、安全、服务体验、社会关系和设计研究方法有关的知识。它服务设计学生、研究者、机器人开发者、产品/服务设计师、AI agent 和大模型知识库。

    ## Inclusion Criteria

    - 与 Human-Robot Interaction、HCI、机器人交互、具身智能或设计研究直接相关。
    - 能转化为交互设计问题、评估指标、原型方向或研究问题。
    - 有可回溯来源：论文、标准、官方网页、案例或本地研究笔记。
    - 能进入节点、关系、三元组或表格结构。

    ## Exclusion Criteria

    - 纯底层控制算法推导，且无法转化为人类体验问题。
    - 与交互无关的机械结构细节。
    - 纯模型训练技巧或 benchmark，而没有 HRI/设计意义。
    - 没有来源、不可追溯或明显营销化的断言。

    ## Core Research Questions

    """ + "\n".join(f"{i+1}. {rq[0]}" for i, rq in enumerate(RESEARCH_QUESTIONS[:8])) + "\n\n" + tree_markdown() + "\n\n" + ontology_markdown())
    write_text("04_节点类型与关系类型.md", f"""
    # 节点类型与关系类型

    ## 节点类型

    | 节点类型 | 英文名称 | 定义 | 字段 | 示例 | 用途 |
    |---|---|---|---|---|---|
    """ + "\n".join(f"| {r[1]} | {r[0]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |" for r in NODE_TYPE_ROWS) + "\n\n" + relation_examples_markdown())
    write_text("05_核心主题模块.md", themes_markdown())
    write_text("06_机器人系统视角.md", robot_system_doc())
    write_text("07_交互设计视角.md", interaction_design_doc())
    write_text("08_研究方法与评估指标.md", methods_metrics_doc())
    write_text("09_设计机会与作品集方向.md", design_opportunities_doc())
    write_text("10_论文与Poster选题.md", topics_doc())
    write_text("11_大模型复用与知识库结构.md", llm_reuse_doc())
    write_text("12_结论与未来工作.md", conclusion_doc())

    # Tables.
    write_csv("tables/术语表.csv", ["英文术语", "中文术语", "定义", "相关概念", "设计意义", "示例场景"], GLOSSARY)
    write_csv("tables/节点类型表.csv", ["节点类型", "英文名称", "定义", "字段", "示例", "用途"], [[r[1], r[0], r[2], r[3], r[4], r[5]] for r in NODE_TYPE_ROWS])
    write_csv("tables/关系类型表.csv", ["关系类型", "中文解释", "使用场景", "示例三元组"], RELATION_TYPE_ROWS)
    write_csv("tables/主题模块表.csv", ["主题", "英文名称", "定义", "关键词", "相关方法", "应用场景", "设计机会"], [[t[0].split("/")[1].strip() if "/" in t[0] else t[0], t[0].split("/")[0].strip(), t[1], t[2], t[5], t[7], t[10]] for t in THEMES])
    write_csv("tables/研究方法表.csv", ["方法名称", "英文名称", "定义", "适用阶段", "优点", "局限", "适合项目"], [[m[1], m[0], m[2], m[3], m[4], m[5], m[6]] for m in METHODS])
    write_csv("tables/评估指标表.csv", ["指标名称", "英文名称", "定义", "测量方式", "适用场景", "相关设计问题"], [[m[1], m[0], m[2], m[3], m[4], m[5]] for m in METRICS])
    write_csv("tables/应用场景表.csv", ["场景", "机器人类型", "用户群体", "核心任务", "交互问题", "设计机会"], SCENARIOS)
    write_csv("tables/设计机会表.csv", ["方向标题", "目标用户", "场景", "核心问题", "相关知识节点", "原型形式", "评估方法", "作品集价值"], OPPORTUNITIES)
    write_csv("tables/研究问题表.csv", ["研究问题", "所属主题", "研究方法", "可能数据", "预期贡献", "可转化方向"], RESEARCH_QUESTIONS)

    # Mirror tables into data/tables with English names.
    write_csv("data/tables/glossary.csv", ["English Term", "Chinese Term", "Definition", "Related Concepts", "Design Relevance", "Example Scenario"], GLOSSARY)
    write_csv("data/tables/design_opportunities.csv", ["Opportunity Title", "Target Users", "Scenario", "Core Problem", "Related Knowledge Nodes", "Prototype", "Evaluation Metrics", "Portfolio Value"], OPPORTUNITIES)
    write_csv("data/tables/research_questions.csv", ["Research Question", "Theme", "Method", "Possible Data", "Contribution", "Translation"], RESEARCH_QUESTIONS)
    write_csv("data/tables/thematic_modules.csv", ["Theme", "Definition", "Keywords", "Disciplines", "Questions", "Methods", "Design Relevance", "Scenarios"], [[t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]] for t in THEMES])
    write_csv("data/tables/evaluation_metrics.csv", ["Metric", "Chinese", "Definition", "Measurement", "Scenario", "Design Issue"], [[m[0], m[1], m[2], m[3], m[4], m[5]] for m in METRICS])
    write_csv("data/tables/methods.csv", ["Method", "Chinese", "Definition", "Stage", "Pros", "Limits", "Suitable Project"], METHODS)

    # Appendices.
    write_text("appendix/知识图谱三元组.md", "# 知识图谱三元组\n\n" + "\n".join(triples()))
    write_json("appendix/JSON知识图谱示例.json", kg_sample())
    write_text("appendix/来源与检索记录.md", f"""
    # 来源与检索记录

    检索日期：2026-06-19。网络与数据库来源包括 web search、OpenAlex API、出版商 DOI 页面、ACM/IEEE/ISO/IFR 官方网站、arXiv/PMLR 页面。引用采用 `Sxx` 编号，所有编号在文档中可回溯。

    {sources_markdown()}
    """)
    write_text("appendix/参考文献整理模板.md", """
    # 参考文献整理模板

    ## 文献标题

    - 作者：
    - 年份：
    - 会议 / 期刊：
    - DOI / 链接：
    - 文献类型：peer-reviewed / survey / preprint / standard / official website / case
    - 研究主题：
    - 方法：
    - 核心观点：
    - 与本课题关系：
    - 可转化的设计启发：
    - 可进入的节点：
    - 可新增的关系：
    - 可信度标记：high / medium / low
    - 备注：是否需要进一步检索？
    """)
    write_text("appendix/作品集案例研究模板.md", """
    # 作品集案例研究模板

    ## 项目标题
    ## 项目概述
    ## 研究背景
    ## 核心问题
    ## 我的角色
    ## 研究过程
    - 桌面研究
    - 文献证据
    - 用户/场景研究
    - 知识图谱路径
    - 设计机会推导
    ## 知识图谱方法
    写出：Source -> Concept -> Scenario -> Design Issue -> Prototype -> Metric。
    ## 关键洞察
    ## 设计机会
    ## 原型方向
    ## 评估方法
    ## 最终输出
    ## 反思与下一步
    """)
    write_text("appendix/Conference_Poster_中文模板.md", """
    # Conference Poster 中文模板

    ## 标题
    ## 背景
    ## 研究空白
    ## 研究目标
    ## 方法
    ## 知识图谱框架
    ## 示例路径
    ## 设计转化
    ## 贡献
    ## 局限
    ## 未来工作
    ## 二维码占位
    """)
    write_text("appendix/知识图谱图册模板.md", """
    # Knowledge Graph Atlas / 知识图谱图册模板

    1. Cover
    2. Field Boundary Map
    3. Top-Level Ontology Map
    4. Human-Robot-Interaction System Map
    5. Core Theme Network
    6. Robot System × Interaction Design Matrix
    7. Research Methods Map
    8. Evaluation Metrics Map
    9. Scenario Map
    10. Design Opportunity Map
    11. LLM Reuse Pipeline
    12. Final Contribution Summary
    """)

    # Data.
    write_json("data/schemas/node.schema.json", node_schema())
    write_json("data/schemas/relation.schema.json", relation_schema())
    write_json("data/schemas/knowledge_graph.schema.json", knowledge_graph_schema())
    write_json("data/graph/nodes.json", NODES)
    write_json("data/graph/relations.json", RELATIONS)
    write_text("data/graph/triples.md", "# Knowledge Triples\n\n" + "\n".join(triples()))
    write_json("data/graph/knowledge_graph_sample.json", kg_sample())

    for path, content in scripts().items():
        write_text(path, content)

    # Output directories.
    for folder in ["outputs/report", "outputs/atlas", "outputs/poster", "outputs/portfolio"]:
        (BASE / folder).mkdir(parents=True, exist_ok=True)
        (BASE / folder / ".gitkeep").write_text("", encoding="utf-8")

    normalize_markdown_files()


def normalize_markdown_files() -> None:
    """Remove template indentation from generated Markdown documents.

    Several long f-strings intentionally live inside indented Python blocks.
    When an inserted unindented ontology block appears in the same string,
    textwrap.dedent cannot infer the intended common indentation. This pass
    keeps the output Word/Markdown friendly without touching Python scripts.
    """
    for path in BASE.rglob("*.md"):
        lines = path.read_text(encoding="utf-8").splitlines()
        cleaned = [line[4:] if line.startswith("    ") else line for line in lines]
        path.write_text("\n".join(cleaned).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_all()
    print(f"Generated research package at {BASE.resolve()}")
