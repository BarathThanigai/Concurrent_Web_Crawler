const features = [
  {
    icon: "⚡",
    title: "Concurrent Crawling",
    description: "Scan pages efficiently with asyncio-powered crawling, depth limits, retries, and crawl-delay safeguards.",
  },
  {
    icon: "🏷️",
    title: "SEO Metadata Analysis",
    description: "Extract titles, descriptions, H1 tags, canonicals, word counts, and missing metadata flags.",
  },
  {
    icon: "🔗",
    title: "Link Issue Detection",
    description: "Classify true broken links, inaccessible pages, server errors, rate limits, and redirect issues.",
  },
  {
    icon: "⏱️",
    title: "Performance Monitoring",
    description: "Track response times, identify slow pages, and surface average, minimum, and maximum timings.",
  },
  {
    icon: "🕸️",
    title: "Interactive Site Graph",
    description: "Explore crawled pages and internal link relationships with a visual graph built for quick inspection.",
  },
  {
    icon: "📄",
    title: "CSV Report Export",
    description: "Download audit-ready crawl data for documentation, handoffs, and deeper spreadsheet analysis.",
  },
];

export default function Features() {
  return (
    <section className="landing-section" id="features">
      <div className="landing-section-header">
        <p className="eyebrow">Features</p>
        <h2>Built for practical website audits</h2>
      </div>
      <div className="landing-grid">
        {features.map(({ icon, title, description }) => (
          <article className="landing-card feature-card" key={title}>
            <span className="feature-icon" aria-hidden="true">{icon}</span>
            <h3>{title}</h3>
            <p>{description}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
