import { motion } from 'motion/react';
import { GlassCard } from '@/src/components/UI';

export function GalleryView() {
  const projects = [
    { title: '神经流光 (Neural Flow)', author: '苏林 (Su Lin)', tag: 'AI GEN', img: 'https://picsum.photos/seed/art1/800/800' },
    { title: '量子结晶 (Quantum Crystal)', author: '王志 (Wang Zhi)', tag: 'ENGINEERING', img: 'https://picsum.photos/seed/art2/800/800' },
    { title: '星尘协议 (Stardust Protocol)', author: '陈美 (Chen Mei)', tag: 'SECURITY', img: 'https://picsum.photos/seed/art3/800/800' },
    { title: '梦境重构 (Dream Refactor)', author: '李佳 (Li Jia)', tag: 'DATA ART', img: 'https://picsum.photos/seed/art4/800/800' },
    { title: '以太网关 (Ether Gateway)', author: '赵雷 (Zhao Lei)', tag: 'NETWORKING', img: 'https://picsum.photos/seed/art5/800/800' },
    { title: '莫比乌斯 (Mobius Pulse)', author: '韩雪 (Han Xue)', tag: 'UX DESIGN', img: 'https://picsum.photos/seed/art6/800/800' },
  ];

  return (
    <main className="pt-32 pb-24 px-6 md:px-12 lg:px-24 max-w-7xl mx-auto">
      <section className="mb-20 text-center">
        <h1 className="font-serif text-6xl md:text-8xl italic font-light text-primary text-glow leading-tight">学生杰作</h1>
        <p className="mt-6 text-on-surface-variant text-lg md:text-xl font-light max-w-2xl mx-auto tracking-wide">
          在以太实验室诞生的突破性项目合集。从神经艺术到量子脚本。
        </p>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
        {projects.map((project) => (
          <motion.div 
            key={project.title}
            whileHover={{ y: -8 }}
            className="glass-card rounded-lg group overflow-hidden relative p-0"
          >
            <div className="h-80 w-full overflow-hidden relative">
              <img 
                src={project.img} 
                alt={project.title} 
                className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                referrerPolicy="no-referrer"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-surface-container-low to-transparent opacity-60" />
            </div>
            <div className="p-8">
              <h3 className="font-serif text-3xl italic text-on-surface group-hover:text-primary transition-colors">{project.title}</h3>
              <div className="flex items-center justify-between mt-4">
                <span className="text-sm text-on-surface-variant font-light tracking-widest">{project.author}</span>
                <span className="px-3 py-1 bg-surface-bright/20 rounded-full text-[10px] text-secondary border border-secondary/20">{project.tag}</span>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      <div className="mt-20 flex justify-center">
        <button className="relative group px-12 py-5 rounded-full overflow-hidden transition-all active:scale-95">
          <div className="absolute inset-0 bg-gradient-to-r from-primary to-secondary opacity-80 group-hover:opacity-100 transition-opacity" />
          <div className="absolute inset-[1.4px] bg-surface-container rounded-full backdrop-blur-xl transition-colors group-hover:bg-transparent" />
          <span className="relative font-bold text-on-surface group-hover:text-surface transition-colors">加载更多 (Load More)</span>
        </button>
      </div>
    </main>
  );
}
