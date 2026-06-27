const stack = ["FastAPI", "SQLite", "aiohttp", "BeautifulSoup", "React", "Vite", "React Flow", "Docker"];

export default function TechStack() {
  return (
    <section className="landing-section" id="tech-stack">
      <div className="landing-section-header">
        <p className="eyebrow">Tech Stack</p>
        <h2>Modern full-stack project foundation</h2>
      </div>
      <div className="tech-list">
        {stack.map((item) => <span key={item}>{item}</span>)}
      </div>
    </section>
  );
}
