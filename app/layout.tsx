import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://senpeichan.github.io"),
  title: {
    default: "Senpei Chen — HCI & Interaction Design",
    template: "%s",
  },
  description: "Personal project and research archive of Senpei Chen.",
  openGraph: {
    title: "Senpei Chen — HCI & Interaction Design",
    description: "Personal project and research archive of Senpei Chen.",
    images: ["/og.png"],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Senpei Chen — HCI & Interaction Design",
    description: "Personal project and research archive of Senpei Chen.",
    images: ["/og.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `if(location.pathname==='/en'||location.pathname.startsWith('/en/'))document.documentElement.lang='en';`,
          }}
        />
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
