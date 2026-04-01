import { Link, useLocation } from 'react-router-dom';
import { Sparkles, Bell, User } from 'lucide-react';
import { cn } from '@/src/lib/utils';

export function TopNav() {
  const location = useLocation();
  
  const navItems = [
    { label: 'Gallery', path: '/gallery' },
    { label: 'Showcase', path: '/showcase' },
    { label: 'Explorer', path: '/explorer' },
    { label: 'Dashboard', path: '/dashboard' },
    { label: 'Summon', path: '/summon' },
    { label: 'Lab', path: '/lab' },
  ];

  return (
    <header className="fixed top-0 w-full flex justify-between items-center px-6 h-16 bg-surface/80 backdrop-blur-2xl z-50 border-b border-white/5">
      <div className="flex items-center gap-8">
        <Link to="/" className="text-xl font-bold bg-gradient-to-br from-primary to-primary-container bg-clip-text text-transparent drop-shadow-[0_0_10px_rgba(229,180,255,0.4)] font-headline tracking-tight">
          CodeBuddyAI
        </Link>
        <nav className="hidden md:flex gap-6">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={cn(
                "text-xs font-medium tracking-tight transition-all duration-300 pb-1",
                location.pathname === item.path 
                  ? "text-primary border-b-2 border-primary" 
                  : "text-on-surface-variant hover:text-on-surface"
              )}
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20">
          <span className="text-primary">💎</span>
          <span className="text-sm font-bold text-primary">1,200</span>
        </div>
        <button className="text-on-surface-variant hover:text-primary transition-colors">
          <Sparkles size={18} />
        </button>
        <button className="text-on-surface-variant hover:text-primary transition-colors">
          <Bell size={18} />
        </button>
        <div className="w-8 h-8 rounded-full bg-surface-container-high overflow-hidden border border-white/10">
          <img 
            src="https://picsum.photos/seed/avatar/100/100" 
            alt="Avatar" 
            className="w-full h-full object-cover"
            referrerPolicy="no-referrer"
          />
        </div>
      </div>
    </header>
  );
}
