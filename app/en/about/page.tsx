import type { Metadata } from "next";
import { AboutPage } from "@/components/AboutPage";

export const metadata: Metadata = {
  title: "About — Senpei Chen",
  description: "Senpei Chen’s profile, research interests, education, practice, methods, and capabilities.",
};

export default function EnglishAbout() {
  return <AboutPage locale="en" />;
}
