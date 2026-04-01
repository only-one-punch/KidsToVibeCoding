import { motion } from 'motion/react';
import { ArrowRight, Sparkles } from 'lucide-react';
import { Button } from '@/src/components/UI';
import { useNavigate } from 'react-router-dom';

export function LandingView() {
  const navigate = useNavigate();

  return (
    <div className="relative min-h-screen flex flex-col items-center justify-center px-8 text-center overflow-hidden pt-20">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="relative z-10"
      >
        <h1 className="font-serif text-6xl md:text-8xl leading-tight mb-8 italic">
          在 <span className="text-primary text-glow">少年心中</span> <br />
          编写 <span className="text-secondary text-glow">AI 的未来</span>
        </h1>
        
        <p className="max-w-2xl mx-auto text-xl text-on-surface-variant font-light leading-relaxed mb-12">
          不仅是代码编写，更是一场跨越维度的数字召唤。<br />
          CodeBuddyAI 让每一行逻辑都闪耀着创意的光芒。
        </p>

        <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
          <Button 
            onClick={() => navigate('/onboarding')}
            className="flex items-center gap-3 text-lg py-5 px-12"
          >
            开启旅程 <Sparkles size={20} />
          </Button>
          <Button 
            variant="ghost"
            className="text-lg py-5 px-12 bg-surface-container-high/40 backdrop-blur-md"
          >
            了解更多
          </Button>
        </div>
      </motion.div>

      {/* Decorative Elements */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-primary/5 blur-[120px] rounded-full -z-10" />
      
      <div className="mt-32 grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-7xl">
        <motion.div 
          whileHover={{ scale: 1.02 }}
          className="group relative rounded-lg overflow-hidden h-[400px] bg-surface-container-low inner-glow cursor-pointer"
        >
          <img 
            src="https://picsum.photos/seed/nebula/800/600" 
            alt="Workspace" 
            className="absolute inset-0 w-full h-full object-cover mix-blend-overlay opacity-60 transition-transform duration-700 group-hover:scale-110"
            referrerPolicy="no-referrer"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-surface to-transparent" />
          <div className="absolute bottom-8 left-8 text-left">
            <h3 className="font-serif text-4xl text-on-surface mb-2">星空工作区</h3>
            <p className="text-on-surface-variant max-w-xs">沉浸式 3D 编码环境，让算法如星辰般流转。</p>
          </div>
        </motion.div>

        <motion.div 
          whileHover={{ scale: 1.02 }}
          className="group relative rounded-lg overflow-hidden h-[400px] bg-surface-container-low inner-glow cursor-pointer"
        >
          <div className="absolute inset-0 flex items-center justify-center">
            <Sparkles size={80} className="text-secondary/40 group-hover:text-secondary transition-all duration-500" />
          </div>
          <div className="absolute inset-0 bg-gradient-to-t from-surface to-transparent" />
          <div className="absolute bottom-8 left-8 text-left">
            <h3 className="font-serif text-4xl text-on-surface mb-2">咒语召唤</h3>
            <p className="text-on-surface-variant max-w-xs">通过自然语言吟唱，瞬间生成复杂微服务架构。</p>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
