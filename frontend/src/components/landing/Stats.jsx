const stats = [
  ["200", "max pages per crawl"],
  ["3", "max crawl depth"],
  ["20", "max concurrency"],
  ["CSV", "export ready"],
];

export default function Stats() {
  return (
    <section className="landing-section landing-stats">
      {stats.map(([value, label]) => (
        <div className="landing-stat" key={label}>
          <strong>{value}</strong>
          <span>{label}</span>
        </div>
      ))}
    </section>
  );
}
