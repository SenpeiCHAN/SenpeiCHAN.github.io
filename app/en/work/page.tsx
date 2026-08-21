import type { Metadata } from "next";
import { WorkPage } from "@/components/WorkPage";

export const metadata: Metadata = {
  title: "Project Archive — Senpei Chen",
  description: "Senpei Chen’s project archive across HCI, smart hardware, AI vision, product design, and physical prototyping.",
};

export default function EnglishWorkArchive() {
  return <WorkPage locale="en" />;
}
