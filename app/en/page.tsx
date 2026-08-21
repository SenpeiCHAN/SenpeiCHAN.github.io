import type { Metadata } from "next";
import { HomePage } from "@/components/HomePage";

export const metadata: Metadata = {
  title: "Senpei Chen — HCI & Interaction Design",
  description: "The personal project and research archive of Senpei Chen, exploring HCI, smart hardware, AI vision, products, and physical prototypes.",
};

export default function EnglishHome() {
  return <HomePage locale="en" />;
}
