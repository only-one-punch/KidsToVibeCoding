import { motion } from 'motion/react';
import { Sparkles, Bolt } from 'lucide-react';
import { Button, GlassCard } from '@/src/components/UI';
import { useNavigate } from 'react-router-dom';
import { cn } from '@/src/lib/utils';

export function OnboardingView() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex items-center justify-center p-6 pt-24">
      <main className="relative w-full max-w-4xl flex flex-col md:flex-row gap-8 items-stretch">
        {/* Left Side: Branding */}
        <div className="hidden md:flex flex-col justify-between w-1/3 p-8 rounded-lg bg-surface-container-low/30 backdrop-blur-md">
          <div>
            <h1 className="font-serif text-4xl text-primary drop-shadow-[0_0_15px_rgba(229,180,255,0.4)] leading-none mb-2">CodeBuddyAI</h1>
            <p className="text-[10px] tracking-[0.2em] text-secondary/60 uppercase font-bold">Dream Spark Edition</p>
          </div>
          
          <div className="relative aspect-square rounded-full overflow-hidden border border-primary/20 p-2">
            <img 
              src="https://picsum.photos/seed/soul/400/400" 
              alt="Identity" 
              className="w-full h-full object-cover rounded-full opacity-80 mix-blend-lighten"
              referrerPolicy="no-referrer"
            />
          </div>

          <div className="flex items-center gap-3">
            <Sparkles className="text-primary" size={20} />
            <p className="text-sm text-on-surface-variant">在此刻，定义你的数字灵魂。</p>
          </div>
        </div>

        {/* Right Side: Form */}
        <GlassCard className="flex-1 p-8 md:p-12 relative overflow-hidden">
          <div className="absolute -top-12 -right-12 w-32 h-32 bg-primary/10 rounded-full blur-3xl" />
          
          <header className="mb-10">
            <h2 className="text-3xl font-extrabold tracking-tight text-on-surface mb-2">身份设定</h2>
            <div className="h-1 w-12 bg-primary rounded-full" />
          </header>

          <form className="space-y-8" onSubmit={(e) => { e.preventDefault(); navigate('/explorer'); }}>
            <div className="group">
              <label className="block text-xs uppercase tracking-widest text-on-surface-variant mb-2 ml-1">姓名 (NAME)</label>
              <input 
                type="text" 
                placeholder="输入你的代号..."
                className="w-full bg-transparent border-0 border-b-2 border-white/10 py-3 px-1 text-lg text-primary focus:ring-0 focus:outline-none focus:border-primary transition-all duration-300 placeholder:text-on-surface-variant/30"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="group">
                <label className="block text-xs uppercase tracking-widest text-on-surface-variant mb-2 ml-1">年龄段 (ERA)</label>
                <select className="w-full bg-transparent border-0 border-b-2 border-white/10 py-3 px-1 text-lg text-primary focus:ring-0 focus:outline-none focus:border-primary transition-all duration-300 appearance-none">
                  <option className="bg-surface">6-9 岁 (探索期)</option>
                  <option className="bg-surface">10-14 岁 (成长期)</option>
                </select>
              </div>
              <div className="group">
                <label className="block text-xs uppercase tracking-widest text-on-surface-variant mb-2 ml-1">邮箱 (EMAIL)</label>
                <input 
                  type="email" 
                  placeholder="architect@nexus.com"
                  className="w-full bg-transparent border-0 border-b-2 border-white/10 py-3 px-1 text-lg text-primary focus:ring-0 focus:outline-none focus:border-primary transition-all duration-300 placeholder:text-on-surface-variant/30"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs uppercase tracking-widest text-on-surface-variant mb-4 ml-1">专注领域 (FOCUS AREA)</label>
              <div className="grid grid-cols-2 gap-4">
                {[
                  { name: '网页建筑师', nameEn: 'Architecture', icon: '🌐', desc: 'Web' },
                  { name: '游戏逻辑师', nameEn: 'Logic', icon: '🎮', desc: 'Game' },
                ].map((area, i) => (
                  <div
                    key={area.name}
                    className={cn(
                      "cursor-pointer p-4 rounded-xl border transition-all duration-300 text-center",
                      i === 0 ? "border-primary bg-primary/5" : "border-white/10 bg-surface-container-highest/20 hover:bg-surface-container-highest/50"
                    )}
                  >
                    <span className="text-2xl mb-2 block">{area.icon}</span>
                    <span className="text-sm font-medium text-on-surface block">{area.name}</span>
                    <span className="text-xs text-on-surface-variant/60">{area.nameEn} ({area.desc})</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-6 flex flex-col items-center gap-6">
              <Button type="submit" className="w-full py-5 text-xl flex items-center justify-center gap-3">
                创建账号 <Bolt size={24} />
              </Button>
              <p className="text-xs text-on-surface-variant/60 text-center">
                点击创建即代表你同意我们的 <a href="#" className="text-primary hover:underline">虚空条约</a> 与 <a href="#" className="text-primary hover:underline">星界隐私协议</a>
              </p>
            </div>
          </form>
        </GlassCard>
      </main>
    </div>
  );
}
