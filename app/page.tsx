import type { Metadata } from "next";
import { HomePage } from "@/components/HomePage";

export const metadata: Metadata = {
  title: "陈森培 Senpei Chen — 人机交互与智能交互设计",
  description: "陈森培的个人项目与研究档案，关注人机交互、智能硬件、AI 视觉、产品与实体原型。",
};

export default function Home() {
  return <HomePage locale="zh" />;
}
