"use client";

import { useEffect, useRef, useState } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { personal } from "@/lib/data";

gsap.registerPlugin(ScrollTrigger);

export default function Contact() {
  const sectionRef = useRef<HTMLElement>(null);
  const [status, setStatus] = useState<"idle" | "sending" | "sent" | "error">("idle");
  const [form, setForm] = useState({ name: "", email: "", message: "" });

  useEffect(() => {
    sectionRef.current!.querySelectorAll(".reveal").forEach((el) => {
      gsap.fromTo(el,
        { y: 28, opacity: 0 },
        {
          y: 0, opacity: 1, duration: 0.7, ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 88%", toggleActions: "play none none none" },
        }
      );
    });
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.name || !form.email || !form.message) return;
    setStatus("sending");
    try {
      /* EmailJS integration — replace with your IDs in .env.local */
      const SERVICE_ID  = process.env.NEXT_PUBLIC_EMAILJS_SERVICE_ID  ?? "";
      const TEMPLATE_ID = process.env.NEXT_PUBLIC_EMAILJS_TEMPLATE_ID ?? "";
      const USER_ID     = process.env.NEXT_PUBLIC_EMAILJS_USER_ID     ?? "";
      const res = await fetch("https://api.emailjs.com/api/v1.0/email/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          service_id:  SERVICE_ID,
          template_id: TEMPLATE_ID,
          user_id:     USER_ID,
          template_params: {
            from_name:  form.name,
            from_email: form.email,
            message:    form.message,
          },
        }),
      });
      setStatus(res.ok ? "sent" : "error");
    } catch {
      setStatus("error");
    }
  };

  const inputClass =
    "w-full bg-white/[0.03] border border-white/10 rounded-lg px-4 py-3 text-white/80 text-sm placeholder-white/20 font-mono focus:outline-none focus:border-[var(--accent)] focus:bg-white/[0.05] transition-all";

  return (
    <section ref={sectionRef} id="contact" className="section">
      <div className="container">
        <span className="label reveal">Get In Touch</span>
        <h2 className="text-5xl font-black heading-gradient mb-16 reveal">Contact</h2>

        <div className="grid md:grid-cols-2 gap-16">
          {/* Left */}
          <div>
            <p className="reveal text-white/50 text-base leading-relaxed mb-10">
              Have a project in mind or just want to connect? Drop me a message
              and I&apos;ll get back to you as soon as possible.
            </p>

            <div className="space-y-6">
              {[
                { label: "Email",   value: personal.email,   href: `mailto:${personal.email}` },
                { label: "Phone",   value: personal.phone,   href: `tel:${personal.phone}`   },
                { label: "Address", value: personal.address, href: undefined                 },
              ].map((item) => (
                <div key={item.label} className="reveal flex gap-4">
                  <div className="w-1.5 h-1.5 rounded-full bg-[var(--accent)] mt-2 flex-shrink-0" />
                  <div>
                    <p className="font-mono text-[10px] text-white/25 tracking-widest uppercase mb-1">
                      {item.label}
                    </p>
                    {item.href ? (
                      <a href={item.href}
                        className="text-white/60 text-sm hover:text-[var(--accent)] transition-colors"
                        style={{ cursor: "none" }}>
                        {item.value}
                      </a>
                    ) : (
                      <p className="text-white/60 text-sm">{item.value}</p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Right — Form */}
          <form onSubmit={handleSubmit} className="reveal space-y-4">
            <input
              type="text"
              placeholder="Your Name"
              className={inputClass}
              style={{ cursor: "none" }}
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
            />
            <input
              type="email"
              placeholder="your@email.com"
              className={inputClass}
              style={{ cursor: "none" }}
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
            />
            <textarea
              rows={5}
              placeholder="Your message..."
              className={inputClass}
              style={{ cursor: "none", resize: "none" }}
              value={form.message}
              onChange={(e) => setForm({ ...form, message: e.target.value })}
            />

            <button
              type="submit"
              disabled={status === "sending" || status === "sent"}
              className="btn btn-filled w-full justify-center disabled:opacity-50"
              style={{ cursor: "none" }}
            >
              {status === "idle"    && "Send Message"}
              {status === "sending" && "Sending…"}
              {status === "sent"    && "Message Sent ✓"}
              {status === "error"   && "Failed — Try Again"}
            </button>

            {/* .env hint */}
            <p className="font-mono text-[10px] text-white/15 text-center">
              Configure EmailJS keys in .env.local to enable sending.
            </p>
          </form>
        </div>
      </div>
    </section>
  );
}
