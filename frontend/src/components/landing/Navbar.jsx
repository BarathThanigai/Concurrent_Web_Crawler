export default function Navbar({ onLaunch }) {
  return (
    <header className="landing-navbar">
      <a className="landing-brand" href="#top">WebScope</a>
      <nav className="landing-links" aria-label="Landing navigation">
        <a href="#features">Features</a>
        <a href="#how-it-works">How it works</a>
        <a href="#tech-stack">Tech stack</a>
        <button className="primary" onClick={onLaunch}>Launch App</button>
      </nav>
    </header>
  );
}
