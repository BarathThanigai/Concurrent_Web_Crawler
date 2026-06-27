export default function Footer({ onLaunch }) {
  return (
    <footer className="landing-footer">
      <span>WebScope</span>
      <button onClick={onLaunch}>Launch App</button>
    </footer>
  );
}
