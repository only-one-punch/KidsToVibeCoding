import { motion } from 'motion/react';
import { BookOpen, Rocket, MoreHorizontal, Trophy, X, Plus } from 'lucide-react';
import { Button, GlassCard } from '@/src/components/UI';

export function DashboardView() {
  return (
    <main className="pt-32 pb-10 px-8 max-w-7xl mx-auto w-full">
      <header className="mb-12 flex justify-between items-end">
        <div>
          <h2 className="text-5xl font-serif text-white italic text-glow leading-none mb-2">天眼监控报告</h2>
          <p className="text-on-surface-variant tracking-wide opacity-80">Guardian Oversight Dashboard — Session ID: ASTR-092</p>
        </div>
        <div className="hidden md:flex items-center gap-4">
          <div className="text-right">
            <p className="text-xs text-on-surface-variant font-bold uppercase tracking-tighter">Active Guardian</p>
            <p className="text-sm text-secondary">Alex Rivers</p>
          </div>
          <div className="w-12 h-12 rounded-full border-2 border-secondary/30 p-1">
            <img 
              src="https://picsum.photos/seed/guardian/100/100" 
              alt="Guardian" 
              className="w-full h-full rounded-full object-cover"
              referrerPolicy="no-referrer"
            />
          </div>
        </div>
      </header>

      <div className="grid grid-cols-12 gap-6">
        {/* Evolution Report */}
        <section className="col-span-12 lg:col-span-7 space-y-6">
          <GlassCard className="relative overflow-hidden group p-8">
            <div className="absolute top-0 right-0 w-64 h-64 bg-primary/5 rounded-full blur-3xl -mr-32 -mt-32" />
            <div className="flex justify-between items-start mb-10">
              <div>
                <span className="text-xs font-bold text-primary uppercase tracking-[0.2em] mb-2 block">Evolution Insights</span>
                <h3 className="text-3xl font-serif italic text-white leading-tight">成长进化曲线报告</h3>
              </div>
              <div className="flex gap-2">
                <span className="px-3 py-1 rounded-full bg-primary/10 text-primary text-[10px] font-bold border border-primary/20">WEEKLY</span>
                <span className="px-3 py-1 rounded-full bg-surface-bright/20 text-on-surface-variant text-[10px] font-bold">MONTHLY</span>
              </div>
            </div>
            
            <div className="h-64 w-full relative">
              <svg className="w-full h-full overflow-visible" viewBox="0 0 100 40">
                <path 
                  d="M0,35 Q10,32 20,20 T40,15 T60,25 T80,5 T100,12" 
                  fill="none" 
                  stroke="url(#line-glow)" 
                  strokeWidth="0.8"
                  className="drop-shadow-[0_0_8px_rgba(229,180,255,0.5)]"
                />
                <defs>
                  <linearGradient id="line-glow" x1="0" x2="1" y1="0" y2="0">
                    <stop offset="0%" stopColor="#e5b4ff" />
                    <stop offset="100%" stopColor="#7cfffe" />
                  </linearGradient>
                </defs>
              </svg>
              <div className="absolute inset-0 flex items-end justify-between px-2 pt-4">
                {['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'].map(day => (
                  <span key={day} className={cn("text-[9px] font-bold", day === 'SAT' ? "text-primary" : "text-on-surface-variant/40")}>
                    {day}
                  </span>
                ))}
              </div>
            </div>
          </GlassCard>

          <GlassCard className="p-8">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-xl font-bold text-white">Activity History / 活动轨迹</h3>
              <MoreHorizontal className="text-on-surface-variant cursor-pointer hover:text-white transition-colors" />
            </div>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-4 rounded-xl bg-surface-container-low/40 hover:bg-surface-container-high transition-all">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-full bg-secondary/10 flex items-center justify-center">
                    <BookOpen className="text-secondary" size={16} />
                  </div>
                  <div>
                    <h4 className="text-sm font-bold text-white">在线学习终端</h4>
                    <p className="text-xs text-on-surface-variant">Mathematics Exploration Module</p>
                  </div>
                </div>
                <div className="text-right">
                  <span className="px-3 py-1 rounded-full bg-secondary/20 text-secondary text-[10px] font-black uppercase tracking-widest border border-secondary/20">In Progress</span>
                  <p className="text-[10px] text-on-surface-variant/50 mt-1 italic">Started 12m ago</p>
                </div>
              </div>

              <div className="flex items-center justify-between p-4 rounded-xl bg-surface-container-low/40 hover:bg-surface-container-high transition-all">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center">
                    <Rocket className="text-primary" size={16} />
                  </div>
                  <div>
                    <h4 className="text-sm font-bold text-white">星际迷航游戏</h4>
                    <p className="text-xs text-on-surface-variant">Galactic Conquest Simulator</p>
                  </div>
                </div>
                <div className="text-right">
                  <span className="px-3 py-1 rounded-full bg-surface-bright/40 text-on-surface-variant text-[10px] font-black uppercase tracking-widest">Completed</span>
                  <p className="text-[10px] text-on-surface-variant/50 mt-1 italic">Duration: 45m</p>
                </div>
              </div>
            </div>
          </GlassCard>
        </section>

        {/* Usage Limit */}
        <section className="col-span-12 lg:col-span-5 space-y-6">
          <GlassCard className="p-10 text-center flex flex-col items-center justify-center bg-gradient-to-br from-surface-container-high to-surface-container-lowest border-primary/10">
            <span className="text-[10px] font-black text-secondary tracking-[0.3em] uppercase mb-4">Current Usage Limit</span>
            <div className="relative mb-6">
              <svg className="w-48 h-48 transform -rotate-90">
                <circle className="text-surface-container-highest" cx="96" cy="96" fill="transparent" r="88" stroke="currentColor" strokeWidth="4" />
                <circle 
                  className="text-secondary drop-shadow-[0_0_8px_rgba(124,255,254,0.5)]" 
                  cx="96" cy="96" fill="transparent" r="88" stroke="currentColor" 
                  strokeWidth="6" strokeDasharray="552.92" strokeDashoffset="138.23" 
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className="text-6xl font-serif italic text-white leading-none">01:42</span>
                <span className="text-xs text-secondary/60 font-bold tracking-widest mt-1">REMAINING</span>
              </div>
            </div>
            <div className="w-full space-y-6 mt-4">
              <div className="flex justify-between items-center px-2">
                <h4 className="text-sm font-bold text-white">每日使用时限</h4>
                <span className="text-lg font-serif italic text-primary">60 分钟</span>
              </div>
              <div className="relative h-2 w-full bg-surface-container-highest rounded-full">
                <div className="absolute h-full bg-gradient-to-r from-primary to-secondary w-[70%] rounded-full" />
              </div>
              <div className="flex justify-between text-[10px] text-on-surface-variant font-bold tracking-tighter opacity-50 uppercase">
                <span>轻松模式</span>
                <span>推荐时长</span>
                <span>极限挑战</span>
              </div>
            </div>
          </GlassCard>

          <div className="grid grid-cols-2 gap-4">
            <GlassCard className="p-6 border-l-4 border-tertiary">
              <p className="text-[10px] font-bold text-on-surface-variant uppercase mb-1">Focus Score</p>
              <p className="text-2xl font-serif italic text-tertiary">88%</p>
            </GlassCard>
            <GlassCard className="p-6 border-l-4 border-secondary">
              <p className="text-[10px] font-bold text-on-surface-variant uppercase mb-1">Total Screen</p>
              <p className="text-2xl font-serif italic text-secondary">2.1h</p>
            </GlassCard>
          </div>
        </section>

        {/* Milestone Banner */}
        <section className="col-span-12 mt-4">
          <div className="relative rounded-lg overflow-hidden bg-surface-container-low p-8 border border-primary/20 group">
            <div className="absolute inset-0 bg-gradient-to-r from-primary/10 via-transparent to-secondary/10 opacity-50" />
            <div className="relative flex flex-col md:flex-row items-center justify-between gap-8">
              <div className="flex items-center gap-6">
                <div className="w-20 h-20 rounded-full bg-surface-container-highest flex items-center justify-center relative">
                  <Trophy className="text-tertiary" size={40} />
                  <div className="absolute -inset-1 rounded-full border border-tertiary/40 animate-pulse" />
                </div>
                <div>
                  <h3 className="text-3xl font-serif italic text-white">里程碑已解锁：数学专家</h3>
                  <p className="text-on-surface-variant text-sm mt-1 max-w-md">达成连续 7 天完成每日逻辑挑战。奖励系统已就绪，等待守护者确认发放。</p>
                </div>
              </div>
              <div className="flex items-center gap-4">
                <Button className="px-8 py-4 text-sm shadow-xl shadow-primary/20">
                  Send Reward / 发放奖励
                </Button>
                <button className="w-14 h-14 rounded-full border border-white/10 flex items-center justify-center hover:bg-white/5 transition-colors">
                  <X className="text-on-surface-variant" />
                </button>
              </div>
            </div>
          </div>
        </section>
      </div>

      <button className="fixed bottom-10 right-10 w-16 h-16 rounded-full bg-gradient-to-br from-tertiary to-tertiary-container text-surface shadow-[0_0_30px_rgba(255,184,117,0.4)] flex items-center justify-center hover:scale-110 active:scale-90 transition-all z-[100]">
        <Plus size={32} />
      </button>
    </main>
  );
}

import { cn } from '@/src/lib/utils';
