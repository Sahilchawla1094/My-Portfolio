"use client";

import { useEffect, useRef } from "react";
import Image from "next/image";
import { gsap, ScrollTrigger } from "@/lib/gsap";
import { personal, education } from "@/lib/data";

export default function About() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const els = sectionRef.current!.querySelectorAll(".reveal");
    els.forEach((el) => {
      gsap.fromTo(
        el,
        { y: 32, opacity: 0 },
        {
          y: 0, opacity: 1, duration: 0.8, ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 88%", toggleActions: "play none none none" },
        }
      );
    });
  }, []);

  return (
    <section ref={sectionRef} id="about" className="section">
      <div className="container">
        <span className="label reveal">About Me</span>
        <h2 className="text-5xl font-black heading-gradient mb-16 reveal">
          Who I Am
        </h2>

        <div className="grid md:grid-cols-2 gap-16 items-start">
          {/* Left — image + education */}
          <div>
            <div className="reveal relative rounded-2xl overflow-hidden aspect-[4/5] mb-10"
              style={{ border: "1px solid rgba(0,212,255,0.15)" }}>
              <Image
                src="/assets/profile.jpg"
                alt="Sahil Chawla"
                fill
                className="object-cover object-top"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
              <div
                className="absolute inset-0"
                style={{ background: "linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 60%)" }}
              />
              <div className="absolute bottom-5 left-5">
                <p className="font-mono text-xs text-[var(--accent)] tracking-widest uppercase">Currently</p>
                <p className="text-white font-semibold text-sm mt-1">Technology Consultant @ EY</p>
              </div>
            </div>

            {/* Education */}
            <h3 className="font-mono text-xs text-white/30 tracking-widest uppercase mb-6 reveal">Education</h3>
            <div className="space-y-4">
              {education.map((edu) => (
                <div
                  key={edu.degree}
                  className="reveal card p-4 flex gap-4 items-start"
                >
                  <div className="w-1.5 h-1.5 rounded-full bg-[var(--accent)] mt-2 flex-shrink-0" />
                  <div>
                    <p className="text-white/80 text-sm font-semibold leading-snug">{edu.degree}</p>
                    <p className="text-white/30 text-xs mt-1 font-mono">{edu.institution}</p>
                    <p className="text-white/20 text-xs font-mono">
                      {edu.duration}{edu.grade ? ` · ${edu.grade}` : ""}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Right — bio */}
          <div>
            <div className="space-y-6 mb-12">
              {personal.bio.map((para, i) => (
                <p key={i} className="reveal text-white/55 text-base leading-relaxed">
                  {para}
                </p>
              ))}
            </div>

            {/* Highlights grid */}
            <div className="grid grid-cols-2 gap-4">
              {[
                { label: "Current Role",   value: "Tech Consultant @ EY" },
                { label: "Domains",        value: "Supply Chain · Ed-tech" },
                { label: "Location",       value: "Gurugram, India" },
                { label: "Languages",      value: "English · Hindi" },
              ].map((item) => (
                <div key={item.label} className="reveal card p-5">
                  <p className="font-mono text-[10px] text-white/25 tracking-widest uppercase mb-1">
                    {item.label}
                  </p>
                  <p className="text-white/70 text-sm font-semibold">{item.value}</p>
                </div>
              ))}
            </div>

            {/* Social links */}
            <div className="reveal flex gap-4 mt-8">
              {[
                { label: "GitHub",   href: personal.github   },
                { label: "LinkedIn", href: personal.linkedin  },
                { label: "Tableau",  href: personal.tableau   },
              ].map((s) => (
                <a
                  key={s.label}
                  href={s.href}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-outline text-xs"
                  style={{ cursor: "none" }}
                >
                  {s.label}
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
