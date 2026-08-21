export type Locale = "zh" | "en";

export type LocalizedText = Record<Locale, string>;

export type ProjectStatus = "published" | "draft" | "archived";

export type ProjectMedia = {
  src: string;
  alt: LocalizedText;
  caption?: LocalizedText;
};

export type ProjectSection = {
  id: string;
  label: LocalizedText;
  title: LocalizedText;
  body: LocalizedText;
  details?: Record<Locale, string[]>;
  image?: string;
  imageAlt?: LocalizedText;
  caption?: LocalizedText;
  gallery?: ProjectMedia[];
};

export type Project = {
  slug: string;
  status: ProjectStatus;
  featuredRank?: number;
  year: string;
  title: LocalizedText;
  shortTitle: LocalizedText;
  subtitle: LocalizedText;
  summary: LocalizedText;
  role: LocalizedText;
  question: LocalizedText;
  contributions: Record<Locale, string[]>;
  sections: ProjectSection[];
  tags: Record<Locale, string[]>;
  cover: string;
  theme: "apricot" | "ice" | "graphite" | "lavender";
};

export const profile = {
  name: "Senpei Chen",
  chineseName: "陈森培",
  email: "chensenpei@email.gzarts.edu.cn",
  github: "https://github.com/SenpeiCHAN",
  portrait: "/images/profile/senpei-chen.png",
  resumeUrl: "/files/Senpei-Chen-CV.docx",
  portfolioUrl: "/files/Senpei-Chen-Portfolio.pdf",
  headline: {
    zh: "从人出发，研究技术该怎样回应。",
    en: "I study how technology can respond to human action and everyday objects.",
  },
  intro: {
    zh: "我是陈森培，就读于广州美术学院智能交互设计专业。我的项目涉及人机交互、智能硬件、AI 视觉和产品设计。我通常先观察真实使用情境，再用访谈、结构拆解、编程和实体原型把问题做清楚。",
    en: "I’m Senpei Chen, an Interaction Design undergraduate at Guangzhou Academy of Fine Arts. My work spans HCI, smart hardware, AI vision, and product design. I begin with real use situations, then use interviews, teardown, code, and physical prototypes to make the problem concrete.",
  },
};

export const documents = [
  {
    id: "cv",
    title: { zh: "个人简历", en: "Curriculum Vitae" },
    description: {
      zh: "教育、项目与研究实践、技能和工具的完整简历。",
      en: "A complete overview of education, projects, research practice, skills, and tools.",
    },
    format: "DOCX",
    href: "/files/Senpei-Chen-CV.docx",
    previewable: false,
  },
  {
    id: "portfolio",
    title: { zh: "项目作品集", en: "Project Portfolio" },
    description: {
      zh: "",
      en: "",
    },
    format: "PDF · 56 pages",
    href: "/files/Senpei-Chen-Portfolio.pdf",
    previewable: true,
  },
];

export const researchQuestions = [
  {
    title: {
      zh: "人与智能硬件设备的交互",
      en: "Human-smart hardware",
    },
    body: {
      zh: "我关注动作、触感和物理反馈如何让设备更容易理解。比起把所有操作放进屏幕，我更想知道：旋转、拍打、握持或移动能否成为准确而自然的输入。",
      en: "I look at how movement, touch, and physical feedback make a device easier to understand. Instead of placing every control on a screen, I ask whether turning, tapping, holding, or moving can become clear inputs.",
    },
  },
  {
    title: {
      zh: "人与 AI 的交互",
      en: "Human-AI",
    },
    body: {
      zh: "我在意 AI 如何被人看见、理解和修正。研究重点不是隐藏模型，而是让识别结果、出错范围和反馈过程变得可感知，让人知道系统正在做什么。",
      en: "I care about how people see, understand, and correct AI. Rather than hiding the model, I want recognition results, errors, and system feedback to remain perceptible.",
    },
  },
  {
    title: {
      zh: "用户研究如何塑造智能硬件",
      en: "How research shapes smart hardware",
    },
    body: {
      zh: "用户研究不只决定功能清单。观察到的动作、困难和使用顺序，也应进入外形、内部机构与系统反馈的设计，让研究结果能在产品上被直接看见和使用。",
      en: "User research should do more than define features. Observed actions, difficulties, and task order can also shape form, internal mechanisms, and system feedback.",
    },
  },
];

export const approachSteps = [
  {
    title: { zh: "文献与案例", en: "Literature & cases" },
    body: {
      zh: "搜集相关文献、既有案例、常见分析框架和视觉参考，确认问题已有的讨论与方案边界。",
      en: "I review literature, prior cases, common analytical frameworks, and visual references to understand what is already known and where existing solutions stop.",
    },
  },
  {
    title: { zh: "场景与体验", en: "Context & experience" },
    body: {
      zh: "进入真实场景，观察任务、环境和限制，并亲自体验问题发生的过程。",
      en: "I enter the real setting, observe tasks, environments, and constraints, and experience how the problem occurs firsthand.",
    },
  },
  {
    title: { zh: "访谈与分析", en: "Interviews & analysis" },
    body: {
      zh: "用访谈理解原因，用问卷观察分布和差异，再根据数据类型完成基础统计与交叉比较。",
      en: "Interviews help explain why; surveys show distributions and differences. I then use suitable descriptive statistics and cross-comparisons.",
    },
  },
  {
    title: { zh: "洞察与问题", en: "Insights & questions" },
    body: {
      zh: "整理材料中的模式，区分事实、假设和机会点，形成可以由设计或实验回答的问题。",
      en: "I organize patterns in the material, separate evidence from assumptions, and frame questions that design or an experiment can answer.",
    },
  },
  {
    title: { zh: "构思与原型", en: "Concepts & prototypes" },
    body: {
      zh: "根据要验证的问题，选择草图、交互流程、结构模型、代码或硬件，制作合适保真度的原型。",
      en: "I choose sketches, interaction flows, structural models, code, or hardware at the fidelity needed to answer the question.",
    },
  },
  {
    title: { zh: "测试与反馈", en: "Testing & feedback" },
    body: {
      zh: "让目标用户在具体任务中使用原型，记录行为、错误、完成情况和主观反馈。",
      en: "Target users try the prototype in concrete tasks while I record behavior, errors, task completion, and subjective feedback.",
    },
  },
  {
    title: { zh: "优化与结论", en: "Refinement & conclusion" },
    body: {
      zh: "根据证据修改方案并再次验证，直到达到交付条件；若假设不成立，也清楚记录结论和边界。",
      en: "I revise and test again until the work is ready to deliver. If the hypothesis fails, I document the conclusion and its limits.",
    },
  },
];

export const capabilityGroups = [
  {
    title: { zh: "研究与洞察", en: "Research & insight" },
    items: {
      zh: ["桌面研究", "竞品分析", "问卷与访谈", "用户旅程", "原型测试"],
      en: ["Desk research", "Competitive analysis", "Surveys & interviews", "User journeys", "Prototype testing"],
    },
  },
  {
    title: { zh: "交互与产品", en: "Interaction & product" },
    items: {
      zh: ["交互流程", "智能硬件", "产品概念", "信息可视化", "CMF"],
      en: ["Interaction flows", "Smart hardware", "Product concepts", "Information visualization", "CMF"],
    },
  },
  {
    title: { zh: "AI 与视觉系统", en: "AI & visual systems" },
    items: {
      zh: ["YOLO 数据集与训练", "TouchDesigner", "AIGC 辅助设计", "视觉反馈"],
      en: ["YOLO datasets & training", "TouchDesigner", "AIGC-assisted design", "Visual feedback"],
    },
  },
  {
    title: { zh: "实体原型", en: "Physical prototyping" },
    items: {
      zh: ["Arduino / ESP32 / STM32", "3D 打印", "激光切割", "结构与机构实验"],
      en: ["Arduino / ESP32 / STM32", "3D printing", "Laser cutting", "Structural experiments"],
    },
  },
];

export const timeline = [
  {
    year: "2024–2028",
    title: {
      zh: "广州美术学院 · 智能交互设计本科",
      en: "Guangzhou Academy of Fine Arts · BFA in Interaction Design",
    },
    description: {
      zh: "学习人机交互、用户研究、信息可视化、产品结构、实体计算与人工智能。",
      en: "Studying HCI, user research, information visualization, product structure, physical computing, and AI.",
    },
  },
  {
    year: "2026",
    title: {
      zh: "Robocon 2026 · 队长",
      en: "Robocon 2026 · Team lead",
    },
    description: {
      zh: "从 0 到 1 组织机械、电控、视觉与运营团队，推进机器人设计、装配与迭代。",
      en: "Building a cross-disciplinary mechanical, electronics, vision, and operations team from the ground up.",
    },
  },
  {
    year: "2024–2025",
    title: {
      zh: "“三好学生”二等奖学金",
      en: "Second-class scholarship for academic and community achievement",
    },
    description: {
      zh: "广州美术学院 2024–2025 学年。",
      en: "Guangzhou Academy of Fine Arts, academic year 2024–2025.",
    },
  },
];

// Add a project by appending one record here. Routes and project grids are
// generated from this collection; no page component needs to be duplicated.
export const projects: Project[] = [
  {
    slug: "qingzhu",
    status: "published",
    featuredRank: 1,
    year: "2026",
    title: {
      zh: "倾注：轻动力辅助专注产品",
      en: "Qingzhu: A Tactile Focus Companion",
    },
    shortTitle: { zh: "倾注", en: "Qingzhu" },
    subtitle: {
      zh: "一件用拍打、旋转和轻触操作的桌面专注设备。",
      en: "A desktop focus device controlled through tapping, turning, and touch.",
    },
    summary: {
      zh: "倾注把开始专注这件事从手机菜单移到桌面。设备承担即时操作，App 负责模式设置和记录，两者各做自己擅长的事。",
      en: "Qingzhu moves the start of a focus session from a phone menu onto the desk. The device handles immediate actions; the app handles settings and records.",
    },
    role: { zh: "核心成员", en: "Core team member" },
    question: {
      zh: "开始专注能否像拍下一只开关一样直接，同时保留足够清楚的状态反馈？",
      en: "Can starting a focus session feel as direct as striking a switch while still giving clear feedback?",
    },
    contributions: {
      zh: ["参与定义拍倒启动、旋钮切换与触摸反馈", "整理专注场景、人物画像和设计目标", "协同设备屏幕与手机端的状态分工", "完成产品渲染、场景图和界面表达"],
      en: ["Co-defined tap-to-start, dial selection, and touch feedback", "Mapped focus contexts, personas, and design goals", "Separated device and mobile responsibilities", "Produced product, scenario, and interface visuals"],
    },
    sections: [
      {
        id: "literature-cases",
        label: { zh: "01 · 文献与案例", en: "01 · Literature & cases" },
        title: { zh: "现有专注工具大多把操作留在屏幕里", en: "Most focus tools keep interaction on the screen" },
        body: {
          zh: "前期调研比较了数字专注工具、桌面计时器与陪伴型设备。它们能管理任务，却常要求用户重新进入手机完成启动、切换和查看。由此确定了项目边界：核心操作应离开手机，复杂设置仍可保留在 App。",
          en: "Early research compared digital focus tools, desk timers, and companion devices. They can manage tasks, but often send the user back to a phone to start, switch, or review a session. This set the boundary: core actions should leave the phone, while complex settings can remain in the app.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-brief.jpg", alt: { zh: "倾注项目背景和产品定位", en: "Qingzhu project context and product positioning" }, caption: { zh: "项目背景、案例范围与产品定位", en: "Context, case scope, and product position" } },
        ],
      },
      {
        id: "context-experience",
        label: { zh: "02 · 场景与体验", en: "02 · Context & experience" },
        title: { zh: "问题集中在开始、恢复与查看三个时刻", en: "The friction sits in starting, resuming, and checking" },
        body: {
          zh: "使用情境与人物画像把专注过程拆成开始任务、被打断后恢复和查看进度。三个时刻都需要快速确认，但不需要完整菜单，因此桌面设备应承担低频选择之外的即时动作。",
          en: "Scenarios and personas separated the focus process into starting a task, resuming after interruption, and checking progress. Each moment needs quick confirmation rather than a full menu, so the desktop device should handle immediate actions.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-research.jpg", alt: { zh: "倾注市场研究和人物画像", en: "Qingzhu market research and personas" }, caption: { zh: "使用情境、人物画像与任务时刻", en: "Scenarios, personas, and task moments" } },
        ],
      },
      {
        id: "interviews-analysis",
        label: { zh: "03 · 访谈与分析", en: "03 · Interviews & analysis" },
        title: { zh: "现有证据用于定义方向，还不足以验证需求", en: "The evidence frames a direction but does not validate demand" },
        body: {
          zh: "作品集记录了案例比较、情境分析和人物画像，但没有可复核的访谈样本、问卷统计或任务数据。因此这些材料只能支持初步判断，不能证明拍打交互更有效。",
          en: "The portfolio documents case comparison, scenario analysis, and personas, but not reproducible interview samples, survey statistics, or task data. These materials support an initial direction; they do not prove that tapping is more effective.",
        },
        details: {
          zh: ["后续访谈应围绕中断恢复、手机依赖和实体输入接受度展开；问卷只用于观察分布，不替代任务测试。"],
          en: ["Later interviews should examine interruption recovery, phone dependence, and acceptance of physical input. A survey can show distributions but cannot replace task testing."],
        },
        gallery: [
          { src: "/images/projects/qingzhu-design-goals.jpg", alt: { zh: "倾注的研究整理和设计目标", en: "Qingzhu research synthesis and design goals" }, caption: { zh: "现有材料形成的初步目标，不是验证结果", en: "Preliminary goals derived from existing material, not validated findings" } },
        ],
      },
      {
        id: "insights-question",
        label: { zh: "04 · 洞察与问题", en: "04 · Insights & questions" },
        title: { zh: "研究问题从“更多功能”转向“更直接的开始”", en: "The question shifted from more features to a more direct start" },
        body: {
          zh: "综合现有材料后，项目不再增加管理功能，而是集中回答：开始专注能否像拍下一只开关一样直接，同时让用户清楚知道动作是否生效？这一问题导出拍倒启动、旋钮切换、即时反馈和端间分工四项判断。",
          en: "The synthesis moved the project away from adding management features. The question became: can a focus session start as directly as striking a switch while making system state clear? This led to tap-to-start, dial selection, immediate feedback, and a division between device and app.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-interaction.jpg", alt: { zh: "倾注的拍打、触摸和旋钮交互", en: "Tapping, touch, and dial interactions for Qingzhu" }, caption: { zh: "研究问题对应的实体输入词汇", en: "Physical inputs linked to the research question" } },
        ],
      },
      {
        id: "concepts-prototypes",
        label: { zh: "05 · 构思与原型", en: "05 · Concepts & prototypes" },
        title: { zh: "设备处理即时动作，App 处理设置与复盘", en: "The device handles action; the app handles configuration" },
        body: {
          zh: "设备以拍打、旋钮和屏幕完成启动、切换与确认。白名单、专注模式和历史数据放在手机端。这个分工减少了桌面端菜单，也建立了反馈层级：设备先确认动作，App 再提供完整信息。",
          en: "Tapping, the dial, and the device screen handle starting, switching, and confirmation. Whitelists, modes, and history remain on the phone. This reduces device menus and creates a feedback hierarchy: the device confirms the action first; the app provides full information.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-system.jpg", alt: { zh: "倾注硬件和手机端的系统关系", en: "System relationship between Qingzhu hardware and mobile app" }, caption: { zh: "硬件、屏幕反馈与 App 的职责分工", en: "Responsibilities across hardware, screen, and app" } },
          { src: "/images/projects/qingzhu-app.jpg", alt: { zh: "倾注手机端流程", en: "Qingzhu mobile flow" }, caption: { zh: "模式设置、同步与数据查看", en: "Mode setup, synchronization, and review" } },
        ],
      },
      {
        id: "testing-feedback",
        label: { zh: "06 · 测试与反馈", en: "06 · Testing & feedback" },
        title: { zh: "当前检查集中在界面一致性和桌面尺度", en: "Current checks focus on interface consistency and desk scale" },
        body: {
          zh: "现阶段通过界面状态、产品比例和场景渲染检查系统是否自洽，但尚未完成目标用户的原型任务测试。因而不能判断拍打输入的学习成本、误触率或长期接受度。",
          en: "Current checks use interface states, product proportion, and scenario renders to examine internal consistency. No task-based user test has been completed, so learnability, false activation, and long-term acceptance remain unknown.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-design-system.jpg", alt: { zh: "倾注界面设计系统", en: "Qingzhu interface design system" }, caption: { zh: "界面状态与反馈一致性检查", en: "Interface state and feedback consistency" } },
          { src: "/images/projects/qingzhu-render.jpg", alt: { zh: "倾注产品渲染", en: "Qingzhu product render" }, caption: { zh: "形态、屏幕角度与桌面尺度检查", en: "Form, screen angle, and desk scale check" } },
        ],
      },
      {
        id: "refinement-conclusion",
        label: { zh: "07 · 优化与结论", en: "07 · Refinement & conclusion" },
        title: { zh: "概念成立，核心交互仍待真实任务验证", en: "The concept is coherent; the core interaction remains untested" },
        body: {
          zh: "当前方案明确了桌面设备与 App 的关系，也形成了可识别的产品语言。下一步不是继续修饰外形，而是制作可重复测试的工作样机，比较拍打与常规按键在首次学习、误触和中断恢复上的差异。",
          en: "The proposal defines the relationship between the desk device and the app and establishes a recognizable product language. The next step is not more styling, but a repeatable working prototype comparing tapping with a conventional button for first-time learning, false activation, and interruption recovery.",
        },
        gallery: [
          { src: "/images/projects/qingzhu-scenarios.jpg", alt: { zh: "倾注使用场景", en: "Qingzhu use scenarios" }, caption: { zh: "当前方案在工作与学习场景中的位置", en: "The current proposal in work and study settings" } },
        ],
      },
    ],
    tags: {
      zh: ["人机交互", "智能硬件", "交互原型"],
      en: ["HCI", "Smart hardware", "Prototyping"],
    },
    cover: "/images/projects/qingzhu-cover.jpg",
    theme: "apricot",
  },
  {
    slug: "co-evo",
    status: "published",
    featuredRank: 2,
    year: "2025",
    title: {
      zh: "CO-EVO：身体姿态与 AI 视觉交互",
      en: "CO-EVO: Body-as-Letter AI Interaction",
    },
    shortTitle: { zh: "CO-EVO", en: "CO-EVO" },
    subtitle: {
      zh: "观众用身体拼出字母，AI 识别后触发现场视觉。",
      en: "Visitors form letters with their bodies; AI recognition triggers live visuals.",
    },
    summary: {
      zh: "CO-EVO 是一件现场互动作品。团队定义 G、A、F 三种身体姿态，建立数据集并训练识别模型，再把结果送入 TouchDesigner。",
      en: "CO-EVO is a live interactive work. The team defined three body poses, built a dataset, trained a recognition model, and sent its output into TouchDesigner.",
    },
    role: { zh: "AI 核心成员", en: "AI core team member" },
    question: {
      zh: "没有控制器时，观众怎样知道自己的身体已被系统看见和识别？",
      en: "Without a controller, how does a visitor know that the system has seen and recognized their body?",
    },
    contributions: {
      zh: ["参与定义 G、A、F 三种身体姿态", "采集、标注并增强训练图像", "调整 YOLO 训练参数，检查 loss 与过拟合", "参与 TouchDesigner 视觉反馈和现场搭建"],
      en: ["Co-defined the G, A, and F body poses", "Captured, labeled, and augmented training images", "Tuned YOLO training and checked loss and overfitting", "Supported TouchDesigner feedback and on-site setup"],
    },
    sections: [
      {
        id: "literature-cases",
        label: { zh: "01 · 文献与案例", en: "01 · Literature & cases" },
        title: { zh: "身体交互案例把动作同时视为表达与输入", en: "Embodied interaction treats movement as expression and input" },
        body: {
          zh: "前期参考聚焦身体姿态、实时视觉和参与式展演。案例说明，现场互动不能只追求识别成功；观众还需要理解该做什么、系统看见了什么，以及动作如何改变画面。",
          en: "Early references focused on body poses, real-time visuals, and participatory performance. They showed that recognition alone is insufficient: visitors also need to understand what to do, what the system sees, and how movement changes the image.",
        },
        gallery: [
          { src: "/images/projects/co-evo-brief.jpg", alt: { zh: "CO-EVO 项目概念与贡献", en: "CO-EVO concept and contributions" }, caption: { zh: "项目概念、角色与工作范围", en: "Concept, role, and scope" } },
          { src: "/images/projects/co-evo-demo.jpg", alt: { zh: "CO-EVO 视觉参考和互动演示", en: "CO-EVO visual references and interaction demo" }, caption: { zh: "视觉参考与反馈方向", en: "Visual references and feedback direction" } },
        ],
      },
      {
        id: "context-experience",
        label: { zh: "02 · 场景与体验", en: "02 · Context & experience" },
        title: { zh: "户外场地改变了识别与反馈条件", en: "The outdoor site changed recognition and feedback conditions" },
        body: {
          zh: "互动发生在户外展演空间。观众与摄像头的距离、背景人流、光照和屏幕位置都会影响识别，也影响观众能否把自己的动作与视觉变化联系起来。场地规划因此先明确摄像头、屏幕和参与区域。",
          en: "The interaction takes place in an outdoor performance space. Camera distance, background movement, lighting, and screen position affect recognition and whether visitors connect their movement with visual change. Site planning therefore defined camera, screen, and participation zones first.",
        },
        gallery: [
          { src: "/images/projects/co-evo-installation-plan.jpg", alt: { zh: "CO-EVO 场地布置与互动规划", en: "CO-EVO site and interaction plan" }, caption: { zh: "屏幕、摄像头与观众区域规划", en: "Screen, camera, and visitor zones" } },
          { src: "/images/projects/co-evo-onsite-a.jpg", alt: { zh: "CO-EVO 现场搭建过程", en: "CO-EVO on-site setup" }, caption: { zh: "现场搭建与设备位置校正", en: "On-site setup and equipment positioning" } },
        ],
      },
      {
        id: "interviews-analysis",
        label: { zh: "03 · 访谈与分析", en: "03 · Interviews & analysis" },
        title: { zh: "参与者差异通过图像采集进入分析", en: "Participant variation entered the analysis through image capture" },
        body: {
          zh: "项目没有记录正式访谈或问卷统计。与参与者相关的证据主要来自不同人物、距离、角度和背景下的姿态图像。标注与增强扩大了变化范围，也暴露了部分姿态边界不够清楚的问题。",
          en: "The project does not document formal interviews or survey statistics. Participant evidence comes mainly from pose images across people, distances, angles, and backgrounds. Labeling and augmentation expanded variation and exposed ambiguous pose boundaries.",
        },
        gallery: [
          { src: "/images/projects/co-evo-dataset.jpg", alt: { zh: "CO-EVO 数据采集、标注和增强", en: "CO-EVO capture, labeling, and augmentation" }, caption: { zh: "参与者变化、原始图像、标注与增强", en: "Participant variation, raw images, labels, and augmentation" } },
        ],
      },
      {
        id: "insights-question",
        label: { zh: "04 · 洞察与问题", en: "04 · Insights & questions" },
        title: { zh: "动作设计、模型分类与系统反馈必须一起定义", en: "Movement, model classes, and feedback must be defined together" },
        body: {
          zh: "G、A、F 三种姿态既要容易记住和完成，也要在轮廓上彼此可分。由此形成研究问题：没有控制器时，观众怎样知道自己已被系统看见、当前姿态是否接近目标，以及该如何修正？",
          en: "The G, A, and F poses must be memorable and achievable while remaining visually distinct. This produced the research question: without a controller, how does a visitor know they have been seen, whether a pose is close to the target, and how to correct it?",
        },
        gallery: [
          { src: "/images/projects/co-evo-system.jpg", alt: { zh: "CO-EVO 姿态和识别路线", en: "CO-EVO poses and recognition pipeline" }, caption: { zh: "G、A、F 姿态与摄像头到视觉反馈的链路", en: "G, A, F poses and the camera-to-feedback pipeline" } },
        ],
      },
      {
        id: "concepts-prototypes",
        label: { zh: "05 · 构思与原型", en: "05 · Concepts & prototypes" },
        title: { zh: "从姿态词汇到实时识别原型", en: "From a pose vocabulary to a real-time recognition prototype" },
        body: {
          zh: "团队先定义三类姿态，再采集和标注数据，训练 YOLO 模型，并把识别结果映射到 TouchDesigner。原型链路把动作设计、模型输出和现场视觉放在同一系统中检查。",
          en: "The team defined three poses, captured and labeled data, trained a YOLO model, and mapped recognition output into TouchDesigner. The prototype pipeline placed movement design, model output, and live visuals in one system.",
        },
        gallery: [
          { src: "/images/projects/co-evo-training.jpg", alt: { zh: "CO-EVO 模型训练设置", en: "CO-EVO model training setup" }, caption: { zh: "训练配置与原型链路记录", en: "Training setup and prototype pipeline notes" } },
        ],
      },
      {
        id: "testing-feedback",
        label: { zh: "06 · 测试与反馈", en: "06 · Testing & feedback" },
        title: { zh: "模型学会三类姿态，不等于现场已经稳定", en: "Learning three poses does not establish live stability" },
        body: {
          zh: "训练曲线和识别样例用于检查收敛与过拟合。现有结果说明模型能够区分三类姿态，但不足以证明它在不同光照、复杂背景、多人进入或距离变化下稳定，也没有系统记录观众是否理解反馈。",
          en: "Training curves and recognition examples were used to inspect convergence and overfitting. The results show that the model can distinguish three poses, but do not establish stability across lighting, complex backgrounds, multiple people, or distance changes. Visitor understanding was not systematically recorded.",
        },
        gallery: [
          { src: "/images/projects/co-evo-evaluation.jpg", alt: { zh: "CO-EVO 训练曲线和结果观察", en: "CO-EVO training curves and result observations" }, caption: { zh: "loss、过拟合与识别样例检查", en: "Loss, overfitting, and recognition checks" } },
        ],
      },
      {
        id: "refinement-conclusion",
        label: { zh: "07 · 优化与结论", en: "07 · Refinement & conclusion" },
        title: { zh: "现场落地完成，下一轮需要同时记录技术与行为", en: "The installation worked; the next study must pair technical and behavioral evidence" },
        body: {
          zh: "系统最终进入户外展演空间，完成了身体输入、模型识别和视觉反馈的现场链路。后续优化应同时记录数据划分、易混淆姿态、反馈延迟，以及观众是否知道如何进入、保持和修正动作。",
          en: "The system reached the outdoor performance site with body input, model recognition, and visual feedback connected. The next iteration should record dataset splits, confused pose pairs, feedback latency, and whether visitors understand how to enter, hold, and correct a pose.",
        },
        gallery: [
          { src: "/images/projects/co-evo-onsite.jpg", alt: { zh: "CO-EVO 户外现场互动", en: "CO-EVO outdoor interaction" }, caption: { zh: "户外展演中的最终状态", en: "Final state in the outdoor performance" } },
        ],
      },
    ],
    tags: {
      zh: ["AI 视觉", "身体交互", "现场装置"],
      en: ["AI vision", "Embodied interaction", "Installation"],
    },
    cover: "/images/projects/co-evo-cover.jpg",
    theme: "lavender",
  },
  {
    slug: "bingbing",
    status: "published",
    featuredRank: 3,
    year: "2026",
    title: {
      zh: "冰冰：家用两用制冰机改良",
      en: "Bingbing: A Dual-use Ice Maker Redesign",
    },
    shortTitle: { zh: "冰冰", en: "Bingbing" },
    subtitle: {
      zh: "从使用问题和拆机结果出发，重做家用制冰机。",
      en: "A household ice maker redesigned from use problems and teardown findings.",
    },
    summary: {
      zh: "冰冰从用户旅程进入产品内部。团队先整理取冰、清洁和操作问题，再通过拆机确认结构限制，最后完成机构、外形与 CMF 方案。",
      en: "Bingbing moves from the user journey into the product interior. The team mapped dispensing, cleaning, and control problems, used a teardown to locate structural constraints, then developed the mechanism, form, and CMF.",
    },
    role: { zh: "负责人", en: "Project lead" },
    question: {
      zh: "用户研究发现的问题，怎样真正进入制冰机的内部结构和操作顺序？",
      en: "How can findings from user research change the internal structure and task sequence of an ice maker?",
    },
    contributions: {
      zh: ["组织市场资料与竞品比较", "参与问卷、访谈、画像和用户旅程", "拆机并梳理冷凝、水箱、储冰和控制模块", "推进多轮草模、结构方案、渲染与 CMF"],
      en: ["Led market and competitor review", "Worked on surveys, interviews, personas, and journey mapping", "Mapped cooling, tank, storage, and control modules through teardown", "Developed models, structural options, renders, and CMF across iterations"],
    },
    sections: [
      {
        id: "literature-cases",
        label: { zh: "01 · 文献与案例", en: "01 · Literature & cases" },
        title: { zh: "市场比较先确定产品类型与改良边界", en: "Market comparison set the product type and redesign boundary" },
        body: {
          zh: "桌面调研比较了家用制冰机的类型、容量、出冰方式、清洁功能和控制布局。结果没有直接给出方案，而是先明确哪些问题来自行业共性，哪些可能通过单台产品的结构调整解决。",
          en: "Desk research compared household ice makers by type, capacity, dispensing method, cleaning features, and control layout. It did not produce a solution directly; it separated common market limitations from issues that one product redesign could address.",
        },
        gallery: [
          { src: "/images/projects/bingbing-market.jpg", alt: { zh: "家用制冰机市场资料", en: "Household ice maker market material" }, caption: { zh: "市场类型与使用情境", en: "Market types and use contexts" } },
          { src: "/images/projects/bingbing-competitors.jpg", alt: { zh: "家用制冰机竞品比较", en: "Household ice maker competitor comparison" }, caption: { zh: "竞品功能、结构与体验比较", en: "Feature, structure, and experience comparison" } },
        ],
      },
      {
        id: "context-experience",
        label: { zh: "02 · 场景与体验", en: "02 · Context & experience" },
        title: { zh: "把一次制冰任务拆成准备、等待、取冰与清洁", en: "The task was separated into preparation, waiting, dispensing, and cleaning" },
        body: {
          zh: "用户旅程把家用场景中的操作按时间展开。问题并不只发生在取冰口：加水是否方便、等待状态是否清楚、冰块如何取出，以及使用后怎样清洁，共同决定完整体验。",
          en: "The user journey placed household actions on a timeline. The problem was not limited to dispensing: filling, understanding the wait, removing ice, and cleaning after use jointly shaped the experience.",
        },
        gallery: [
          { src: "/images/projects/bingbing-journey.jpg", alt: { zh: "冰冰用户旅程与人物画像", en: "Bingbing journey map and persona" }, caption: { zh: "用户旅程、任务顺序与体验断点", en: "Journey, task order, and experience breakdowns" } },
        ],
      },
      {
        id: "interviews-analysis",
        label: { zh: "03 · 访谈与分析", en: "03 · Interviews & analysis" },
        title: { zh: "用户材料与拆机结果共同约束方案", en: "User evidence and teardown findings constrained the design together" },
        body: {
          zh: "问卷、访谈和问题整理指向出冰方式、维护、等待感与控制信息。拆机则确认冷凝管、水箱、储冰区、压缩机和控制模块的空间关系。两类材料交叉后，体验诉求才被转换为可讨论的内部结构条件。",
          en: "Surveys, interviews, and problem mapping pointed to dispensing, maintenance, waiting, and control information. The teardown located cooling tubes, tank, storage, compressor, and controls. Crossing these two evidence sources turned experience needs into structural conditions.",
        },
        details: {
          zh: ["作品集未提供足够信息复核样本规模和统计方法，因此这里只陈述材料指向，不声称总体比例或显著差异。"],
          en: ["The portfolio does not provide enough information to verify sample size or statistical methods, so the case reports directions in the material rather than population estimates or significant differences."],
        },
        gallery: [
          { src: "/images/projects/bingbing-field-study.jpg", alt: { zh: "冰冰问卷和访谈材料", en: "Bingbing survey and interview material" }, caption: { zh: "问卷、访谈与问题整理", en: "Survey, interviews, and problem mapping" } },
          { src: "/images/projects/bingbing-teardown.jpg", alt: { zh: "家用制冰机拆机与部件标注", en: "Ice maker teardown and component labels" }, caption: { zh: "拆机、部件识别与空间关系", en: "Teardown, component identification, and spatial relationships" } },
        ],
      },
      {
        id: "insights-question",
        label: { zh: "04 · 洞察与问题", en: "04 · Insights & questions" },
        title: { zh: "研究问题必须同时落到任务顺序和内部机构", en: "The research question had to connect task order with internal mechanisms" },
        body: {
          zh: "综合分析后，核心问题被表述为：用户研究发现的问题，怎样进入制冰机的内部结构和操作顺序？由此形成五项判断：分离式冷却、碎冰、抽屉取冰、紫外消毒和更直接的控制。每项判断都对应一个任务断点。",
          en: "The synthesis produced one question: how can user research change the internal structure and task sequence of an ice maker? Five decisions followed: separated cooling, ice crushing, drawer dispensing, UV disinfection, and clearer controls. Each maps to a task breakdown.",
        },
        gallery: [
          { src: "/images/projects/bingbing-design.jpg", alt: { zh: "冰冰主要设计点", en: "Main Bingbing design decisions" }, caption: { zh: "结构与交互改良概览", en: "Structural and interaction changes" } },
          { src: "/images/projects/bingbing-design-details.jpg", alt: { zh: "冰冰补充设计细节", en: "Additional Bingbing design details" }, caption: { zh: "消毒、取冰与控制细节", en: "Disinfection, dispensing, and control details" } },
        ],
      },
      {
        id: "concepts-prototypes",
        label: { zh: "05 · 构思与原型", en: "05 · Concepts & prototypes" },
        title: { zh: "草图与模型用于同时比较体积、结构和手部空间", en: "Sketches and models compared volume, structure, and hand clearance" },
        body: {
          zh: "多轮方案改变开口、取冰方向、体块和模块位置。草模排除了不合理比例，检查手是否能完成加水、取冰与清洁；结构草图继续推演新增机构对水路、隔热和内部体积的影响。",
          en: "Iterations changed openings, dispensing direction, overall volume, and module positions. Study models removed awkward proportions and checked hand clearance for filling, dispensing, and cleaning. Structural sketches examined effects on water routing, insulation, and internal volume.",
        },
        gallery: [
          { src: "/images/projects/bingbing-concepts.jpg", alt: { zh: "冰冰早期概念方案", en: "Early Bingbing concepts" }, caption: { zh: "功能布局与形态方向", en: "Functional layouts and form directions" } },
          { src: "/images/projects/bingbing-models.jpg", alt: { zh: "冰冰草模和比例推演", en: "Bingbing study models and proportion tests" }, caption: { zh: "草模、比例与操作空间", en: "Study models, proportion, and hand clearance" } },
          { src: "/images/projects/bingbing-sketches.jpg", alt: { zh: "冰冰设计草图", en: "Bingbing design sketches" }, caption: { zh: "外形与结构推演", en: "Form and structure studies" } },
        ],
      },
      {
        id: "testing-feedback",
        label: { zh: "06 · 测试与反馈", en: "06 · Testing & feedback" },
        title: { zh: "当前验证确认了操作逻辑，尚未确认真实任务表现", en: "Current checks confirm the interaction logic, not real task performance" },
        body: {
          zh: "操作流程检查了加水、制冰、取冰和维护是否形成连续顺序，模型也用于检查比例与可达性。但项目尚未用工作样机完成制冰、碎冰和清洁任务，因此不能判断耗时、错误率或维护负担是否改善。",
          en: "The interaction flow checked whether filling, ice making, dispensing, and maintenance form a continuous sequence. Models checked proportion and reach. No working prototype completed ice-making, crushing, or cleaning tasks, so time, errors, and maintenance burden remain unknown.",
        },
        gallery: [
          { src: "/images/projects/bingbing-interaction.jpg", alt: { zh: "冰冰产品操作流程", en: "Bingbing product interaction flow" }, caption: { zh: "加水、制冰、取冰与维护的流程检查", en: "Flow check for filling, making, dispensing, and maintenance" } },
        ],
      },
      {
        id: "refinement-conclusion",
        label: { zh: "07 · 优化与结论", en: "07 · Refinement & conclusion" },
        title: { zh: "方案完成结构闭环，工程效果仍需样机确认", en: "The proposal closes the structural loop; engineering performance remains unverified" },
        body: {
          zh: "最终方案以明确的上部控制区和下部取冰区组织操作，并用爆炸图说明模块关系。结论是研究已经进入结构层，但还没有形成工程证据。下一步应制作制冰与碎冰样机，用清洁任务、完成时间和操作错误检验改良。",
          en: "The final proposal organizes an upper control zone and lower dispensing zone, with an exploded view explaining module relationships. Research reached the structural level but did not yet produce engineering evidence. A working ice-making and crushing prototype should test cleaning, completion time, and operating errors.",
        },
        gallery: [
          { src: "/images/projects/bingbing-render-a.jpg", alt: { zh: "冰冰产品渲染正面", en: "Bingbing front product render" }, caption: { zh: "最终外形与操作分区", en: "Final form and control zones" } },
          { src: "/images/projects/bingbing-render-b.jpg", alt: { zh: "冰冰产品细节渲染", en: "Bingbing detail render" }, caption: { zh: "取冰口与材质细节", en: "Dispensing and material details" } },
          { src: "/images/projects/bingbing-exploded.jpg", alt: { zh: "冰冰最终结构爆炸图", en: "Bingbing final exploded view" }, caption: { zh: "最终方案的模块关系", en: "Module relationships in the final proposal" } },
        ],
      },
    ],
    tags: {
      zh: ["用户研究", "产品设计", "结构分析"],
      en: ["User research", "Product design", "Structure"],
    },
    cover: "/images/projects/bingbing-cover.jpg",
    theme: "ice",
  },
  {
    slug: "hive-wings",
    status: "published",
    featuredRank: 4,
    year: "2025",
    title: {
      zh: "蜂巢之翼：多叶片可变形开合窗",
      en: "Wings of the Hive: A Kinetic Window",
    },
    shortTitle: { zh: "蜂巢之翼", en: "Wings of the Hive" },
    subtitle: {
      zh: "一组由舵机驱动、可以旋转和展开的动态叶片。",
      en: "A servo-driven array of panels that rotate and unfold.",
    },
    summary: {
      zh: "蜂巢之翼从虹膜、折纸和蜂窝阵列寻找开合方式，再用单元模型、连杆和舵机逐步解决同步、干涉与装配问题。",
      en: "Wings of the Hive draws opening actions from irises, origami, and honeycomb arrays, then works through synchronization, collision, and assembly with unit models, linkages, and servos.",
    },
    role: { zh: "负责人", en: "Project lead" },
    question: {
      zh: "一组叶片怎样稳定地一起开合，同时避免彼此碰撞？",
      en: "How can a set of panels open together without colliding?",
    },
    contributions: {
      zh: ["负责概念、结构和三维建模", "推演叶片折叠、连杆与驱动关系", "完成多轮单体和阵列测试", "制作、装配并调试实体原型"],
      en: ["Led concept, structure, and 3D modeling", "Developed panel folding, linkage, and actuation", "Tested units and arrays across iterations", "Fabricated, assembled, and tuned the physical prototype"],
    },
    sections: [
      {
        id: "literature-cases",
        label: { zh: "01 · 文献与案例", en: "01 · Literature & cases" },
        title: { zh: "虹膜、折纸与蜂窝提供三类运动线索", en: "Irises, origami, and honeycombs offered three movement cues" },
        body: {
          zh: "案例调研没有直接复制自然形态，而是拆出可用于机构设计的关系：虹膜对应旋转收放，折纸对应面与折线，蜂窝对应可重复阵列。三类线索共同限定了动态叶片的构思范围。",
          en: "The review did not copy natural forms directly. It extracted relationships useful for mechanism design: radial motion from the iris, surface-and-fold logic from origami, and repeatable arrays from honeycombs. Together they bounded the concept space.",
        },
        gallery: [
          { src: "/images/projects/hive-brief.jpg", alt: { zh: "蜂巢之翼项目背景", en: "Wings of the Hive project context" }, caption: { zh: "项目目标与原型范围", en: "Project goal and prototype scope" } },
          { src: "/images/projects/hive-concept.jpg", alt: { zh: "蜂巢、虹膜与折纸概念来源", en: "Honeycomb, iris, and origami references" }, caption: { zh: "形态来源与运动线索", en: "Form references and movement cues" } },
        ],
      },
      {
        id: "context-experience",
        label: { zh: "02 · 场景与体验", en: "02 · Context & experience" },
        title: { zh: "动态表皮需要同时处理开口、遮挡与视觉变化", en: "A kinetic surface must balance opening, shading, and visual change" },
        body: {
          zh: "概念场景把叶片视为建筑表皮单元，需要在闭合和展开之间改变开口面积，同时保持阵列连续。项目未开展真实建筑场地调研，因此通风、遮光和尺度表现仍是设计假设，而非环境验证结果。",
          en: "The concept treats each panel as an architectural-surface unit whose opening area changes while the array remains continuous. No real building-site study was conducted, so ventilation, shading, and scale remain design assumptions rather than environmental findings.",
        },
        gallery: [
          { src: "/images/projects/hive-rendering.jpg", alt: { zh: "蜂巢之翼概念渲染", en: "Wings of the Hive concept render" }, caption: { zh: "动态表皮的概念场景与尺度假设", en: "Concept setting and scale assumptions" } },
        ],
      },
      {
        id: "interviews-analysis",
        label: { zh: "03 · 访谈与分析", en: "03 · Interviews & analysis" },
        title: { zh: "这个项目以结构分析替代用户统计", en: "This project relies on structural analysis rather than user statistics" },
        body: {
          zh: "作品集没有访谈、问卷或统计材料。分析对象是叶片、固定件、连杆、齿轮、舵机与支撑之间的关系。部件拆解用于检查转轴位置、连杆长度、装配顺序和运动边界。",
          en: "The portfolio contains no interviews, surveys, or statistical material. Analysis instead focused on panels, fixtures, linkages, gears, servos, and supports. Component decomposition examined pivots, linkage length, assembly order, and movement limits.",
        },
        gallery: [
          { src: "/images/projects/hive-structure.jpg", alt: { zh: "蜂巢之翼结构拆解", en: "Wings of the Hive structural decomposition" }, caption: { zh: "主体结构、驱动部件与运动边界", en: "Primary structure, actuation, and movement limits" } },
          { src: "/images/projects/hive-assembly.jpg", alt: { zh: "蜂巢之翼装配关系", en: "Wings of the Hive assembly relationships" }, caption: { zh: "单元装配与连接顺序", en: "Unit assembly and connection order" } },
        ],
      },
      {
        id: "insights-question",
        label: { zh: "04 · 洞察与问题", en: "04 · Insights & questions" },
        title: { zh: "核心矛盾是联动、干涉与可制作性", en: "The central conflict is linkage, collision, and buildability" },
        body: {
          zh: "早期分析说明，叶片能否展开并不是唯一标准。多个单元还要同步运动、避免相互碰撞，并能用现有材料和加工方式装配。因此研究问题被收敛为：一组叶片怎样稳定地一起开合，同时避免彼此干涉？",
          en: "Early analysis showed that opening alone was not enough. Multiple units also had to move together, avoid collision, and remain buildable with available materials and fabrication. The question became: how can a set of panels open together without interfering with one another?",
        },
        gallery: [
          { src: "/images/projects/hive-iteration-a.jpg", alt: { zh: "蜂巢之翼第一轮结构迭代", en: "Wings of the Hive first structural iteration" }, caption: { zh: "早期方案暴露的联动与干涉问题", en: "Linkage and collision issues in an early concept" } },
        ],
      },
      {
        id: "concepts-prototypes",
        label: { zh: "05 · 构思与原型", en: "05 · Concepts & prototypes" },
        title: { zh: "方案从蜂窝阵列收敛到三叉星簇", en: "The design converged from a honeycomb array to a three-branch cluster" },
        body: {
          zh: "多轮原型分别调整折面、支点、连杆与阵列方式。每一轮只处理一个主要冲突，并保留被放弃的方案作为比较证据。最终选择三叉星簇，因为它更适合联动和空间展开。",
          en: "Successive prototypes changed surfaces, pivots, linkages, and array logic. Each iteration isolated one main conflict, while discarded options remained as comparative evidence. The final three-branch cluster better supported linkage and spatial expansion.",
        },
        gallery: [
          { src: "/images/projects/hive-iteration-b.jpg", alt: { zh: "蜂巢之翼第二轮结构迭代", en: "Wings of the Hive second structural iteration" }, caption: { zh: "支点与连接方式调整", en: "Pivot and connection changes" } },
          { src: "/images/projects/hive-iteration-c.jpg", alt: { zh: "蜂巢之翼第三轮结构迭代", en: "Wings of the Hive third structural iteration" }, caption: { zh: "联动与空间展开测试", en: "Linkage and spatial expansion test" } },
          { src: "/images/projects/hive-iteration-d.jpg", alt: { zh: "蜂巢之翼第四轮结构迭代", en: "Wings of the Hive fourth structural iteration" }, caption: { zh: "单元关系进一步收敛", en: "Further convergence of the unit" } },
          { src: "/images/projects/hive-iteration.jpg", alt: { zh: "蜂巢之翼最终三叉星簇", en: "Final three-branch cluster" }, caption: { zh: "最终单元与阵列", en: "Final unit and array" } },
        ],
      },
      {
        id: "testing-feedback",
        label: { zh: "06 · 测试与反馈", en: "06 · Testing & feedback" },
        title: { zh: "动作分解与实体制作共同检查机构", en: "Motion studies and fabrication tested the mechanism together" },
        body: {
          zh: "动作分解检查闭合、旋转、顶出和展开各阶段的干涉；实体制作进一步暴露材料厚度、舵机位置、连杆长度和装配公差。反馈直接进入下一轮结构调整，但尚未形成循环寿命、噪声或同步误差的量化记录。",
          en: "Motion studies checked collision during closing, rotation, extension, and opening. Fabrication then exposed material thickness, servo placement, linkage length, and assembly tolerances. Findings informed structural changes, but cycle life, noise, and synchronization error were not quantified.",
        },
        gallery: [
          { src: "/images/projects/hive-action-a.jpg", alt: { zh: "蜂巢之翼开合动作前半段", en: "First half of Wings of the Hive opening sequence" }, caption: { zh: "闭合、旋转与顶出检查", en: "Closed, rotating, and extending checks" } },
          { src: "/images/projects/hive-action-b.jpg", alt: { zh: "蜂巢之翼开合动作后半段", en: "Second half of Wings of the Hive opening sequence" }, caption: { zh: "展开与最终状态检查", en: "Opening and final-state checks" } },
          { src: "/images/projects/hive-fabrication.jpg", alt: { zh: "蜂巢之翼制作和调试", en: "Wings of the Hive fabrication and tuning" }, caption: { zh: "切割、装配与机构调试", en: "Cutting, assembly, and mechanism tuning" } },
        ],
      },
      {
        id: "refinement-conclusion",
        label: { zh: "07 · 优化与结论", en: "07 · Refinement & conclusion" },
        title: { zh: "原型完成基本开合，建筑尺度结论仍然有限", en: "The prototype opens; conclusions at architectural scale remain limited" },
        body: {
          zh: "最终实体原型说明这套开合关系可以工作，但不能据此直接推断建筑尺度的可靠性。下一阶段应先测量单元同步误差、噪声、承载和循环寿命，再决定是否加入环境传感和更大规模阵列。",
          en: "The final prototype shows that the opening relationship can work, but it does not establish reliability at architectural scale. The next stage should measure synchronization error, noise, load, and cycle life before adding environmental sensing or a larger array.",
        },
        gallery: [
          { src: "/images/projects/hive-final.jpg", alt: { zh: "蜂巢之翼最终实体原型", en: "Final Wings of the Hive prototype" }, caption: { zh: "最终实体模型与当前结论边界", en: "Final physical prototype and current limits" } },
        ],
      },
    ],
    tags: {
      zh: ["实体计算", "机构设计", "原型制作"],
      en: ["Physical computing", "Mechanism design", "Fabrication"],
    },
    cover: "/images/projects/hive-wings-cover.jpg",
    theme: "graphite",
  },
];

export function getPublishedProjects() {
  return projects
    .filter((project) => project.status === "published")
    .sort((a, b) => (a.featuredRank ?? 999) - (b.featuredRank ?? 999));
}

export function getFeaturedProjects() {
  return getPublishedProjects().filter((project) => project.featuredRank != null);
}

export function getProject(slug: string) {
  return projects.find(
    (project) => project.slug === slug && project.status === "published",
  );
}

export function localePath(locale: Locale, path = "") {
  const normalized = path === "/" ? "" : path;
  return locale === "en" ? `/en${normalized}` : normalized || "/";
}
