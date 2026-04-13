"use client";
import dynamic from "next/dynamic";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

// Skip SSR for all sections that use GSAP / canvas / browser APIs
const Hero       = dynamic(() => import("@/components/Hero"),       { ssr: false });
const About      = dynamic(() => import("@/components/About"),      { ssr: false });
const Experience = dynamic(() => import("@/components/Experience"), { ssr: false });
const Skills     = dynamic(() => import("@/components/Skills"),     { ssr: false });
const Projects   = dynamic(() => import("@/components/Projects"),   { ssr: false });
const Contact    = dynamic(() => import("@/components/Contact"),    { ssr: false });

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <About />
      <Experience />
      <Skills />
      <Projects />
      <Contact />
      <Footer />
    </main>
  );
}
