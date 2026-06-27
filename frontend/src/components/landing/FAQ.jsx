const faqs = [
  ["Does WebScope bypass robots.txt?", "No. WebScope audits publicly crawlable pages only."],
  ["Can I export results?", "Yes. Crawl results can be exported as CSV."],
  ["Is this production ready?", "It is structured for deployment and portfolio demonstration with room for roadmap improvements."],
];

export default function FAQ() {
  return (
    <section className="landing-section">
      <div className="landing-section-header">
        <p className="eyebrow">FAQ</p>
        <h2>Common questions</h2>
      </div>
      <div className="faq-list">
        {faqs.map(([question, answer]) => (
          <article className="landing-card" key={question}>
            <h3>{question}</h3>
            <p>{answer}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
