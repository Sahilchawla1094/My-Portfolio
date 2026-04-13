import { personal } from "@/lib/data";

export default function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="border-t border-white/5 py-10">
      <div className="container flex flex-col md:flex-row items-center justify-between gap-4">
        <p className="font-mono text-xs text-white/20 tracking-widest">
          &copy; {year} {personal.name.toUpperCase()} &mdash; {personal.domain}
        </p>
        <div className="flex items-center gap-6">
          <a href={personal.github}  target="_blank" rel="noreferrer"
            className="font-mono text-xs text-white/30 hover:text-[var(--accent)] transition-colors tracking-wider uppercase"
            style={{ cursor: "none" }}>GitHub</a>
          <a href={personal.linkedin} target="_blank" rel="noreferrer"
            className="font-mono text-xs text-white/30 hover:text-[var(--accent)] transition-colors tracking-wider uppercase"
            style={{ cursor: "none" }}>LinkedIn</a>
          <a href={personal.tableau} target="_blank" rel="noreferrer"
            className="font-mono text-xs text-white/30 hover:text-[var(--accent)] transition-colors tracking-wider uppercase"
            style={{ cursor: "none" }}>Tableau</a>
        </div>
      </div>
    </footer>
  );
}
