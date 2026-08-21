import { localePath, profile, type Locale } from "@/content/site";

const labels = {
  zh: { work: "项目", about: "关于", documents: "资料", contact: "联系", locale: "EN" },
  en: { work: "Work", about: "About", documents: "Documents", contact: "Contact", locale: "中文" },
};

export function SiteHeader({ locale, path = "" }: { locale: Locale; path?: string }) {
  const isEnglish = locale === "en";
  const homePath = localePath(locale);
  const switchPath = isEnglish ? path || "/" : `/en${path}`;

  return (
    <header className="site-header">
      <a className="site-brand" href={homePath} aria-label="Senpei Chen home">
        <img className="brand-avatar" src={profile.portrait} alt="" />
        <span>陈森培 Senpei Chen</span>
      </a>
      <nav className="site-nav" aria-label={isEnglish ? "Primary" : "主导航"}>
        <a href={localePath(locale, "/work")}>{labels[locale].work}</a>
        <a href={localePath(locale, "/about")}>{labels[locale].about}</a>
        <a href={localePath(locale, "/documents")}>{labels[locale].documents}</a>
        <a className="header-contact" href={`mailto:${profile.email}`}>{labels[locale].contact}</a>
        <a className="locale-switch" href={switchPath}>
          {labels[locale].locale}
        </a>
      </nav>
    </header>
  );
}
