"use client";

import { useEffect, useRef } from "react";

export default function SmoothScroll({ children }: { children: React.ReactNode }) {
  const lenisRef = useRef<unknown>(null);

  useEffect(() => {
    let raf: number;

    // Dynamic import so Lenis never runs on server
    import("lenis").then(({ default: Lenis }) => {
      const lenis = new Lenis({ duration: 1.1, smoothWheel: true });
      lenisRef.current = lenis;

      function tick(time: number) {
        lenis.raf(time);
        raf = requestAnimationFrame(tick);
      }
      raf = requestAnimationFrame(tick);
    });

    return () => {
      cancelAnimationFrame(raf);
      (lenisRef.current as { destroy?: () => void })?.destroy?.();
    };
  }, []);

  return <>{children}</>;
}
