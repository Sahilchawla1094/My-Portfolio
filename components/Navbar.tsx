"use client";

import { useEffect, useRef, useState } from "react";
import { gsap } from "@/lib/gsap";
import { personal } from "@/lib/data";

const links = [
  { label: "About",      href: "#about"      },
  { label: "Experience", href: "#experience" },
  { label: "Skills",     href: "#skills"     },
  { label: "Projects",   href: "#projects"   },
  { label: "Contact",    href: "#contact"    },
];

export default function Navbar() {
  const navRef  = useRef<HTMLElement>(null);
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    gsap.fromTo(
      navRef.current,
      { y: -20, opacity: 0 },
      { y: 0,   opacity: 1, duration: 0.8, ease: "power2.out", delay: 1.6 }
    );

    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // Lock body scroll when menu is open
  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [menuOpen]);

  const closeMenu = () => setMenuOpen(false);

  return (
    <>
      <nav
        ref={navRef}
        className="fixed top-0 left-0 right-0 z-50 opacity-0"
        style={{
          backdropFilter: scrolled ? "blur(14px)" : "none",
          background:     scrolled ? "rgba(0,0,0,0.7)" : "transparent",
          borderBottom:   scrolled ? "1px solid rgba(255,255,255,0.06)" : "none",
          transition:     "background 0.4s ease, backdrop-filter 0.4s ease, border 0.4s ease",
        }}
      >
        <div className="container flex items-center justify-between h-16">
          {/* Logo */}
          <a
            href="#"
            className="font-mono text-sm tracking-widest text-white/70 hover:text-[var(--accent)] transition-colors"
            style={{ cursor: "none" }}
            onClick={closeMenu}
          >
            {personal.name.split(" ")[0].toUpperCase()}
            <span className="text-[var(--accent)]">.</span>
          </a>

          {/* Desktop links */}
          <ul className="hidden md:flex items-center gap-8">
            {links.map((l) => (
              <li key={l.href}>
                <a
                  href={l.href}
                  className="font-mono text-xs tracking-widest text-white/50 hover:text-[var(--accent)] transition-colors uppercase"
                  style={{ cursor: "none" }}
                >
                  {l.label}
                </a>
              </li>
            ))}
          </ul>

          {/* Desktop CV button */}
          <a
            href={personal.cv}
            download
            className="btn btn-outline text-xs hidden md:flex"
            style={{ cursor: "none" }}
          >
            Download CV
          </a>

          {/* Mobile hamburger */}
          <button
            onClick={() => setMenuOpen((v) => !v)}
            className="md:hidden flex flex-col justify-center items-center w-10 h-10 gap-1.5"
            aria-label="Toggle menu"
            style={{ cursor: "none" }}
          >
            <span
              className="block w-5 h-px bg-white/70 transition-all duration-300 origin-center"
              style={menuOpen ? { transform: "translateY(4px) rotate(45deg)" } : {}}
            />
            <span
              className="block w-5 h-px bg-white/70 transition-all duration-300"
              style={menuOpen ? { opacity: 0 } : {}}
            />
            <span
              className="block w-5 h-px bg-white/70 transition-all duration-300 origin-center"
              style={menuOpen ? { transform: "translateY(-4px) rotate(-45deg)" } : {}}
            />
          </button>
        </div>
      </nav>

      {/* Mobile drawer */}
      <div
        className="fixed inset-0 z-40 md:hidden transition-opacity duration-300"
        style={{
          pointerEvents: menuOpen ? "auto" : "none",
          opacity: menuOpen ? 1 : 0,
          background: "rgba(0,0,0,0.95)",
          backdropFilter: "blur(20px)",
        }}
      >
        <div className="flex flex-col items-center justify-center h-full gap-8">
          {links.map((l) => (
            <a
              key={l.href}
              href={l.href}
              onClick={closeMenu}
              className="font-mono text-2xl tracking-widest text-white/60 hover:text-[var(--accent)] transition-colors uppercase"
            >
              {l.label}
            </a>
          ))}
          <a
            href={personal.cv}
            download
            onClick={closeMenu}
            className="btn btn-outline mt-4"
          >
            Download CV
          </a>
        </div>
      </div>
    </>
  );
}
