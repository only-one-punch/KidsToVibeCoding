# CodeBuddyAI UI 设计指南

**版本**: v1.0
**创建日期**: 2026-03-27
**灵感来源**: Google Stitch (https://stitch.withgoogle.com/)

---

## 设计理念

### 核心原则

**「AI 工具版多邻国」** — 让学习 AI 工具像玩游戏一样有趣，像搭积木一样简单。

| 原则 | 说明 |
|------|------|
| 🎯 **清晰易懂** | 6-14 岁孩子能独立理解，无需家长协助 |
| 🚀 **即时反馈** | 每个操作都有响应，保持学习动力 |
| 🎮 **游戏化** | 积分、徽章、进度条，让学习像闯关 |
| 🌈 **愉悦感** | 色彩丰富但不杂乱，动画流畅但不干扰 |

---

## 视觉风格

### 整体美学

**现代 × 友好 × 专业**

参考 Google Stitch 的设计语言：
- 大面积留白，让内容呼吸
- 圆角卡片，柔和亲切
- 渐变色彩，充满活力
- 微动画，增添趣味

---

## 色彩系统

### 主色调

```
品牌蓝 (Primary Blue)
─────────────────────────
#4F46E5 → #6366F1 → #818CF8

活力渐变：从深蓝到紫蓝
用于：主按钮、重要元素、品牌标识
```

```
活力橙 (Accent Orange)
─────────────────────────
#F97316 → #FB923C

用于：强调、奖励、成就提示
```

```
成功绿 (Success Green)
─────────────────────────
#10B981 → #34D399

用于：完成状态、正确反馈、进度完成
```

### 中性色

```
深色文字
─────────────────────────
#111827 (主标题)
#374151 (正文)
#6B7280 (次要文字)
#9CA3AF (占位符)
```

```
背景色
─────────────────────────
#FFFFFF (主背景)
#F9FAFB (次背景/卡片背景)
#F3F4F6 (分割线/边框)
#E5E7EB (禁用状态)
```

### 语义色

```
错误红: #EF4444
警告黄: #F59E0B
信息蓝: #3B82F6
```

### 色彩应用示例

```html
<!-- 主按钮 -->
<button class="btn-primary">开始学习</button>
<style>
.btn-primary {
  background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%);
  color: white;
  border-radius: 12px;
  padding: 12px 24px;
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
}
</style>
```

---

## 字体系统

### 主字体

**中文**: 系统默认 (PingFang SC / 思源黑体)
**英文/数字**: Inter

```css
:root {
  --font-sans: "Inter", "PingFang SC", "Hiragino Sans GB", sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
}
```

### 字体层级

| 用途 | 大小 | 字重 | 行高 | 示例 |
|------|------|------|------|------|
| 大标题 | 32px | 700 | 1.2 | 欢迎来到 CodeBuddyAI |
| 页面标题 | 24px | 600 | 1.3 | 开始你的第一个项目 |
| 卡片标题 | 18px | 600 | 1.4 | 学习 Figma |
| 正文 | 16px | 400 | 1.6 | 今天我们来学习如何... |
| 小字 | 14px | 400 | 1.5 | 辅助说明文字 |
| 微型 | 12px | 400 | 1.4 | 标签、时间戳 |

### 字体加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

---

## 间距系统

### 基础单位

**基础单位**: 4px

```
--space-1:  4px   (紧凑)
--space-2:  8px   (小)
--space-3:  12px  (默认)
--space-4:  16px  (中等)
--space-6:  24px  (大)
--space-8:  32px  (超大)
--space-12: 48px  (区块间距)
--space-16: 64px  (页面边距)
```

### 组件内间距

```css
/* 卡片 */
.card { padding: var(--space-6); }

/* 按钮 */
.btn { padding: var(--space-3) var(--space-6); }

/* 输入框 */
.input { padding: var(--space-3) var(--space-4); }
```

---

## 圆角系统

```
--radius-sm:   6px   (小按钮、标签)
--radius-md:   12px  (按钮、输入框、卡片)
--radius-lg:   16px  (大卡片、模态框)
--radius-xl:   24px  (特殊容器)
--radius-full: 9999px (圆形头像、徽章)
```

---

## 阴影系统

```css
/* 卡片阴影 */
.shadow-sm {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.shadow-md {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.shadow-lg {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.shadow-xl {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

/* 品牌色阴影 (用于主按钮) */
.shadow-primary {
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
}
```

---

## 组件规范

### 按钮

#### 主按钮 (Primary)

```css
.btn-primary {
  background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%);
  color: white;
  border: none;
  border-radius: 12px;
  padding: 12px 24px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}
```

#### 次按钮 (Secondary)

```css
.btn-secondary {
  background: #F9FAFB;
  color: #374151;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 12px 24px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: #F3F4F6;
  border-color: #D1D5DB;
}
```

#### 图标按钮

```css
.btn-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #F9FAFB;
  border: 1px solid #E5E7EB;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-icon:hover {
  background: #F3F4F6;
}
```

### 卡片

```css
.card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  border: 1px solid #F3F4F6;
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
}

.card-clickable {
  cursor: pointer;
}

/* 学习路径卡片 */
.path-card {
  display: flex;
  align-items: center;
  gap: 16px;
}

.path-card .icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}
```

### 输入框

```css
.input {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #E5E7EB;
  border-radius: 12px;
  font-size: 16px;
  transition: all 0.2s ease;
  background: white;
}

.input:focus {
  outline: none;
  border-color: #4F46E5;
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1);
}

.input::placeholder {
  color: #9CA3AF;
}
```

### 进度条

```css
.progress-bar {
  height: 8px;
  background: #E5E7EB;
  border-radius: 9999px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4F46E5, #6366F1);
  border-radius: 9999px;
  transition: width 0.5s ease;
}

/* 圆形进度 */
.progress-circle {
  width: 60px;
  height: 60px;
  position: relative;
}

.progress-circle svg {
  transform: rotate(-90deg);
}

.progress-circle .progress-ring {
  stroke: #4F46E5;
  stroke-linecap: round;
  transition: stroke-dashoffset 0.5s ease;
}
```

### 徽章

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
}

.badge-primary {
  background: rgba(79, 70, 229, 0.1);
  color: #4F46E5;
}

.badge-success {
  background: rgba(16, 185, 129, 0.1);
  color: #10B981;
}

.badge-warning {
  background: rgba(249, 115, 22, 0.1);
  color: #F97316;
}
```

---

## 动画规范

### 原则

1. **快速响应**: 交互反馈 < 100ms
2. **流畅过渡**: 状态变化 200-300ms
3. **自然缓动**: 使用 ease-out 或 cubic-bezier

### 缓动函数

```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
```

### 常用动画

```css
/* 淡入 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* 上移淡入 */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 缩放 */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* 弹跳 */
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* 脉冲 (用于徽章获取) */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}
```

### 交互动画

```css
/* 按钮点击 */
.btn:active {
  transform: scale(0.97);
}

/* 卡片悬停 */
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
}

/* 链接悬停 */
.link:hover {
  color: #4F46E5;
}

/* 加载旋转 */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

---

## 图标系统

### 图标风格

- 风格: 线性图标 (Lucide / Heroicons)
- 粗细: 1.5px - 2px
- 大小: 16px / 20px / 24px

### 常用图标

```
学习相关:
- book-open (课程)
- play (开始)
- check-circle (完成)
- trophy (成就)
- star (收藏/星级)

工具相关:
- code (代码)
- paintbrush (设计)
- globe (部署)
- rocket (发布)

交互相关:
- send (发送)
- microphone (语音)
- message-circle (对话)
- heart (喜欢)

状态相关:
- loader (加载中)
- alert-circle (错误)
- info (提示)
- check (成功)
```

---

## 布局规范

### 页面宽度

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* 窄内容区 */
.container-sm {
  max-width: 640px;
}

/* 中等内容区 */
.container-md {
  max-width: 768px;
}
```

### 网格系统

```css
.grid {
  display: grid;
  gap: 24px;
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

/* 响应式 */
@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 {
    grid-template-columns: 1fr;
  }
}
```

---

## 响应式设计

### 断点

```css
/* 移动端 */
@media (max-width: 640px) { ... }

/* 平板 */
@media (min-width: 641px) and (max-width: 1024px) { ... }

/* 桌面 */
@media (min-width: 1025px) { ... }
```

### 移动端适配

- 最小可点击区域: 44px × 44px
- 底部导航栏高度: 64px
- 表单元素高度: 48px
- 字体最小: 14px

---

## 页面模板

### 首页

```
┌─────────────────────────────────────┐
│  Logo              登录 | 注册      │
├─────────────────────────────────────┤
│                                     │
│      让孩子学会用 AI 创造           │
│      CodeBuddyAI                    │
│                                     │
│      [ 开始学习 ]  [ 了解更多 ]     │
│                                     │
│  ┌─────────┐  ┌─────────┐          │
│  │ 🎨 Figma │  │ 🤖 AI   │          │
│  │ 设计入门 │  │ 助手使用 │          │
│  └─────────┘  └─────────┘          │
│                                     │
└─────────────────────────────────────┘
```

### 学习页面

```
┌─────────────────────────────────────┐
│  ← 返回           学习 Figma        │
├─────────────────────────────────────┤
│  进度: ████░░░░░░ 40%               │
├─────────────────────────────────────┤
│                                     │
│  第 3 课: 创建你的第一个设计        │
│                                     │
│  [ 视频教程区域 ]                   │
│                                     │
│  步骤说明...                        │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ 💡 提示: 点击这里可以...     │   │
│  └─────────────────────────────┘   │
│                                     │
│  [ 上一课 ]          [ 下一课 ]    │
│                                     │
└─────────────────────────────────────┘
```

### AI 对话

```
┌─────────────────────────────────────┐
│  AI 老师                    ✕      │
├─────────────────────────────────────┤
│                                     │
│  🤖 你好！我是你的 AI 老师，        │
│     有什么问题可以问我哦~           │
│                                     │
│  👤 这个工具怎么用？                │
│                                     │
│  🤖 好问题！让我来告诉你...         │
│     [ 详细解答 ]                    │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ 输入你的问题...        🎤  │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## 深色模式 (可选)

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #0F172A;
    --bg-secondary: #1E293B;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --border: #334155;
  }
}
```

---

## 无障碍设计

### 对比度

- 正文文字: 至少 4.5:1
- 大标题: 至少 3:1
- 交互元素: 清晰可辨

### 焦点状态

```css
:focus-visible {
  outline: 2px solid #4F46E5;
  outline-offset: 2px;
}
```

### 动画偏好

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 设计资源

### Figma 设计系统

- 组件库: 待创建
- 设计 Token: 待定义

### 图标库

- Lucide Icons: https://lucide.dev/
- Heroicons: https://heroicons.com/

### 配色工具

- Coolors: https://coolors.co/
- Realtime Colors: https://realtimecolors.com/

---

## 下一步

1. 创建 Figma 设计系统文件
2. 开发 React 组件库
3. 设计关键页面原型
4. 用户测试与迭代

---

**版本历史**

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-03-27 | 初始版本 |