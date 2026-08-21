# Senpei Chen Portfolio

陈森培（Senpei Chen）的中英文个人网站。内容以人机交互为主，包含智能硬件、AI 交互、产品设计、用户研究和实体原型项目。

## 页面

- `/`、`/en`：首页
- `/work`、`/en/work`：项目档案
- `/work/[slug]`、`/en/work/[slug]`：项目详情
- `/about`、`/en/about`：个人介绍、研究问题与经历
- `/documents`、`/en/documents`：CV 与完整作品集

## 本地运行

需要 Node.js 22.13 或更高版本。

```bash
npm install
npm run dev
```

浏览器打开 `http://localhost:3000/`。英文版位于 `http://localhost:3000/en`。

GitHub Pages 静态发布文件可以用以下命令生成到 `docs/`：

```bash
npm run export:static
```

## 内容在哪里

主要内容都在 [`content/site.ts`](content/site.ts)：

- `profile`：姓名、简介、头像、邮箱和资料链接
- `researchQuestions`：首页与 About 页的研究问题
- `approachSteps`：首页的工作方式
- `projects`：项目卡片和完整案例内容
- `timeline`、`capabilityGroups`：经历与能力

图片位于 `public/images/`。CV 和作品集位于 `public/files/`。

## 添加项目

1. 把图片放进 `public/images/projects/`。
2. 在 `content/site.ts` 的 `projects` 数组末尾加入一条项目记录。
3. 使用唯一的 `slug`，填写中英文内容、封面、标签和任意数量的 `sections`。
4. 每个 section 可以加入 `details` 和多张 `gallery` 图片。
5. 编辑时设为 `status: "draft"`；公开时改为 `"published"`。
6. 需要出现在首页时添加 `featuredRank`。

不需要复制页面文件。公开项目会自动生成中英文详情页。

更具体的数据结构说明见 [`content/README.md`](content/README.md)。案例写作规则见 [`design/content-narrative.md`](design/content-narrative.md)。

## 检查

```bash
npm run lint
npm test
```

## 资料来源

项目文字与图片整理自仓库中的 CV 和 56 页作品集。网页对内容做了重组，没有改动原始文件。
