export default function Footer({ onLaunch }) {
  return (
    <footer className="landing-footer">
      <div className="footer-brand">
        <span>WebScope</span>
        <p>Website intelligence for crawl health, SEO checks, link issues, performance, and reporting.</p>
      </div>
      <div className="footer-links" aria-label="Footer links">
        <a href="https://github.com/BarathThanigai/Concurrent_Web_Crawler" target="_blank" rel="noopener noreferrer">GitHub</a>
        <a href="#">Roadmap</a>
        <button onClick={onLaunch}>Launch App</button>
      </div>
      <div className="footer-meta">
        <span>Built with React + FastAPI</span>
        <small>&copy; {new Date().getFullYear()} WebScope. All rights reserved.</small>
      </div>
    </footer>
  );
}
