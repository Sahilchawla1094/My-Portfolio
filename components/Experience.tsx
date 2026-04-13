"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { experience } from "@/lib/data";

gsap.registerPlugin(ScrollTrigger);

export default function Experience() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    sectionRef.current!.querySelectorAll(".reveal").forEach((el) => {
      gsap.fromTo(el,
        { y: 32, opacity: 0 },
        {
          y: 0, opacity: 1, duration: 0.7, ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 88%", toggleActions: "play none none none" },
        }
      );
    });
  }, []);

  return (
    <section ref={sectionRef} id="experience" className="section">
      <div className="container">
        <span className="label reveal">Work History</span>
        <h2 className="text-5xl font-black heading-gradient mb-16 reveal">Experience</h2>

        <div className="relative">
          {/* Vertical line */}
          <div
            className="absolute left-0 top-0 bottom-0 w-px hidden md:block"
            style={{ background: "linear-gradient(180deg, var(--accent), rgba(123,47,247,0.4) 70%, transparent)" }}
          />

          <div className="space-y-8 md:pl-10">
            {experience.map((exp, i) => (
              <div
                key={i}
                className="reveal card p-8 relative group transition-all duration-300 hover:border-[rgba(0,212,255,0.3)]"
              >
                {/* Timeline dot */}
                <div
                  className="absolute -left-[43px] top-8 w-3 h-3 rounded-full border-2 border-black hidden md:block"
                  style={{ background: "var(--accent)", boxShadow: "0 0 10px rgba(0,212,255,0.5)" }}
                />

                {/* Header */}
                <div className="flex flex-wrap items-start justify-between gap-4 mb-5">
                  <div>
                    <h3 className="text-white text-xl font-bold">{exp.title}</h3>
                    <p className="text-[var(--accent)] font-mono text-sm mt-1">{exp.company} · {exp.location}</p>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    <span className="font-mono text-xs text-white/30 border border-white/10 rounded-full px-3 py-1">
                      {exp.duration}
                    </span>
                    <span className="font-mono text-xs text-purple-400 border border-purple-400/20 rounded-full px-3 py-1 bg-purple-400/5">
                      {exp.domain}
                    </span>
                  </div>
                </div>

                {/* Bullets */}
                <ul className="space-y-2 mb-6">
                  {exp.bullets.map((b, j) => (
                    <li key={j} className="flex gap-3 text-sm text-white/45 leading-relaxed">
                      <span className="text-[var(--accent)] mt-1.5 flex-shrink-0">›</span>
                      {b}
                    </li>
                  ))}
                </ul>

                {/* Tech chips */}
                <div className="flex flex-wrap gap-2">
                  {exp.tech.map((t) => (
                    <span
                      key={t}
                      className="font-mono text-[10px] text-purple-300/60 border border-purple-400/15 rounded px-2 py-1 bg-purple-400/5"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
