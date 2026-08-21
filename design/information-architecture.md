# 个人网站信息架构 / Portfolio Information Architecture

## 1. Content strategy

网站的核心不是“列出做过什么”，而是建立一条清晰证据链：

> 我关注什么问题 → 我怎样研究与原型化 → 我在项目中具体做了什么 → 结果与反思是什么 → 我适合怎样的岗位或合作。

V1 采用“小而完整”的结构。首页完成身份判断和项目分流，案例页负责证明能力，About / CV 负责补全经历。学术气质来自研究问题、方法、证据、引用和反思，而不是单独挂一个没有论文内容的 Research 标签。

## 2. Sitemap

```text
senpeichan.github.io
├── /                            中文首页
│   ├── /work/                   可持续扩展的完整项目档案
│   ├── /work/[slug]/            数据驱动的通用项目详情页
│   ├── /about/                  关于 / 教育 / 经历 / 能力
│   └── /documents/              CV 与作品集资料接口
└── /en/                         English home
    ├── /work/
    ├── /work/qingzhu/
    ├── /work/co-evo/
    ├── /work/bingbing/
    ├── /work/hive-wings/
    ├── /about/
    └── /documents/
```

根路径 `/` 可默认进入中文首页，也可根据浏览器语言做一次温和跳转；任何页面的语言切换都应进入对应页面，而不是回到首页。

### Global navigation

| 中文 | English | 行为 |
|---|---|---|
| 项目 | Work | 进入可持续扩展的项目档案 |
| 关于 | About | 进入 About 页面 |
| 资料 | Documents | CV 下载与作品集 PDF 在线查看 / 下载 |
| 联系 | Contact | 首页或 About 的联系区 |
| 中 / EN | 中 / EN | 切换当前页面语言 |

不保留现站中的“研究 / 实验”独立导航。相关内容会在首页“研究关注”和各案例的过程模块中出现。

## 3. Homepage structure

### 3.1 Header

- 左侧：`陈森培 / Senpei Chen`，作为返回首页链接。
- 右侧：Work、About、Documents、Contact、语言切换。
- 白色背景、1 px 底部细线；滚动后可保持粘性。

### 3.2 Hero — identity in 10 seconds

**中文建议文案**

> 陈森培 / Senpei Chen  
> 人机交互与智能交互设计本科生  
> 我关注实体交互、AI 视觉与智能硬件体验，通过用户研究和原型实验，把技术机制转化为可理解、可使用、可感知的交互。

**English draft**

> Senpei Chen  
> HCI & Interaction Design Undergraduate  
> I explore physical interaction, AI vision, and smart hardware experiences, using user research and prototyping to turn technical systems into interactions people can understand, use, and feel.

首屏动作：

- 主按钮：查看项目 / View selected work
- 次按钮：下载简历 / Download CV
- 文本链接：联系我 / Get in touch
- 状态标签：`广州美术学院 · 2028 届 · Available for internship`（公开前确认）

首屏加入本人照片，与研究定位和项目入口共同构成个人识别；项目证据仍然是首页主体。

### 3.3 Selected work — four evidence-rich projects

首页当前展示 4 个精选项目，不再使用“近期实践”这类泛化卡片。项目数量不写死；新项目可进入完整档案，也可通过 `featuredRank` 加入首页。当前排序：

1. **倾注 / Qingzhu** — 身体参与式输入、智能硬件、App 联动；最接近 HCI + 智能硬件定位。
2. **CO-EVO Prelude** — 身体姿态、YOLO、TouchDesigner；证明 AI 视觉与空间交互能力。
3. **冰冰 / Bingbing** — 问卷访谈、用户旅程、拆机、结构与 CMF；证明研究到产品方案的闭环。
4. **蜂巢之翼 / Wings of the Hive** — 机构、舵机、实体原型；证明实体计算与迭代能力。

每张项目卡固定展示：

- 项目中英文名与一句话命题。
- 年份、角色、团队 / 个人项目。
- 2–3 个能力标签，而不是长工具列表。
- 一张高质量主图。
- `View case study` 明确入口。

### 3.4 Research interests — academic flavor without overclaiming

标题建议：`我正在探索的问题 / Questions I’m exploring`

- 身体动作如何成为比点击、滑动更自然、更有情绪感的交互输入？
- 计算机视觉如何让身体与空间成为直接界面？
- 用户研究如何共同塑造智能硬件的形态、机构与系统反馈？

这一区域只陈述“当前问题”，不把课程项目包装成已经验证的研究结论。

### 3.5 Capabilities — evidence, not software cloud

将技能压缩为四组，每组链接到最能证明它的项目：

- **研究与洞察**：桌面研究、竞品分析、问卷、访谈、用户旅程、原型测试。
- **交互与产品**：交互流程、智能硬件交互、产品概念、界面与信息可视化。
- **AI 与视觉系统**：YOLO 数据集、标注、训练观察、TouchDesigner、AIGC 辅助设计。
- **实体原型**：Arduino、ESP32、STM32、Physical Computing、3D 打印、激光切割。

工具名放在次级层级，优先讲能完成的任务。

### 3.6 Current practice / experience

- `Robocon 2026 — 队伍建设与机器人开发`：用 3–4 行说明队长职责、跨模块协同与当前阶段。
- 教育与荣誉：广州美术学院智能交互设计本科（2024–2028）；2024–2025 学年“三好学生”二等奖学金。
- 链接到 About，避免首页复制完整 CV。

### 3.7 Contact footer

- 邮箱：`chensenpei@email.gzarts.edu.cn`
- GitHub：`github.com/SenpeiCHAN`
- LinkedIn / Behance：收到真实链接后再显示。
- 简短邀请：`欢迎讨论 HCI、智能硬件、AI 交互与实习机会。`
- 不建议公开个人电话。

## 4. Project evidence map

| 项目 | 作品集页码 | 首页定位 | 主要证据 | 需要补充 |
|---|---:|---|---|---|
| 倾注 | 3–12 | HCI / Smart Hardware | 市场与用户洞察、拍打式交互、硬件交互、App 流程与设计规范 | 原型视频、个人角色确认、是否完成用户测试 |
| 冰冰 | 13–30 | User Research / Product Redesign | 市场与竞品、问卷访谈、用户旅程、拆机、4 轮方案、结构与 CMF | 样本量与访谈人数、测试反馈、团队分工 |
| 蜂巢之翼 | 31–45 | Physical Computing / Kinetic Interaction | 结构拆解、3 轮以上形态迭代、机构与舵机、制作过程、最终原型 | 控制逻辑、演示视频、故障与改进记录 |
| CO-EVO | 46–55 | AI Vision / Embodied Interaction | 姿态设计、技术路线、数据集、训练参数与 loss、TouchDesigner、现场落地 | 数据集规模核对、模型指标口径、个人贡献与团队署名 |
| Robocon 2026 | CV | Leadership / Robotics Practice | 队伍从 0 到 1、跨组协作、资源与阶段管理 | 视觉材料、机器人系统图、个人技术工作后再升级为案例 |

## 5. Case-study template

每个案例页统一采用以下结构，控制在 6–9 个核心模块：

1. **Project hero**  
   主图、项目名、一句话命题、年份、角色、团队、周期、方法与工具。

2. **Context & research question**  
   真实场景、目标用户、问题背景；用一个明确问题替代泛化“项目简介”。

3. **My role & contribution**  
   单独列出个人负责内容，并区分主导、共同完成与协助。

4. **Research & evidence**  
   方法、样本、关键发现、引用来源与证据限制。图表只保留能支撑设计决策的部分。

5. **Design principles**  
   将洞察转译成 3–5 条设计原则或系统需求。

6. **Interaction / system / mechanism**  
   用流程图、系统图或机构图解释“它如何工作”。

7. **Iterations & prototype**  
   展示关键失败、取舍和版本差异，不只陈列最终渲染。

8. **Outcome & evaluation**  
   分开写已完成产出、已观察反馈、尚未验证的问题；没有数据时不虚构影响。

9. **Reflection & next step**  
   说明如果继续，会怎样改进研究与设计。

页尾提供前后项目导航与联系入口。

## 6. About / CV page

建议顺序：

1. 简短个人介绍与工作方式。
2. 当前研究关注：HCI、physical interaction、AI vision、smart hardware。
3. 教育与荣誉。
4. 经历时间线：Robocon + 四个项目。
5. 能力与工具分组。
6. 下载公开版 CV。
7. 联系方式与真实社交链接。

About 页可以使用证件照或自然工作照，但主页面应以项目证据为主。

## 7. Bilingual content model

- 采用独立 `/zh/` 与 `/en/` 路径，利于分享、SEO 和保持当前阅读位置。
- 页面组件共用，文字数据按 locale 管理，避免手工维护两套结构。
- 项目专有名词首次出现保留中文原名与英文工作译名。
- 时间、工具、模型名、数字等中英共用；角色、方法和反思必须分别润色，不能只做直译。
- 中文标点和英文标点按语言分别排版；正文不逐句并排双语。
- 图片 alt、页面 title、description、Open Graph 文案均需双语版本。

### Working English project names

- `倾注 — Qingzhu: A Tactile Focus Companion`
- `冰冰 — Bingbing: A Dual-use Home Ice Maker Redesign`
- `蜂巢之翼 — Wings of the Hive: A Transformable Kinetic Window`
- `CO-EVO 研究生展演序幕 — CO-EVO Prelude: Body-as-Letter AI Interaction`

这些名称为工作译名，上线前由本人确认。

## 8. Visual direction

### Overall tone

**White editorial research portfolio**：纯白、图像主导、强排版、细线网格、项目色轻提示。求职信息应易扫读，研究内容应可追溯。

### Borrow from the portfolio

- 大幅 16:9 项目图与宽屏构图。
- 大量留白与左对齐信息层级。
- 每个项目拥有自己的低饱和色：倾注暖杏、冰冰浅蓝、蜂巢冷灰、CO-EVO 淡紫蓝。
- 中英文小标题、页码感编号、图注与方法标签。

### Do not carry over

- 作品集中单页过多的小字号信息、密集表格与整页 PPT 式拼贴。
- 现站的黑底、霓虹、扫描线、终端面板和多彩状态灯。
- 通用 SaaS 卡片、过度圆角、渐变背景、装饰性玻璃拟态。
- 卡片 hover 放大；只使用轻微位移、下划线或图片透明度变化。

## 9. Responsive behavior

- Desktop：最大内容宽度约 1200 px；12 列网格；项目图片可跨 7–8 列。
- Tablet：6 列；项目元数据下移，不压缩成小字。
- Mobile：单列；导航可折叠，但语言切换与 Work 入口保持直接可见。
- 正文建议 17–18 px，行高 1.65；项目图不裁掉交互关键区域。
- 数据表在移动端转为可读卡片或横向滚动，不强行缩小。

## 10. Current-site cleanup

- 将 `Pacey Chen` 统一为 `Senpei Chen`。
- 将现站“人-机器人交互 / HCI / 工业设计 / AI / 实验实践”五方向收束为一个 HCI 主定位和三类支撑能力。
- 把“项目”导航从页面锚点变为真实案例入口。
- 删除跳回 `#top` 的 Behance、Instagram、LinkedIn、CV 占位链接。
- 用真实项目标题和证据替换三张泛化“近期实践”卡片。
- 保留中英切换能力，但迁移到稳定的语言路由。

## 11. Recommended next phase

1. 逐项目确认个人角色、团队署名、样本量与可公开结果。
2. 继续补充项目原图、系统图、演示视频与过程证据。
3. 用 `content/site.ts` 的数据记录持续增加项目与资料，不复制页面结构。
4. 完成无障碍、性能与 GitHub Pages 部署适配后再发布。
