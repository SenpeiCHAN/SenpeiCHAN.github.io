import { documents, profile, type Locale } from "@/content/site";
import { SiteFooter } from "./SiteFooter";
import { SiteHeader } from "./SiteHeader";

const copy = {
  zh: {
    label: "资料",
    title: "简历与完整作品集。",
    intro: "CV 可以下载，完整作品集可以在线查看或保存。",
    open: "在线查看",
    download: "下载文件",
    note: "需要其他格式或项目材料，可以发邮件给我。",
  },
  en: {
    label: "Documents",
    title: "CV and complete portfolio.",
    intro: "Download the CV or read the complete portfolio online.",
    open: "Open online",
    download: "Download file",
    note: "Email me if you need another format or more project material.",
  },
};

export function DocumentsPage({ locale }: { locale: Locale }) {
  return (
    <div className="site-shell">
      <SiteHeader locale={locale} path="/documents" />
      <main>
        <header className="page-intro documents-intro">
          <h1>{copy[locale].title}</h1>
          <p className="page-lead">{copy[locale].intro}</p>
        </header>
        <section className="documents-section" aria-label={copy[locale].label}>
          <div className="document-list">
            {documents.map((document, index) => (
              <article className="document-card" key={document.id}>
                <div className="document-number">{String(index + 1).padStart(2, "0")}</div>
                <div className="document-copy">
                  <span>{document.format}</span>
                  <h2>{document.title[locale]}</h2>
                  {document.description[locale] ? <p>{document.description[locale]}</p> : null}
                </div>
                <div className="document-actions">
                  {document.previewable ? (
                    <a className="button button-primary" href={document.href} target="_blank" rel="noreferrer">
                      {copy[locale].open}
                    </a>
                  ) : null}
                  <a className="button button-text" href={document.href} download>
                    {copy[locale].download}
                  </a>
                </div>
              </article>
            ))}
          </div>
          <p className="documents-note">
            {copy[locale].note} <a href={`mailto:${profile.email}`}>{profile.email}</a>
          </p>
        </section>
      </main>
      <SiteFooter locale={locale} />
    </div>
  );
}
