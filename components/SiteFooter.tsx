import { localePath, profile, type Locale } from "@/content/site";

const copy = {
  zh: {
    label: "联系",
    title: "想继续讨论这些问题，可以写信给我。",
    note: "人机交互、智能硬件、AI 交互或设计研究等等方面都可以。",
    work: "查看全部项目",
    about: "了解更多",
    documents: "资料下载",
  },
  en: {
    label: "Contact",
    title: "If you want to continue the conversation, send me an email.",
    note: "HCI, smart hardware, AI interaction, and design research are all welcome.",
    work: "View all work",
    about: "More about me",
    documents: "Documents",
  },
};

export function SiteFooter({ locale }: { locale: Locale }) {
  return (
    <footer className="site-footer" id="contact">
      <p className="section-kicker">{copy[locale].label}</p>
      <div className="footer-main">
        <h2>{copy[locale].title}</h2>
        <p>{copy[locale].note}</p>
        <a className="email-link" href={`mailto:${profile.email}`}>
          {profile.email}
        </a>
      </div>
      <div className="footer-bottom">
        <span>© {new Date().getFullYear()} Senpei Chen</span>
        <nav aria-label={locale === "en" ? "Footer" : "页尾导航"}>
          <a href={localePath(locale, "/work")}>{copy[locale].work}</a>
          <a href={localePath(locale, "/about")}>{copy[locale].about}</a>
          <a href={localePath(locale, "/documents")}>{copy[locale].documents}</a>
          <a href={profile.github} target="_blank" rel="noreferrer">GitHub</a>
        </nav>
      </div>
    </footer>
  );
}
