import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

// Only register in the browser — ScrollTrigger needs window/document
if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
}

export { gsap, ScrollTrigger };
