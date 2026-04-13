"use client";

import { useEffect, useRef } from "react";
import gsap from "gsap";

export default function Cursor() {
  const dotRef  = useRef<HTMLDivElement>(null);
  const ringRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const dot  = dotRef.current!;
    const ring = ringRef.current!;

    const moveDot  = { x: 0, y: 0 };
    const moveRing = { x: 0, y: 0 };

    const onMove = (e: MouseEvent) => {
      moveDot.x  = e.clientX;
      moveDot.y  = e.clientY;
      gsap.to(dot,  { x: moveDot.x,  y: moveDot.y,  duration: 0,    ease: "none" });
      gsap.to(ring, { x: moveDot.x,  y: moveDot.y,  duration: 0.18, ease: "power2.out" });
    };

    const onEnter = () => ring.classList.add("hovered");
    const onLeave = () => ring.classList.remove("hovered");

    window.addEventListener("mousemove", onMove);

    const interactables = document.querySelectorAll("a, button, [data-cursor]");
    interactables.forEach((el) => {
      el.addEventListener("mouseenter", onEnter);
      el.addEventListener("mouseleave", onLeave);
    });

    return () => {
      window.removeEventListener("mousemove", onMove);
      interactables.forEach((el) => {
        el.removeEventListener("mouseenter", onEnter);
        el.removeEventListener("mouseleave", onLeave);
      });
    };
  }, []);

  return (
    <>
      <div ref={dotRef}  className="cursor-dot"  aria-hidden />
      <div ref={ringRef} className="cursor-ring" aria-hidden />
    </>
  );
}
