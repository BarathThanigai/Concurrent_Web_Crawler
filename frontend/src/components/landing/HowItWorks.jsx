const steps = [
  {
    title: "Enter Website URL",
    description: "Start with any publicly crawlable website and choose safe crawl limits.",
  },
  {
    title: "WebScope Crawls Pages",
    description: "The crawler follows internal links concurrently while respecting robots.txt.",
  },
  {
    title: "Analyze SEO & Performance",
    description: "Titles, descriptions, headings, status codes, and response times are audited.",
  },
  {
    title: "Visualize Site Graph",
    description: "See how discovered pages connect and quickly spot crawl structure issues.",
  },
  {
    title: "Export Audit Report",
    description: "Download CSV results for documentation, handoff, or deeper analysis.",
  },
];

export default function HowItWorks() {
  return (
    <section className="landing-section" id="how-it-works">
      <div className="landing-section-header">
        <p className="eyebrow">Workflow</p>
        <h2>How it works</h2>
      </div>
      <div className="landing-steps how-steps">
        {steps.map((step, index) => (
          <article className="landing-card workflow-card" key={step.title}>
            <span className="step-number">{index + 1}</span>
            <h3>{step.title}</h3>
            <p>{step.description}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
