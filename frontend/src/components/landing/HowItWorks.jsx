const steps = [
  "Enter a public seed URL",
  "Choose safe crawl limits",
  "Run the audit",
  "Review reports, pages, graph, and exports",
];

export default function HowItWorks() {
  return (
    <section className="landing-section" id="how-it-works">
      <div className="landing-section-header">
        <p className="eyebrow">Workflow</p>
        <h2>How it works</h2>
      </div>
      <div className="landing-steps">
        {steps.map((step, index) => (
          <article className="landing-card" key={step}>
            <span className="step-number">{index + 1}</span>
            <h3>{step}</h3>
          </article>
        ))}
      </div>
    </section>
  );
}
