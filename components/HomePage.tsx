import {
  approachSteps,
  getFeaturedProjects,
  localePath,
  profile,
  researchQuestions,
  type Locale,
} from "@/content/site";
import { ProjectCard } from "./ProjectCard";
import { SiteHeader } from "./SiteHeader";
import { SiteFooter } from "./SiteFooter";

const copy = {
  zh: {
    workLabel: "项目档案",
    workTitle: "Selected Work",
    explore: "浏览项目",
    contact: "联系我",
    allWork: "查看全部项目",
    approachLabel: "工作方式",
    approachTitle: "我怎样推进一个项目",
    approachIntro: "这是一条常用路径。实际项目会在调研、原型与测试之间往返。",
    questionsLabel: "研究关注",
    questionsTitle: "Questions I’m exploring",
    aboutLabel: "个人档案",
    aboutTitle: "我想把研究做成可以触摸、操作和讨论的东西。",
    aboutBody: "这个网站既是作品集，也是我的项目档案。除了最终结果，我会保留研究材料、结构推演、训练过程和原型中的问题。",
    aboutLink: "关于我与经历",
  },
  en: {
    workLabel: "Project archive",
    workTitle: "Selected Work",
    explore: "Explore work",
    contact: "Get in touch",
    allWork: "View all projects",
    approachLabel: "Approach",
    approachTitle: "How I move a project forward",
    approachIntro: "This is a common path. In practice, a project moves back and forth between research, prototyping, and testing.",
    questionsLabel: "Research focus",
    questionsTitle: "Questions I’m exploring",
    aboutLabel: "Profile",
    aboutTitle: "I want research to become something people can touch, use, and discuss.",
    aboutBody: "This site is both a portfolio and a project archive. Alongside finished work, I keep the research material, structural studies, training process, and unresolved questions.",
    aboutLink: "About me and my experience",
  },
};

export function HomePage({ locale }: { locale: Locale }) {
  const projects = getFeaturedProjects();

  return (
    <div className="site-shell">
      <SiteHeader locale={locale} />
      <main>
        <section className="hero hero-with-portrait" aria-labelledby="hero-title">
          <div className="hero-heading">
            <h1 id="hero-title">{profile.headline[locale]}</h1>
          </div>
          <figure className="portrait-frame">
            <img src={profile.portrait} alt={locale === "en" ? "Portrait of Senpei Chen" : "陈森培肖像"} />
          </figure>
          <div className="hero-footer">
            <p className="hero-intro">{profile.intro[locale]}</p>
            <div className="hero-actions">
              <a className="button button-primary" href="#work">
                {copy[locale].explore}
              </a>
              <a className="button button-text" href={`mailto:${profile.email}`}>
                {copy[locale].contact}
              </a>
            </div>
          </div>
        </section>

        <section className="approach-section" aria-labelledby="approach-title">
          <div className="section-heading">
            <p className="section-kicker">{copy[locale].approachLabel}</p>
            <h2 id="approach-title">{copy[locale].approachTitle}</h2>
            <p>{copy[locale].approachIntro}</p>
          </div>
          <ol className="approach-grid">
            {approachSteps.map((step, index) => (
              <li key={step.title.en}>
                <span>{String(index + 1).padStart(2, "0")}</span>
                <h3>{step.title[locale]}</h3>
                <p>{step.body[locale]}</p>
              </li>
            ))}
          </ol>
        </section>

        <section className="work-section" id="work" aria-labelledby="work-title">
          <div className="section-heading">
            <p className="section-kicker">{copy[locale].workLabel}</p>
            <h2 id="work-title">{copy[locale].workTitle}</h2>
          </div>
          <div className="project-grid">
            {projects.map((project, index) => (
              <ProjectCard
                project={project}
                locale={locale}
                index={index}
                key={project.slug}
              />
            ))}
          </div>
          <div className="section-end-link">
            <a className="text-arrow-link" href={localePath(locale, "/work")}>
              {copy[locale].allWork}<span aria-hidden="true">↗</span>
            </a>
          </div>
        </section>

        <section className="questions-section" aria-labelledby="questions-title">
          <div className="section-heading section-heading-top">
            <p className="section-kicker">{copy[locale].questionsLabel}</p>
            <h2 id="questions-title">{copy[locale].questionsTitle}</h2>
          </div>
          <ol className="question-list">
            {researchQuestions.map((question, index) => (
              <li key={question.title.en}>
                <span>{String(index + 1).padStart(2, "0")}</span>
                <div>
                  <h3>{question.title[locale]}</h3>
                  <p>{question.body[locale]}</p>
                </div>
              </li>
            ))}
          </ol>
        </section>

        <section className="about-preview" aria-labelledby="about-preview-title">
          <div className="about-preview-copy">
            <p className="section-kicker">{copy[locale].aboutLabel}</p>
            <h2 id="about-preview-title">{copy[locale].aboutTitle}</h2>
            <p>{copy[locale].aboutBody}</p>
            <a className="text-arrow-link" href={localePath(locale, "/about")}>
              {copy[locale].aboutLink}<span aria-hidden="true">↗</span>
            </a>
          </div>
          <div className="academic-note" aria-label={locale === "en" ? "Current profile" : "当前信息"}>
            <span>GZARTS</span>
            <strong>2024—2028</strong>
            <p>{locale === "en" ? "Interaction Design undergraduate" : "智能交互设计本科"}</p>
          </div>
        </section>
      </main>
      <SiteFooter locale={locale} />
    </div>
  );
}
