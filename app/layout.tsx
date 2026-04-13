import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import SmoothScroll from "@/components/SmoothScroll";
import Cursor from "@/components/Cursor";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Sahil Chawla | Data Scientist",
  description:
    "Data Scientist with 4.5+ years of experience in ML, Generative AI, and Supply Chain. Technology Consultant at EY.",
  keywords: [
    "Sahil Chawla",
    "Data Scientist",
    "Machine Learning",
    "Generative AI",
    "EY",
    "Portfolio",
  ],
  authors: [{ name: "Sahil Chawla", url: "https://sahilchawla.xyz" }],
  metadataBase: new URL("https://sahilchawla.xyz"),
  openGraph: {
    title: "Sahil Chawla | Data Scientist",
    description:
      "Data Scientist with 4.5+ years of experience in ML, Generative AI, and Supply Chain.",
    url: "https://sahilchawla.xyz",
    siteName: "Sahil Chawla",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Sahil Chawla | Data Scientist",
    description: "Data Scientist | ML | GenAI | EY",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body>
        <Cursor />
        <SmoothScroll>{children}</SmoothScroll>
      </body>
    </html>
  );
}
