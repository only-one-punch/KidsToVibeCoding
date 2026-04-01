import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { TopNav } from './components/TopNav';
import { LandingView } from './views/LandingView';
import { OnboardingView } from './views/OnboardingView';
import { ExplorerView } from './views/ExplorerView';
import { DashboardView } from './views/DashboardView';
import { SummonView } from './views/SummonView';
import { ClassroomView } from './views/ClassroomView';
import { GalleryView } from './views/GalleryView';
import { UserProvider } from './store/useUserStore';

export default function App() {
  return (
    <UserProvider>
      <Router>
      <div className="min-h-screen flex flex-col">
        <TopNav />
        
        <div className="flex-1 pt-16">
          <Routes>
            <Route path="/" element={<LandingView />} />
            <Route path="/onboarding" element={<OnboardingView />} />
            <Route path="/explorer" element={<ExplorerView />} />
            <Route path="/dashboard" element={<DashboardView />} />
            <Route path="/summon" element={<SummonView />} />
            <Route path="/lab" element={<ClassroomView />} />
            <Route path="/gallery" element={<GalleryView />} />
            <Route path="/showcase" element={<GalleryView />} /> {/* Reusing gallery for showcase */}
          </Routes>
        </div>

        <footer className="py-8 bg-surface-container-lowest/30 border-t border-white/5 backdrop-blur-sm">
          <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
            <div className="flex items-center gap-3">
              <span className="text-lg font-bold tracking-tighter text-primary/80 font-headline">CodeBuddyAI</span>
              <span className="text-on-surface-variant/40 text-xs">© 2026 Astral Architect Lab</span>
            </div>
            <div className="flex gap-8 text-[10px] font-bold tracking-[0.2em] text-on-surface-variant/50">
              <Link to="#" className="hover:text-primary transition-colors">TERMS</Link>
              <Link to="#" className="hover:text-primary transition-colors">PRIVACY</Link>
              <Link to="#" className="hover:text-primary transition-colors">MANIFESTO</Link>
            </div>
            <p className="text-on-surface-variant/30 text-[9px] uppercase tracking-[0.3em]">Summoned with Magic</p>
          </div>
        </footer>
      </div>
    </Router>
    </UserProvider>
  );
}
