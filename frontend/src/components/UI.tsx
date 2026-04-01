import { ReactNode } from 'react';
import { cn } from '@/src/lib/utils';

interface GlassCardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
}

export function GlassCard({ children, className, hover = false }: GlassCardProps) {
  return (
    <div className={cn(
      "glass-card rounded-lg p-6 transition-all duration-500",
      hover && "hover:translate-y-[-4px] hover:bg-surface-container-high/60",
      className
    )}>
      {children}
    </div>
  );
}

interface ButtonProps {
  children: ReactNode;
  variant?: 'primary' | 'secondary' | 'ghost';
  className?: string;
  onClick?: () => void;
  type?: 'button' | 'submit';
}

export function Button({ children, variant = 'primary', className, onClick, type = 'button' }: ButtonProps) {
  const variants = {
    primary: "bg-gradient-to-br from-primary to-primary-container text-surface shadow-[0_0_20px_rgba(229,180,255,0.3)] hover:shadow-[0_0_30px_rgba(229,180,255,0.5)]",
    secondary: "border border-secondary/20 text-secondary hover:bg-secondary/10",
    ghost: "text-on-surface-variant hover:text-primary"
  };

  return (
    <button
      type={type}
      onClick={onClick}
      className={cn(
        "px-8 py-3 rounded-full font-bold transition-all duration-300 active:scale-95",
        variants[variant],
        className
      )}
    >
      {children}
    </button>
  );
}
