"use client";

import { useEffect, useRef } from "react";
import { gsap } from "@/lib/gsap";
import { personal, stats } from "@/lib/data";

/* ── Particle canvas ──────────────────────────────────── */
function ParticleCanvas() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current!;
    const ctx    = canvas.getContext("2d")!;
    let   raf:   number;

    const resize = () => {
      canvas.width  = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    resize();
    window.addEventListener("resize", resize);

    type Pt = { x: number; y: number; vx: number; vy: number; r: number; a: number };
    const pts: Pt[] = Array.from({ length: 70 }, () => ({
      x:  Math.random() * canvas.width,
      y:  Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      r:  Math.random() * 1.3 + 0.4,
      a:  Math.random() * 0.3 + 0.07,
    }));

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (let i = 0; i < pts.length; i++) {
        const p = pts[i];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > canvas.width)  p.vx *= -1;
        if (p.y < 0 || p.y > canvas.height)  p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0,212,255,${p.a})`;
        ctx.fill();

        for (let j = i + 1; j < pts.length; j++) {
          const q  = pts[j];
          const dx = p.x - q.x, dy = p.y - q.y;
          const d  = Math.sqrt(dx * dx + dy * dy);
          if (d < 110) {
            ctx.beginPath();
            ctx.strokeStyle = `rgba(0,212,255,${0.1 * (1 - d / 110)})`;
            ctx.lineWidth = 0.5;
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(q.x, q.y);
            ctx.stroke();
          }
        }
      }
      raf = requestAnimationFrame(draw);
    };
    draw();

    return () => { cancelAnimationFrame(raf); window.removeEventListener("resize", resize); };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="absolute inset-0 w-full h-full"
      aria-hidden
    />
  );
}

/* ── Split chars helper ───────────────────────────────── */
function SplitText({ text, className }: { text: string; className?: string }) {
  return (
    <span aria-label={text} className={className}>
      {text.split("").map((ch, i) => (
        <span key={i} className="split-char" style={{ whiteSpace: ch === " " ? "pre" : "normal" }}>
          {ch}
        </span>
      ))}
    </span>
  );
}

/* ── Hero ─────────────────────────────────────────────── */
export default function Hero() {
  const sectionRef = useRef<HTMLElement>(null);
  const subtitleRef = useRef<HTMLParagraphElement>(null);
  const buttonsRef = useRef<HTMLDivElement>(null);
  const statsRef   = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const chars = sectionRef.current!.querySelectorAll(".split-char");
    const tl = gsap.timeline({ delay: 0.3 });

    tl.fromTo(
      chars,
      { y: 60, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.8, stagger: 0.03, ease: "power3.out" }
    )
    .fromTo(subtitleRef.current,
      { y: 20, opacity: 0 },
      { y: 0,  opacity: 1, duration: 0.6, ease: "power2.out" },
      "-=0.3"
    )
    .fromTo(buttonsRef.current,
      { y: 20, opacity: 0 },
      { y: 0,  opacity: 1, duration: 0.5, ease: "power2.out" },
      "-=0.2"
    )
    .fromTo(statsRef.current!.children,
      { y: 24, opacity: 0 },
      { y: 0,  opacity: 1, duration: 0.5, stagger: 0.1, ease: "power2.out" },
      "-=0.1"
    );
  }, []);

  /* animated counter */
  useEffect(() => {
    const els = statsRef.current!.querySelectorAll<HTMLElement>("[data-count]");
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el      = entry.target as HTMLElement;
        const target  = parseFloat(el.dataset.count!);
        const dec     = parseInt(el.dataset.dec ?? "0");
        const dur     = 1600;
        const start   = performance.now();
        const tick = (now: number) => {
          const p = Math.min((now - start) / dur, 1);
          const v = (1 - Math.pow(1 - p, 3)) * target;
          el.textContent = dec ? v.toFixed(dec) : String(Math.floor(v));
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        obs.unobserve(el);
      });
    }, { threshold: 0.5 });
    els.forEach((el) => obs.observe(el));
    return () => obs.disconnect();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="hero"
      className="relative min-h-screen flex flex-col justify-center overflow-hidden"
    >
      <ParticleCanvas />

      {/* Radial glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse 80% 60% at 50% 40%, rgba(0,212,255,0.05) 0%, transparent 70%)",
        }}
        aria-hidden
      />

      <div className="container relative z-10 pt-28 pb-16">
        {/* Greeting */}
        <p className="label mb-4">// hello, world</p>

        {/* Name */}
        <h1
          className="text-[clamp(52px,8vw,110px)] font-black leading-none tracking-tight mb-4 overflow-hidden"
          style={{ lineHeight: 1.0 }}
        >
          <SplitText text={personal.name} className="heading-gradient" />
        </h1>

        {/* Role */}
        <p
          ref={subtitleRef}
          className="font-mono text-[clamp(14px,2vw,20px)] text-white/40 tracking-[0.2em] mb-8 uppercase"
        >
          {personal.role}
        </p>

        {/* Bio one-liner */}
        <p className="text-white/50 text-base max-w-lg leading-relaxed mb-10 reveal">
          {personal.tagline}
        </p>

        {/* CTAs */}
        <div ref={buttonsRef} className="flex flex-wrap gap-4">
          <a href="#projects" className="btn btn-filled" style={{ cursor: "none" }}>
            View Projects
          </a>
          <a href="#contact" className="btn btn-outline" style={{ cursor: "none" }}>
            Get In Touch
          </a>
        </div>

        {/* Stats */}
        <div
          ref={statsRef}
          className="grid grid-cols-2 md:grid-cols-4 gap-px mt-20 border border-white/5 rounded-2xl overflow-hidden"
          style={{ background: "rgba(255,255,255,0.03)" }}
        >
          {stats.map((s) => (
            <div
              key={s.label}
              className="flex flex-col items-center justify-center py-8 px-4 text-center"
              style={{ background: "rgba(0,0,0,0.4)" }}
            >
              <div className="font-mono text-4xl font-bold text-[var(--accent)]">
                {s.prefix ?? ""}
                <span data-count={s.value} data-dec={s.decimals}>0</span>
                {s.suffix}
              </div>
              <div className="font-mono text-[10px] tracking-widest text-white/30 uppercase mt-2">
                {s.label}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Scroll indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-30">
        <span className="font-mono text-[10px] tracking-widest uppercase text-white/40">Scroll</span>
        <div className="w-px h-12 bg-gradient-to-b from-white/40 to-transparent" />
      </div>
    </section>
  );
}
