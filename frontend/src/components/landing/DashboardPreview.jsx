export default function DashboardPreview({ onLaunch }) {
  return (
    <section className="landing-section dashboard-preview">
      <div>
        <p className="eyebrow">Dashboard</p>
        <h2>Audit workspace preview</h2>
        <p>
          The app includes overview metrics, crawled pages, link issues, SEO issues, performance,
          and an interactive site graph.
        </p>
        <button className="primary" onClick={onLaunch}>Launch App</button>
      </div>
      <div className="preview-box">
        <div className="preview-row"></div>
        <div className="preview-row short"></div>
        <div className="preview-grid">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </section>
  );
}
