import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import ClientShell from "@/components/ClientShell";

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
  keywords: ["Sahil Chawla", "Data Scientist", "Machine Learning", "Generative AI", "EY"],
  authors: [{ name: "Sahil Chawla", url: "https://sahilchawla.xyz" }],
  metadataBase: new URL("https://sahilchawla.xyz"),
  openGraph: {
    title: "Sahil Chawla | Data Scientist",
    description: "Data Scientist with 4.5+ years of experience in ML, Generative AI, and Supply Chain.",
    url: "https://sahilchawla.xyz",
    siteName: "Sahil Chawla",
    type: "website",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body>
        <ClientShell>{children}</ClientShell>
      </body>
    </html>
  );
}
