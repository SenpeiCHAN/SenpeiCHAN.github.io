import type { Metadata } from "next";
import { DocumentsPage } from "@/components/DocumentsPage";

export const metadata: Metadata = {
  title: "资料 — 陈森培 Senpei Chen",
  description: "在线查看或下载陈森培的个人简历和完整项目作品集。",
};

export default function Documents() {
  return <DocumentsPage locale="zh" />;
}
