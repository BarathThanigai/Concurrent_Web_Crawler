import Navbar from "./Navbar";
import Hero from "./Hero";
import Stats from "./Stats";
import Features from "./Features";
import HowItWorks from "./HowItWorks";
import DashboardPreview from "./DashboardPreview";
import WhyWebScope from "./WhyWebScope";
import TechStack from "./TechStack";
import FAQ from "./FAQ";
import Footer from "./Footer";

export default function LandingPage({ onLaunch }) {
  return (
    <main className="landing-page">
      <Navbar onLaunch={onLaunch} />
      <Hero onLaunch={onLaunch} />
      <Stats />
      <Features />
      <HowItWorks />
      <DashboardPreview onLaunch={onLaunch} />
      <WhyWebScope />
      <TechStack />
      <FAQ />
      <Footer onLaunch={onLaunch} />
    </main>
  );
}
