import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Send, Mic, Sparkles } from 'lucide-react';
import { GoogleGenAI } from "@google/genai";
import { cn } from '@/src/lib/utils';
import { GlassCard } from '@/src/components/UI';

export function SummonView() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<{ role: 'user' | 'ai', text: string }[]>([
    { role: 'ai', text: '小明，按住 [Shift] 键可以锁定比例。' }
  ]);
  const [isTyping, setIsTyping] = useState(false);
  
  const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

  const handleSend = async () => {
    if (!input.trim()) return;
    
    const userMsg = input;
    setInput('');
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setIsTyping(true);

    try {
      const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: userMsg,
        config: {
          systemInstruction: "You are Oracle Buddy, a helpful AI coding mentor for teenagers. Your tone is encouraging, slightly magical, and very practical. Keep responses concise and helpful for a young learner."
        }
      });
      
      setMessages(prev => [...prev, { role: 'ai', text: response.text || '魔法似乎失效了，请再试一次。' }]);
    } catch (error) {
      console.error(error);
      setMessages(prev => [...prev, { role: 'ai', text: '连接星界失败，请检查你的网络。' }]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <main className="pt-20 h-screen flex flex-col relative nebula-bg overflow-hidden">
      <div className="flex-1 flex flex-col items-center justify-center p-8 relative">
        <div className="relative group mb-12">
          <div className="absolute inset-0 bg-primary/20 blur-[100px] rounded-full group-hover:bg-secondary/20 transition-colors duration-1000" />
          <div className="relative w-48 h-48 flex items-center justify-center">
            <motion.div 
              animate={{ 
                rotate: 45,
                scale: [1, 1.05, 1],
              }}
              transition={{ 
                duration: 4,
                repeat: Infinity,
                ease: "easeInOut"
              }}
              className="w-32 h-32 bg-gradient-to-br from-primary via-surface-container-high to-secondary rounded-[2.5rem] flex items-center justify-center shadow-[0_0_60px_20px_rgba(229,180,255,0.3),inset_0_0_40px_rgba(0,245,255,0.5)]"
            >
              <div className="w-full h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-30 rounded-[2.5rem]" />
            </motion.div>
            <div className="absolute inset-0 border-2 border-primary/20 rounded-full animate-[spin_10s_linear_infinite]" />
            <div className="absolute -inset-4 border border-secondary/10 rounded-full animate-[spin_15s_linear_infinite_reverse]" />
          </div>
        </div>

        <div className="text-center max-w-2xl w-full">
          <h2 className="font-serif text-4xl text-on-surface mb-4 italic text-glow">Oracle Buddy</h2>
          <div className="glass-card px-10 py-8 rounded-[40px] shadow-2xl min-h-[120px] flex items-center justify-center">
            <AnimatePresence mode="wait">
              <motion.p 
                key={messages[messages.length - 1].text}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="text-2xl leading-[2] text-primary font-medium tracking-wide"
              >
                {isTyping ? '正在吟唱咒语...' : messages[messages.length - 1].text}
              </motion.p>
            </AnimatePresence>
          </div>
        </div>
      </div>

      <div className="absolute right-8 top-28 w-72 hidden xl:block space-y-6">
        <GlassCard className="p-6 border-l-4 border-secondary/30">
          <p className="text-xs text-secondary mb-2 uppercase tracking-widest font-bold">最新指令</p>
          <p className="text-sm text-on-surface-variant leading-relaxed">优化 React 组件的重绘逻辑，建议使用 useMemo 包装计算密集型函数。</p>
        </GlassCard>
        <GlassCard className="p-6 opacity-60">
          <p className="text-xs text-on-surface-variant/60 mb-2 uppercase tracking-widest">魔法历史</p>
          <p className="text-sm text-on-surface-variant/40 italic">"如何构建一个无边界的 UI 框架？"</p>
        </GlassCard>
      </div>

      <div className="w-full max-w-4xl mx-auto px-8 pb-12">
        <div className="relative group">
          <div className="absolute -inset-1 bg-gradient-to-r from-primary/30 to-secondary/30 blur-xl opacity-0 group-focus-within:opacity-100 transition-opacity duration-500" />
          <div className="relative glass-card rounded-[40px] flex items-center p-2 border border-white/10 shadow-2xl">
            <button className="w-12 h-12 flex items-center justify-center text-on-surface-variant hover:text-secondary transition-colors">
              <Mic size={20} />
            </button>
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSend()}
              className="flex-1 bg-transparent border-none focus:ring-0 text-on-surface placeholder:text-on-surface-variant/40 py-4 px-4 text-lg" 
              placeholder="与 Buddy 交流..." 
            />
            <button 
              onClick={handleSend}
              className="p-3 bg-gradient-to-tr from-primary to-primary-container text-surface rounded-full shadow-lg hover:scale-110 transition-transform flex items-center justify-center"
            >
              <Send size={20} />
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
