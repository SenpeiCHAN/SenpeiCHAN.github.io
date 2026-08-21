import type { Metadata } from "next";
import Link from "next/link";
import { ProjectPage } from "@/components/ProjectPage";
import { getProject, getPublishedProjects } from "@/content/site";

type ProjectRouteProps = { params: Promise<{ slug: string }> };
const SITE_URL = "https://senpeichan.github.io";

export function generateStaticParams() {
  return getPublishedProjects().map((project) => ({ slug: project.slug }));
}

export async function generateMetadata({ params }: ProjectRouteProps): Promise<Metadata> {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) return { title: "项目未找到 — Senpei Chen" };
  const image = new URL(project.cover, SITE_URL).toString();

  return {
    title: `${project.title.zh} — Senpei Chen`,
    description: project.summary.zh,
    openGraph: { title: project.title.zh, description: project.summary.zh, images: [image] },
    twitter: { card: "summary_large_image", title: project.title.zh, description: project.summary.zh, images: [image] },
  };
}

export default async function ProjectDetail({ params }: ProjectRouteProps) {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) return <main className="not-found"><h1>项目未找到</h1><Link href="/work">返回项目档案</Link></main>;
  return <ProjectPage project={project} locale="zh" />;
}
