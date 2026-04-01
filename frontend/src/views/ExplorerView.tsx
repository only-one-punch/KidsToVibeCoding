import { motion } from 'motion/react';
import { Sparkles, Terminal, Layout, Rocket, Flame, Wand2 } from 'lucide-react';
import { Button, GlassCard } from '@/src/components/UI';
import { useNavigate } from 'react-router-dom';
import { cn } from '@/src/lib/utils';

export function ExplorerView() {
  const navigate = useNavigate();

  const paths = [
    {
      title: 'WEB 架构师',
      dimension: 'Dimension Alpha',
      desc: '从 Figma 设计稿到全球部署。掌握现代网站的完整构建流程。',
      img: 'https://picsum.photos/seed/web/800/1000',
      color: 'primary',
      duration: '12h',
      level: 5,
      recommended: true,
    },
    {
      title: '游戏引擎',
      dimension: 'Dimension Beta',
      desc: '构建你自己的数字物理世界。深入底层内存管理与实时渲染。',
      img: 'https://picsum.photos/seed/game/800/1000',
      color: 'secondary',
      duration: '15h',
      level: 7,
      isNew: true,
    }
  ];

  return (
    <div className="pt-32 pb-20 px-8 min-h-screen">
      <section className="max-w-7xl mx-auto">
        <header className="mb-16 space-y-4">
          <h1 className="text-5xl md:text-7xl font-serif font-bold italic tracking-tight text-glow leading-tight">
            选择你的 <span className="text-secondary">进化路径</span>
          </h1>
          <p className="text-on-surface-variant max-w-xl text-lg">
            不仅仅是学习，这是一次代码灵魂的升华。从两个平行的维度中选择一个，开启你的星际编码之旅。
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-16 lg:gap-24 mb-24">
          {paths.map((path) => (
            <motion.div 
              key={path.title}
              whileHover={{ y: -10 }}
              className="group relative bg-surface-container-high rounded-[40px] overflow-hidden transition-all duration-700 shadow-2xl"
            >
              <div className="h-[500px] w-full relative overflow-hidden">
                <img 
                  src={path.img} 
                  alt={path.title} 
                  className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110"
                  referrerPolicy="no-referrer"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-surface-container-high via-surface-container-high/20 to-transparent" />
              </div>
              
              <div className="absolute bottom-0 left-0 p-10 w-full">
                <div className="flex items-center gap-2 mb-4">
                  <div className={cn(
                    "inline-block px-4 py-1 rounded-full text-xs font-bold tracking-widest uppercase border",
                    path.color === 'primary' ? "bg-primary/20 text-primary border-primary/20" : "bg-secondary/20 text-secondary border-secondary/20"
                  )}>
                    {path.dimension}
                  </div>
                  {path.recommended && (
                    <span className="px-3 py-1 rounded-full bg-tertiary/20 text-tertiary text-[10px] font-bold border border-tertiary/20">RECOMMENDED</span>
                  )}
                  {path.isNew && (
                    <span className="px-3 py-1 rounded-full bg-secondary/30 text-secondary text-[10px] font-bold border border-secondary/30">NEW</span>
                  )}
                </div>
                <h2 className="text-4xl md:text-5xl font-serif font-bold mb-2 text-glow">{path.title}</h2>
                <p className="text-on-surface-variant mb-4 line-clamp-2">{path.desc}</p>
                <div className="flex items-center gap-4 mb-6 text-sm text-on-surface-variant/80">
                  <span>{path.duration} Course</span>
                  <span className={cn(
                    "px-2 py-0.5 rounded bg-surface-bright/30",
                    path.color === 'primary' ? "text-primary" : "text-secondary"
                  )}>Level {path.level}</span>
                </div>
                <Button 
                  onClick={() => navigate('/dashboard')}
                  className="w-full py-5 text-lg"
                >
                  开始旅程
                </Button>
              </div>
            </motion.div>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <GlassCard className="inner-glow flex items-center justify-between">
            <div>
              <p className="text-xs uppercase tracking-widest text-on-surface-variant/60 mb-2">当前进度</p>
              <h3 className="text-2xl font-bold text-secondary">64% 升华完成</h3>
            </div>
            <div className="w-12 h-12 rounded-full border-4 border-secondary/20 border-t-secondary relative flex items-center justify-center">
              <span className="text-[10px] text-secondary font-bold">LV.4</span>
            </div>
          </GlassCard>

          <GlassCard className="flex items-center justify-between">
            <div>
              <p className="text-xs uppercase tracking-widest text-on-surface-variant/60 mb-2">持续召唤</p>
              <h3 className="text-2xl font-bold">14 天</h3>
            </div>
            <Flame className="text-tertiary" size={32} />
          </GlassCard>

          <GlassCard className="flex items-center justify-between border-2 border-primary/20">
            <div>
              <p className="text-xs uppercase tracking-widest text-on-surface-variant/60 mb-2">待办密令</p>
              <h3 className="text-2xl font-bold text-primary">8 个咒语</h3>
            </div>
            <Wand2 className="text-primary" size={32} />
          </GlassCard>
        </div>
      </section>
    </div>
  );
}
