const problems = [
  {
    title: "Manual audits are slow",
    description: "Replacing scattered checks with one crawl report helps teams move from discovery to decisions faster.",
  },
  {
    title: "Broken links hurt UX",
    description: "Link issue classification separates true broken pages from crawler-inaccessible or server-side failures.",
  },
  {
    title: "Missing SEO metadata affects visibility",
    description: "WebScope flags missing titles, descriptions, and H1 tags so pages are easier to prioritize.",
  },
  {
    title: "Slow pages reduce engagement",
    description: "Response-time analysis highlights slow pages before performance issues become user-facing friction.",
  },
];

export default function WhyWebScope() {
  return (
    <section className="landing-section why-webscope">
      <div className="landing-section-header why-copy">
        <p className="eyebrow">Why WebScope</p>
        <h2>A focused crawler for portfolio-grade auditing</h2>
        <p className="landing-copy">
          WebScope turns crawl data into practical website intelligence, giving developers a clear
          view of health, visibility, performance, and link quality.
        </p>
      </div>
      <div className="why-grid">
        {problems.map((problem) => (
          <article className="landing-card why-card" key={problem.title}>
            <h3>{problem.title}</h3>
            <p>{problem.description}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
