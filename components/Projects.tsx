"use client";

import { useEffect, useRef } from "react";
import Image from "next/image";
import { projects } from "@/lib/data";

export default function Projects() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    let ctx: ReturnType<typeof import("gsap").gsap.context> | undefined;

    import("@/lib/gsap").then(({ gsap, ScrollTrigger }) => {
      ctx = gsap.context(() => {
        sectionRef.current!.querySelectorAll<HTMLElement>(".reveal").forEach((el) => {
          gsap.fromTo(el,
            { y: 30, opacity: 0 },
            {
              y: 0, opacity: 1, duration: 0.7, ease: "power2.out",
              scrollTrigger: { trigger: el, start: "top 88%", toggleActions: "play none none none" },
            }
          );
        });
        ScrollTrigger.refresh();
      }, sectionRef.current!);
    });

    return () => ctx?.revert();
  }, []);

  return (
    <section ref={sectionRef} id="projects" className="section">
      <div className="container">
        <span className="label reveal">Portfolio</span>
        <h2 className="text-4xl md:text-5xl font-black heading-gradient mb-10 md:mb-16 reveal">Projects</h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
          {projects.map((p, i) => (
            <a
              key={i}
              href={p.link}
              target="_blank"
              rel="noreferrer"
              className="reveal group card overflow-hidden flex flex-col"
              style={{ cursor: "none" }}
            >
              <div className="relative h-44 overflow-hidden">
                <Image
                  src={p.image}
                  alt={p.title}
                  fill
                  className="object-cover transition-transform duration-700 group-hover:scale-105"
                  style={{ filter: "brightness(0.7) saturate(0.7)" }}
                  sizes="(max-width: 768px) 100vw, 33vw"
                />
                <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                  style={{ background: "rgba(0,212,255,0.06)" }} />
                <span className="absolute top-3 right-4 font-mono text-xs text-white/20">
                  {String(i + 1).padStart(2, "0")}
                </span>
              </div>

              <div className="p-6 flex flex-col flex-1">
                <p className="font-mono text-[10px] text-[var(--accent)] tracking-widest uppercase mb-2">{p.subtitle}</p>
                <h3 className="text-white font-bold text-base mb-3 leading-snug">{p.title}</h3>
                <p className="text-white/35 text-sm leading-relaxed flex-1 mb-4">{p.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {p.tags.map((t) => (
                    <span key={t} className="font-mono text-[10px] text-purple-300/50 border border-purple-400/15 rounded px-2 py-0.5 bg-purple-400/5">
                      {t}
                    </span>
                  ))}
                </div>
                <div className="flex items-center gap-2 font-mono text-xs text-[var(--accent)] group-hover:gap-3 transition-all">
                  <span>View on GitHub</span>
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
