import { getPublishedProjects, type Locale } from "@/content/site";
import { ProjectCard } from "./ProjectCard";
import { SiteFooter } from "./SiteFooter";
import { SiteHeader } from "./SiteHeader";

const copy = {
  zh: {
    label: "项目档案",
    title: "项目",
    intro: "这里有研究材料、方案变化、制作过程和结果。",
  },
  en: {
    label: "Project archive",
    title: "Projects",
    intro: "Research material, changing ideas, fabrication, and outcomes.",
  },
};

export function WorkPage({ locale }: { locale: Locale }) {
  const projects = getPublishedProjects();

  return (
    <div className="site-shell">
      <SiteHeader locale={locale} path="/work" />
      <main>
        <header className="page-intro">
          <h1>{copy[locale].title}</h1>
          <p className="page-lead">{copy[locale].intro}</p>
        </header>
        <section className="archive-section" aria-label={copy[locale].label}>
          <div className="project-grid">
            {projects.map((project, index) => (
              <ProjectCard key={project.slug} project={project} locale={locale} index={index} />
            ))}
          </div>
        </section>
      </main>
      <SiteFooter locale={locale} />
    </div>
  );
}
