import type { Metadata } from "next";
import { WorkPage } from "@/components/WorkPage";

export const metadata: Metadata = {
  title: "项目档案 — 陈森培 Senpei Chen",
  description: "陈森培在人机交互、智能硬件、AI 视觉、产品设计与实体原型方面的项目档案。",
};

export default function WorkArchive() {
  return <WorkPage locale="zh" />;
}
