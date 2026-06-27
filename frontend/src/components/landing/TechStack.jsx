const stack = [
  { name: "React", role: "Frontend UI" },
  { name: "Vite", role: "Fast builds" },
  { name: "FastAPI", role: "Backend API" },
  { name: "Python", role: "Crawler logic" },
  { name: "asyncio", role: "Concurrency" },
  { name: "aiohttp", role: "Async requests" },
  { name: "BeautifulSoup", role: "HTML parsing" },
  { name: "SQLite", role: "Local storage" },
  { name: "React Flow", role: "Site graph" },
];

export default function TechStack() {
  return (
    <section className="landing-section" id="tech-stack">
      <div className="landing-section-header">
        <p className="eyebrow">Tech Stack</p>
        <h2>Modern full-stack project foundation</h2>
      </div>
      <div className="tech-list">
        {stack.map((item) => (
          <article className="tech-card" key={item.name}>
            <span>{item.name}</span>
            <small>{item.role}</small>
          </article>
        ))}
      </div>
    </section>
  );
}
