import type { Metadata } from "next";
import { DocumentsPage } from "@/components/DocumentsPage";

export const metadata: Metadata = {
  title: "Documents — Senpei Chen",
  description: "View or download Senpei Chen’s CV and complete project portfolio.",
};

export default function EnglishDocuments() {
  return <DocumentsPage locale="en" />;
}
