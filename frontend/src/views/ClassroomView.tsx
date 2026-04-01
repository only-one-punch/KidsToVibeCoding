import { Play, Volume2, Maximize2, Terminal, Sparkles } from 'lucide-react';
import { GlassCard } from '@/src/components/UI';
import { cn } from '@/src/lib/utils';

export function ClassroomView() {
  const steps = [
    { id: '01', title: '1. 打开 Figma Studio', active: false },
    { id: '02', title: '2. 定义 1440x900', active: true },
    { id: '03', title: '3. 创建图层', active: false },
  ];

  return (
    <main className="pt-32 pb-12 px-8 lg:px-16 min-h-screen relative">
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12">
        <div className="lg:col-span-8 space-y-8">
          <div className="space-y-2">
            <h1 className="text-4xl font-extrabold text-primary text-glow">专注课堂</h1>
            <p className="text-on-surface-variant font-medium opacity-80">当前召唤: UI 架构设计</p>
          </div>

          <div className="relative group aspect-video rounded-lg overflow-hidden bg-surface-container-lowest shadow-2xl">
            <img 
              src="https://picsum.photos/seed/workspace/1200/800" 
              alt="Workspace" 
              className="w-full h-full object-cover"
              referrerPolicy="no-referrer"
            />
            <div className="absolute inset-0 flex flex-col justify-end p-6 bg-gradient-to-t from-surface/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div className="flex items-center justify-between gap-4 mb-4">
                <div className="flex items-center gap-4">
                  <Play size={20} className="text-white cursor-pointer hover:text-primary transition-colors" />
                  <Volume2 size={20} className="text-white cursor-pointer hover:text-primary transition-colors" />
                  <span className="text-xs text-white/80">12:45 / 24:00</span>
                </div>
                <Maximize2 size={20} className="text-white cursor-pointer hover:text-primary transition-colors" />
              </div>
              <div className="h-1.5 w-full bg-white/10 rounded-full overflow-hidden relative">
                <div className="absolute top-0 left-0 h-full w-1/2 bg-gradient-to-r from-primary to-secondary rounded-full shadow-[0_0_20px_rgba(229,180,255,0.3)]" />
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <GlassCard className="p-8">
              <h3 className="text-lg font-bold text-secondary mb-4 flex items-center gap-2">
                <Terminal size={18} />
                实时架构注释
              </h3>
              <p className="text-sm leading-relaxed text-on-surface-variant">
                正在使用 <span className="text-primary">CodeBuddyAI</span> 生成响应式网格。自动调整画布比例以适应 1440px 视口，同时保持比例连贯性。
              </p>
            </GlassCard>
            <GlassCard className="p-8">
              <h3 className="text-lg font-bold text-secondary mb-4 flex items-center gap-2">
                <Sparkles size={18} />
                魔法建议
              </h3>
              <p className="text-sm leading-relaxed text-on-surface-variant">
                通过增加 <span className="text-primary">24px</span> 的背景模糊值，可以提升图层的深度感。
              </p>
            </GlassCard>
          </div>
        </div>

        <div className="lg:col-span-4 flex flex-col gap-8">
          <GlassCard className="p-10 sticky top-32 shadow-2xl">
            <div className="mb-10">
              <span className="text-primary text-xs font-bold tracking-[0.2em] uppercase">Phase Execution</span>
              <h2 className="text-3xl font-extrabold mt-2 text-primary">阶段 03: 画布</h2>
            </div>
            <ul className="space-y-4">
              {steps.map((step) => (
                <li 
                  key={step.id}
                  className={cn(
                    "flex items-center gap-6 px-6 py-4 rounded-xl transition-all cursor-pointer",
                    step.active 
                      ? "bg-surface-container-high/80 border-l-4 border-primary shadow-[inset_0_0_20px_rgba(229,180,255,0.15)]" 
                      : "text-on-surface-variant/40 hover:bg-white/5"
                  )}
                >
                  <div className={cn(
                    "w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm",
                    step.active ? "bg-primary text-surface" : "border border-white/10"
                  )}>
                    {step.id}
                  </div>
                  <span className={cn("font-medium text-lg", step.active ? "text-primary font-bold" : "")}>
                    {step.title}
                  </span>
                </li>
              ))}
            </ul>
            <div className="mt-12 flex flex-col gap-6">
              <button className="w-full py-5 px-8 rounded-full bg-gradient-to-br from-primary to-primary-container text-surface font-bold text-xl transition-all duration-300 active:scale-95 shadow-[0_0_30px_rgba(229,180,255,0.4)] hover:shadow-[0_0_50px_rgba(229,180,255,0.6)]">
                标记完成
              </button>
              <p className="text-center text-xs text-on-surface-variant/40 tracking-widest uppercase">
                点击召唤下一个阶段
              </p>
            </div>
          </GlassCard>
        </div>
      </div>
    </main>
  );
}
