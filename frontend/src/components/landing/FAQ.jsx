const faqs = [
  [
    "Does WebScope crawl every website?",
    "No. It audits publicly crawlable pages and respects crawl limits, robots.txt, and sites that block automated requests.",
  ],
  [
    "Why do some links work in browser but show crawler-inaccessible?",
    "Some pages require cookies, authentication, special headers, or anti-bot checks that a respectful crawler should not bypass.",
  ],
  [
    "Does WebScope support JavaScript-rendered websites?",
    "WebScope analyzes server-returned HTML. JavaScript-heavy pages may need a future browser-rendered crawling mode.",
  ],
  [
    "Can I export reports?",
    "Yes. Crawl results can be exported as CSV for sharing, documentation, and spreadsheet analysis.",
  ],
  [
    "Is WebScope safe and respectful of robots.txt?",
    "Yes. WebScope checks robots.txt, applies request timeouts, uses crawl limits, and avoids aggressive crawling by default.",
  ],
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
          <article className="landing-card faq-card" key={question}>
            <h3>{question}</h3>
            <p>{answer}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
