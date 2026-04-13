"use client";

import { useEffect, useRef } from "react";
import { skills } from "@/lib/data";

const doubled = [...skills, ...skills];

export default function Skills() {
  const sectionRef = useRef<HTMLElement>(null);
  const barsRef    = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!sectionRef.current) return;
    let ctx: ReturnType<typeof import("gsap").gsap.context> | undefined;

    import("@/lib/gsap").then(({ gsap, ScrollTrigger }) => {
      ctx = gsap.context(() => {
        sectionRef.current!.querySelectorAll<HTMLElement>(".reveal").forEach((el) => {
          gsap.fromTo(el,
            { y: 28, opacity: 0 },
            {
              y: 0, opacity: 1, duration: 0.7, ease: "power2.out",
              scrollTrigger: { trigger: el, start: "top 88%", toggleActions: "play none none none" },
            }
          );
        });

        // Skill bar animation
        const fills = barsRef.current!.querySelectorAll<HTMLElement>(".skill-fill");
        gsap.fromTo(fills,
          { width: "0%" },
          {
            width: (i: number) => fills[i].dataset.pct + "%",
            duration: 1.3,
            stagger: 0.04,
            ease: "power2.out",
            scrollTrigger: { trigger: barsRef.current, start: "top 80%", toggleActions: "play none none none" },
          }
        );
        ScrollTrigger.refresh();
      }, sectionRef.current!);
    });

    return () => ctx?.revert();
  }, []);

  return (
    <section ref={sectionRef} id="skills" className="section overflow-hidden">
      <div className="container">
        <span className="label reveal">Technical Proficiency</span>
        <h2 className="text-5xl font-black heading-gradient mb-16 reveal">Skills</h2>
      </div>

      {/* Marquee */}
      <div className="border-y border-white/5 py-5 mb-14 reveal overflow-hidden">
        <div className="marquee-track">
          {doubled.map((s, i) => (
            <span key={i} className="font-mono text-xs text-white/25 uppercase tracking-widest mx-6 whitespace-nowrap">
              {s.name}
              <span className="text-[var(--accent)] ml-6">·</span>
            </span>
          ))}
        </div>
      </div>

      {/* Bars */}
      <div className="container">
        <div ref={barsRef} className="grid md:grid-cols-2 gap-x-16 gap-y-5">
          {skills.map((s) => (
            <div key={s.name} className="reveal">
              <div className="flex justify-between mb-2">
                <span className="font-mono text-xs text-white/60">{s.name}</span>
                <span className="font-mono text-xs text-[var(--accent)]">{s.pct}%</span>
              </div>
              <div className="h-px bg-white/5 rounded overflow-hidden">
                <div
                  className="skill-fill h-full rounded"
                  data-pct={s.pct}
                  style={{ width: "0%", background: "linear-gradient(90deg, var(--accent), #7b2ff7)", boxShadow: "0 0 6px rgba(0,212,255,0.3)" }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
