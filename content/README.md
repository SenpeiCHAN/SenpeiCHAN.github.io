# Content editing guide

网站由 `content/site.ts` 生成。主页卡片、项目档案、中英文详情页和资料链接共用同一份数据。

## Project 字段

- `slug`：页面地址，必须唯一
- `status`：`draft`、`published` 或 `archived`
- `featuredRank`：首页排序；不填写则只进入项目档案
- `title`、`subtitle`、`summary`：卡片与详情页开头
- `question`：项目要回答的核心问题
- `contributions`：个人工作范围
- `sections`：案例正文，可自由增减
- `cover`、`theme`、`tags`：封面与视觉信息

## Section 字段

每个 section 有 `id`、`label`、`title` 和 `body`。还可以加入：

- `details`：补充判断或证据边界，按段落显示
- `gallery`：任意数量的图片；每张图有 `src`、`alt` 和可选 `caption`
- `image`：兼容旧内容的单图字段

项目页会自动排布 gallery。桌面端为双列，图片数量为奇数时第一张跨两列；移动端为单列。

## 添加和维护

1. 图片放在 `public/images/projects/`，使用小写英文和连字符命名。
2. 新项目先用 `status: "draft"`。
3. 中英文应表达同一事实，但不要求逐字翻译。
4. 不确定的数据、样本数或性能指标不要补写。
5. 研究材料、设计判断和验证结果要分开描述。
6. 每次内容调整记录在根目录 `CHANGELOG.md`。

新增案例时，按照 `design/content-narrative.md` 中的七步研究与设计流程组织 section。没有完成的方法需要说明证据缺口，不能省略阶段或补造结论。

头像路径由 `profile.portrait` 控制。邮箱由 `profile.email` 控制，并自动用于页头、页尾和资料页。
