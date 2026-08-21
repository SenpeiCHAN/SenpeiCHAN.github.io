import type { Metadata } from "next";
import { AboutPage } from "@/components/AboutPage";

export const metadata: Metadata = {
  title: "关于 — 陈森培 Senpei Chen",
  description: "陈森培的个人介绍、研究关注、教育经历、实践与方法能力。",
};

export default function About() {
  return <AboutPage locale="zh" />;
}
