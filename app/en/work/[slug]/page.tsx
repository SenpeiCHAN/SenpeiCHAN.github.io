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
  if (!project) return { title: "Project not found — Senpei Chen" };
  const image = new URL(project.cover, SITE_URL).toString();

  return {
    title: `${project.title.en} — Senpei Chen`,
    description: project.summary.en,
    openGraph: { title: project.title.en, description: project.summary.en, images: [image] },
    twitter: { card: "summary_large_image", title: project.title.en, description: project.summary.en, images: [image] },
  };
}

export default async function EnglishProjectDetail({ params }: ProjectRouteProps) {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) return <main className="not-found"><h1>Project not found</h1><Link href="/en/work">Back to archive</Link></main>;
  return <ProjectPage project={project} locale="en" />;
}
