import type { Locale, Project } from "@/content/site";

export function ProjectCard({
  project,
  locale,
  index,
}: {
  project: Project;
  locale: Locale;
  index: number;
}) {
  const prefix = locale === "en" ? "/en" : "";

  return (
    <article className={`project-card theme-${project.theme}`}>
      <a className="project-image-link" href={`${prefix}/work/${project.slug}`}>
        <img
          className="project-image"
          src={project.cover}
          alt={project.title[locale]}
        />
      </a>
      <div className="project-meta">
        <span>{String(index + 1).padStart(2, "0")}</span>
        <span>{project.year}</span>
        <span>{project.role[locale]}</span>
      </div>
      <h3>
        <a href={`${prefix}/work/${project.slug}`}>{project.title[locale]}</a>
      </h3>
      <p>{project.subtitle[locale]}</p>
      <ul className="tag-list" aria-label={locale === "en" ? "Project tags" : "项目标签"}>
        {project.tags[locale].map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    </article>
  );
}
