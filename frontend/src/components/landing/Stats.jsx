const stats = [
  {
    icon: "🔎",
    value: "10,000+",
    label: "Links Analyzed",
    detail: "Audit crawlable links across real site structures.",
  },
  {
    icon: "⚡",
    value: "Async",
    label: "Concurrent Crawling",
    detail: "Fast, respectful crawling with safety limits.",
  },
  {
    icon: "🕸️",
    value: "Visual",
    label: "Interactive Site Graphs",
    detail: "See how pages connect across your website.",
  },
  {
    icon: "📄",
    value: "CSV",
    label: "Audit Reports",
    detail: "Export crawl findings for sharing and review.",
  },
];

export default function Stats() {
  return (
    <section className="landing-section landing-stats">
      {stats.map(({ icon, value, label, detail }) => (
        <div className="landing-stat" key={label}>
          <span className="stat-icon" aria-hidden="true">{icon}</span>
          <strong>{value}</strong>
          <span>{label}</span>
          <p>{detail}</p>
        </div>
      ))}
    </section>
  );
}
