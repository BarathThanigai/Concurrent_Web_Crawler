const features = [
  "Robots-aware concurrent crawling",
  "SEO metadata extraction",
  "Link issue classification",
  "Performance and slow page analysis",
  "Interactive site graph",
  "CSV crawl report export",
];

export default function Features() {
  return (
    <section className="landing-section" id="features">
      <div className="landing-section-header">
        <p className="eyebrow">Features</p>
        <h2>Built for practical website audits</h2>
      </div>
      <div className="landing-grid">
        {features.map((feature) => (
          <article className="landing-card" key={feature}>
            <h3>{feature}</h3>
            <p>Placeholder copy for this audit capability.</p>
          </article>
        ))}
      </div>
    </section>
  );
}
