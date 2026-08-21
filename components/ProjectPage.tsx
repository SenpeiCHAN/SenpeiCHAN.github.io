import {
  getPublishedProjects,
  localePath,
  type Locale,
  type Project,
} from "@/content/site";
import { SiteFooter } from "./SiteFooter";
import { SiteHeader } from "./SiteHeader";

const copy = {
  zh: {
    question: "研究问题",
    role: "角色",
    year: "年份",
    contribution: "我的贡献",
    next: "下一个项目",
    archive: "返回项目档案",
  },
  en: {
    question: "Research question",
    role: "Role",
    year: "Year",
    contribution: "My contribution",
    next: "Next project",
    archive: "Back to project archive",
  },
};

export function ProjectPage({ project, locale }: { project: Project; locale: Locale }) {
  const projects = getPublishedProjects();
  const index = projects.findIndex((item) => item.slug === project.slug);
  const nextProject = projects[(index + 1) % projects.length];
  const projectPath = `/work/${project.slug}`;

  return (
    <div className={`site-shell project-page theme-${project.theme}`}>
      <SiteHeader locale={locale} path={projectPath} />
      <main>
        <header className="project-hero">
          <div className="project-hero-title">
            <h1>{project.title[locale]}</h1>
            <p className="project-deck">{project.summary[locale]}</p>
          </div>
          <dl className="project-facts">
            <div><dt>{copy[locale].year}</dt><dd>{project.year}</dd></div>
            <div><dt>{copy[locale].role}</dt><dd>{project.role[locale]}</dd></div>
          </dl>
          <img className="project-hero-image" src={project.cover} alt={project.title[locale]} />
        </header>

        <section className="research-question" aria-labelledby="research-question-title">
          <p className="section-kicker">{copy[locale].question}</p>
          <h2 id="research-question-title">{project.question[locale]}</h2>
        </section>

        <section className="contribution-section" aria-labelledby="contribution-title">
          <p className="section-kicker">{copy[locale].contribution}</p>
          <h2 id="contribution-title">{project.role[locale]}</h2>
          <ol>
            {project.contributions[locale].map((item, itemIndex) => (
              <li key={item}><span>{String(itemIndex + 1).padStart(2, "0")}</span>{item}</li>
            ))}
          </ol>
        </section>

        <div className="case-sections">
          {project.sections.map((section) => (
            <section className="case-section" id={section.id} key={section.id}>
              <div className="case-copy">
                <p className="section-kicker">{section.label[locale]}</p>
                <h2>{section.title[locale]}</h2>
                <p>{section.body[locale]}</p>
                {section.details?.[locale].map((detail) => (
                  <p className="case-detail" key={detail}>{detail}</p>
                ))}
              </div>
              <div className="case-visuals">
                {section.gallery?.map((media) => (
                  <figure key={media.src}>
                    <img loading="lazy" src={media.src} alt={media.alt[locale]} />
                    {media.caption ? <figcaption>{media.caption[locale]}</figcaption> : null}
                  </figure>
                ))}
                {!section.gallery && section.image ? (
                  <figure>
                    <img loading="lazy" src={section.image} alt={section.imageAlt?.[locale] ?? section.title[locale]} />
                    {section.caption ? <figcaption>{section.caption[locale]}</figcaption> : null}
                  </figure>
                ) : null}
              </div>
            </section>
          ))}
        </div>

        <nav className="project-pagination" aria-label={locale === "en" ? "Project navigation" : "项目导航"}>
          <a href={localePath(locale, "/work")}>{copy[locale].archive}</a>
          <a href={localePath(locale, `/work/${nextProject.slug}`)}>
            <span>{copy[locale].next}</span>
            <strong>{nextProject.shortTitle[locale]}</strong>
          </a>
        </nav>
      </main>
      <SiteFooter locale={locale} />
    </div>
  );
}
