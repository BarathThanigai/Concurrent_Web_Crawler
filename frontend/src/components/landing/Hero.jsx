export default function Hero({ onLaunch }) {
  return (
    <section className="landing-hero" id="top">
      <div>
        <p className="eyebrow">Website Intelligence & Audit Platform</p>
        <h1>Audit crawlability, SEO, performance, and link health.</h1>
        <p>
          WebScope helps developers inspect publicly crawlable websites with a practical audit dashboard,
          crawl reports, CSV exports, and site graph visualization.
        </p>
        <div className="landing-actions">
          <button className="primary" onClick={onLaunch}>Launch App</button>
          <a href="#features">Explore features</a>
        </div>
      </div>
      <div className="hero-panel">
        <span>Preview</span>
        <strong>Health Score</strong>
        <p>Link issues, SEO metadata gaps, slow pages, and robots-aware crawl results in one place.</p>
      </div>
    </section>
  );
}
