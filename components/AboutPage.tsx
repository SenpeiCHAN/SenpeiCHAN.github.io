import {
  capabilityGroups,
  profile,
  researchQuestions,
  timeline,
  type Locale,
} from "@/content/site";
import { SiteFooter } from "./SiteFooter";
import { SiteHeader } from "./SiteHeader";

const copy = {
  zh: {
    label: "关于",
    title: "我是陈森培。我研究人怎样与设备、AI 和空间发生交互。",
    bio: "我就读于广州美术学院智能交互设计专业。我会做访谈、拆机、建模和原型，直到问题能被操作，也能被继续验证。",
    focus: "研究关注",
    timeline: "教育与实践",
    capabilities: "方法与能力",
    toolsNote: "工具会随项目改变，以下内容更关注我能够完成的研究与设计工作。",
  },
  en: {
    label: "About",
    title: "I’m Senpei Chen. I study how people interact with devices, AI, and space.",
    bio: "I study Interaction Design at Guangzhou Academy of Fine Arts. I use interviews, teardown, modeling, and prototypes until the question becomes usable and testable.",
    focus: "Research focus",
    timeline: "Education & practice",
    capabilities: "Methods & capabilities",
    toolsNote: "Tools change with each project; this section emphasizes the research and design work I can carry out.",
  },
};

export function AboutPage({ locale }: { locale: Locale }) {
  return (
    <div className="site-shell">
      <SiteHeader locale={locale} path="/about" />
      <main>
        <header className="about-hero">
          <div className="about-hero-copy">
            <h1>{copy[locale].title}</h1>
            <p>{copy[locale].bio}</p>
          </div>
          <figure className="about-portrait">
            <img src={profile.portrait} alt={locale === "en" ? "Portrait of Senpei Chen" : "陈森培肖像"} />
          </figure>
        </header>

        <section className="about-section" aria-labelledby="focus-heading">
          <p className="section-kicker">01</p>
          <div>
            <h2 id="focus-heading">{copy[locale].focus}</h2>
            <ol className="compact-question-list">
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
          </div>
        </section>

        <section className="about-section" aria-labelledby="timeline-heading">
          <p className="section-kicker">02</p>
          <div>
            <h2 id="timeline-heading">{copy[locale].timeline}</h2>
            <div className="timeline-list">
              {timeline.map((item) => (
                <article key={`${item.year}-${item.title.en}`}>
                  <time>{item.year}</time>
                  <div>
                    <h3>{item.title[locale]}</h3>
                    <p>{item.description[locale]}</p>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="about-section" aria-labelledby="capabilities-heading">
          <p className="section-kicker">03</p>
          <div>
            <h2 id="capabilities-heading">{copy[locale].capabilities}</h2>
            <p className="section-note">{copy[locale].toolsNote}</p>
            <div className="capability-grid">
              {capabilityGroups.map((group, index) => (
                <article key={group.title.en}>
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <h3>{group.title[locale]}</h3>
                  <ul>
                    {group.items[locale].map((item) => <li key={item}>{item}</li>)}
                  </ul>
                </article>
              ))}
            </div>
          </div>
        </section>
      </main>
      <SiteFooter locale={locale} />
    </div>
  );
}
