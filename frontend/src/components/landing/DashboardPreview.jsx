export default function DashboardPreview({ onLaunch }) {
  return (
    <section className="landing-section dashboard-preview">
      <div className="dashboard-preview-copy">
        <p className="eyebrow">Dashboard</p>
        <h2>Audit workspace preview</h2>
        <p>
          Review crawl health, SEO gaps, link issues, performance, and site structure in one
          focused workspace before exporting your audit.
        </p>
        <button className="primary" onClick={onLaunch}>Launch App</button>
      </div>

      <div className="preview-box dashboard-mock" aria-label="Static WebScope dashboard preview">
        <div className="mock-topbar">
          <div>
            <span>Audit Overview</span>
            <strong>books.toscrape.com</strong>
          </div>
          <span className="mock-status">Complete</span>
        </div>

        <div className="mock-summary">
          <div className="mock-health">
            <span>Health Score</span>
            <strong>96%</strong>
          </div>
          <div className="mock-metric">
            <span>SEO Issues</span>
            <strong>4</strong>
          </div>
          <div className="mock-metric">
            <span>Link Issues</span>
            <strong>1</strong>
          </div>
          <div className="mock-metric">
            <span>Avg Response</span>
            <strong>586ms</strong>
          </div>
        </div>

        <div className="mock-content-grid">
          <div className="mock-panel">
            <div className="mock-panel-heading">
              <span>SEO Breakdown</span>
              <strong>3 checks</strong>
            </div>
            <div className="mock-bar"><span style={{ width: "82%" }}></span></div>
            <div className="mock-row"><span>Missing descriptions</span><strong>2</strong></div>
            <div className="mock-row"><span>Missing H1 tags</span><strong>1</strong></div>
            <div className="mock-row"><span>Missing titles</span><strong>1</strong></div>
          </div>

          <div className="mock-panel">
            <div className="mock-panel-heading">
              <span>Mini Site Graph</span>
              <strong>24 pages</strong>
            </div>
            <div className="mock-site-graph" aria-hidden="true">
              <svg viewBox="0 0 240 138" role="img">
                <path d="M52 70 L118 34 L118 104 L188 70" />
                <path d="M118 34 L188 70 L118 104" />
              </svg>
              <span className="mock-node node-one"></span>
              <span className="mock-node node-two"></span>
              <span className="mock-node node-three"></span>
              <span className="mock-node node-four"></span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
