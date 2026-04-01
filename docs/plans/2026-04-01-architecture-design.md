# CodeBuddyAI 系统架构设计文档

**版本**: v1.0
**创建日期**: 2026-04-01
**状态**: 待实施

---

## 1. 概述

### 1.1 产品定位

CodeBuddyAI 是一个面向 12-14 岁青少年的 AI 工具学习平台，让孩子通过游戏化方式学习 AI 工具（Figma、Claude Code、Cloudflare 等），最终能独立创作作品并分享。

### 1.2 目标用户

- **主要用户**: 12-14 岁青少年，能熟练打字，有一定理解能力
- **次要用户**: 家长（可选的学习报告接收者）

### 1.3 核心功能

- 课程学习（网站开发、游戏开发、视频创作等路径）
- AI 老师实时对话（解答问题、引导学习）
- 语音交互（语音识别、语音合成）
- 数字人老师（虚拟形象、表情驱动）
- 代码执行与可视化（沙箱环境、算法可视化）
- 学习进度追踪与成就系统

---

## 2. 架构设计原则

### 2.1 为什么选择微服务架构

**工作负载特性差异大，不适合单体架构**：

| 服务 | 工作负载特性 | 资源需求 |
|------|-------------|----------|
| AI 对话 | IO 密集 + 计算密集，需要流式输出 | CPU + 大内存 |
| 语音识别/合成 | 计算密集 | GPU（可选） |
| 代码执行 | 需要沙箱隔离，不可信代码 | 独立容器，资源限制 |
| 数字人渲染 | 实时渲染，计算密集 | GPU / 专用渲染 |
| 业务 API | 普通 CRUD，响应快 | 低配 CPU |

**微服务架构优势**：
1. 每个服务独立扩展
2. 故障隔离
3. 资源最优配置
4. 技术栈灵活
5. 团队并行开发效率高

---

## 3. 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户层                                    │
│   Web App (React)    │    Mobile App (未来)    │    家长端       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Gateway Service                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ 路由        │  │ 认证        │  │ 限流        │              │
│  │ /api/*      │  │ JWT验证     │  │ 用户级限流  │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ User Service  │    │Learning Service│    │AI Assistant   │
│               │    │               │    │   Service     │
│ • 用户认证    │    │ • 课程管理    │    │ • LLM对话     │
│ • 用户档案    │    │ • 学习路径    │◄──►│ • RAG检索     │
│ • 家长关联    │    │ • 进度追踪    │    │ • 记忆系统    │
│               │    │ • 成就系统    │    │ • Skills编排  │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ PostgreSQL    │    │ PostgreSQL    │    │ Redis         │
│ (用户数据)    │    │ (学习数据)    │    │ (会话记忆)    │
└───────────────┘    └───────────────┘    │ Pinecone      │
                                          │ (向量检索)    │
                                          └───────────────┘

        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│AI Multimodal  │    │ Sandbox       │    │ Message Queue │
│   Service     │    │   Service     │    │   (Celery)    │
│               │    │               │    │               │
│ • 语音识别    │    │ • 代码执行    │    │ • 异步任务    │
│ • 语音合成    │    │ • 可视化渲染  │    │ • 任务调度    │
│ • 数字人驱动  │    │ • 安全隔离    │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
        │                    │
        ▼                    ▼
┌───────────────┐    ┌───────────────┐
│ 讯飞API       │    │ Docker/Fire   │
│ (语音/数字人) │    │ cracker沙箱   │
└───────────────┘    └───────────────┘
```

---

## 4. 服务拆分

采用 **领域 + 特殊工作负载** 的拆分策略：

```
├── gateway-service          # API 网关（路由/限流/认证）
│
├── user-service             # 用户管理
│   ├── 认证授权
│   ├── 用户档案
│   └── 家长关联（可选报告推送）
│
├── learning-service         # 学习领域
│   ├── 课程体系
│   ├── 学习路径
│   ├── 进度追踪
│   └── 成就系统
│
├── ai-assistant-service     # AI 助手（核心）
│   ├── LLM 对话（流式）
│   ├── RAG 知识检索
│   ├── 记忆系统（短期/长期）
│   ├── Skills 编排
│   └── 画板理解
│
├── ai-multimodal-service    # 多模态服务
│   ├── 语音识别（讯飞）
│   ├── 语音合成（讯飞）
│   └── 数字人驱动（讯飞）
│
└── sandbox-service          # 代码沙箱
    ├── 代码执行
    ├── 可视化渲染
    └── 安全隔离（Docker/gVisor）
```

**服务清单**：

```
服务名称                端口      数据库              依赖
─────────────────────────────────────────────────────────────
gateway-service        8000      -                   所有服务
user-service           8001      PostgreSQL         -
learning-service       8002      PostgreSQL         -
ai-assistant-service   8003      Redis + Pinecone   user, learning
ai-multimodal-service  8004      -                  讯飞API
sandbox-service        8005      -                  Docker
```

---

## 5. Gateway Service

**职责**：系统的唯一入口，负责路由、认证、限流、协议转换

```
Gateway Service
├── 路由层
│   ├── /api/user/*      → user-service
│   ├── /api/learning/*  → learning-service
│   ├── /api/chat/*      → ai-assistant-service (WebSocket)
│   ├── /api/voice/*     → ai-multimodal-service
│   └── /api/code/*      → sandbox-service
│
├── 认证层
│   ├── JWT 验证（用户请求）
│   ├── API Key 验证（服务间调用）
│   └── 家长权限检查（家长控制相关接口）
│
├── 限流层
│   ├── 用户级限流（防止滥用）
│   ├── IP级限流（防止攻击）
│   └── AI接口特殊限流（LLM成本控制）
│
└── 协议转换
    ├── HTTP → HTTP（普通API）
    ├── HTTP → WebSocket（AI对话流式输出）
    └── WebSocket → HTTP（语音流上传）
```

**技术选型**：FastAPI 自建 Gateway

**关键接口**：

```
POST   /api/user/auth/login          # 登录
POST   /api/user/auth/register       # 注册
GET    /api/learning/courses         # 获取课程列表
POST   /api/learning/progress        # 更新学习进度
WS     /api/chat/stream              # AI对话（WebSocket流式）
POST   /api/voice/recognize          # 语音识别
POST   /api/code/execute             # 代码执行
```

---

## 6. User Service

**职责**：用户管理、认证授权、家长关联

### 6.1 功能模块

```
User Service
├── 认证模块
│   ├── 注册（邮箱/手机号 + 密码）
│   ├── 登录（JWT Token）
│   ├── Token刷新
│   └── 第三方登录（可选：微信/QQ）
│
├── 用户档案模块
│   ├── 基本信息（昵称、头像、年龄）
│   ├── 学习偏好（兴趣方向：网站/游戏/视频）
│   ├── 数字人形象选择
│   └── 学习统计数据（积分、徽章、连续打卡）
│
├── 家长关联模块（可选）
│   ├── 家长账号绑定（用于查看学习报告）
│   ├── 学习报告推送（每周/每月）
│   └── 无强制控制功能
│
└── 权限模块
    ├── 普通用户
    └── 管理员（后台运营）
```

### 6.2 数据库设计

```sql
-- 用户表
CREATE TABLE users (
    id UUID PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    avatar_url VARCHAR(255),
    age INT,                       -- 12-14
    interest_direction ENUM('web', 'game', 'video', 'other'),
    digital_human_id VARCHAR(50),  -- 选择的数字人形象
    points INT DEFAULT 0,          -- 积分
    streak_days INT DEFAULT 0,     -- 连续打卡天数
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- 认证凭证表
CREATE TABLE auth_credentials (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    last_login TIMESTAMP,
    created_at TIMESTAMP
);

-- 家长关联表（可选）
CREATE TABLE parent_links (
    id UUID PRIMARY KEY,
    child_id UUID REFERENCES users(id),
    parent_email VARCHAR(255),
    report_frequency ENUM('weekly', 'monthly', 'none') DEFAULT 'none',
    created_at TIMESTAMP
);
```

---

## 7. Learning Service

**职责**：课程管理、学习路径、进度追踪、成就系统

### 7.1 功能模块

```
Learning Service
├── 课程模块
│   ├── 课程库管理
│   ├── 课程版本控制（工具更新时课程同步更新）
│   ├── 课程难度分级
│   └── 课程内容存储（Markdown/富文本）
│
├── 学习路径模块
│   ├── 路径定义（网站开发路径 = Figma → Claude Code → Cloudflare）
│   ├── 路径推荐（根据用户兴趣选择）
│   ├── 路径解锁逻辑（完成前置才能解锁后续）
│   └── 路径进度计算
│
├── 进度追踪模块
│   ├── 课程完成状态
│   ├── 学习时长记录
│   ├── 知识点掌握评估
│   └── 学习轨迹分析
│
└── 成就系统模块
│   ├── 徽章定义（网站大师、游戏开发者等）
│   ├── 积分规则（完成任务 +10，连续打卡 +20）
│   ├── 成就解锁触发
│   └── 排行榜（社区互动）
```

### 7.2 数据库设计

```sql
-- 课程表
CREATE TABLE courses (
    id UUID PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    tool VARCHAR(50),              -- Figma / Claude Code / Cloudflare
    difficulty ENUM('beginner', 'intermediate', 'advanced'),
    estimated_minutes INT,
    content_url VARCHAR(255),
    version VARCHAR(20),
    order_in_path INT,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- 学习路径表
CREATE TABLE learning_paths (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    courses_order JSONB,
    total_courses INT,
    estimated_hours INT,
    badge_id UUID,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP
);

-- 用户学习进度表
CREATE TABLE user_progress (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    path_id UUID REFERENCES learning_paths(id),
    current_course_id UUID REFERENCES courses(id),
    completed_courses JSONB,
    progress_percentage INT DEFAULT 0,
    started_at TIMESTAMP,
    last_activity_at TIMESTAMP,
    completed_at TIMESTAMP
);

-- 课程学习记录表
CREATE TABLE course_sessions (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    course_id UUID REFERENCES courses(id),
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    duration_seconds INT,
    completed BOOLEAN DEFAULT false,
    quiz_score INT,
    notes TEXT
);

-- 徽章表
CREATE TABLE badges (
    id UUID PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    icon_url VARCHAR(255),
    requirement JSONB,
    created_at TIMESTAMP
);

-- 用户徽章表
CREATE TABLE user_badges (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    badge_id UUID REFERENCES badges(id),
    unlocked_at TIMESTAMP
);

-- 积分记录表
CREATE TABLE points_log (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    points INT,
    reason VARCHAR(100),
    created_at TIMESTAMP
);
```

---

## 8. AI Assistant Service

**职责**：AI 对话核心，协调 RAG、记忆系统、Skills 编排

### 8.1 功能模块

```
AI Assistant Service
├── 对话引擎
│   ├── LLM 调用（Claude Opus 4.6）
│   ├── 流式输出（WebSocket）
│   ├── 多轮对话管理
│   └── 对话历史存储
│
├── RAG 知识检索
│   ├── 知识库管理（编程知识、工具使用、常见问题）
│   ├── 向量检索（Pinecone）
│   ├── 检索结果排序
│   └── 知识更新机制
│
├── 记忆系统
│   ├── 短期记忆（当前会话，Redis）
│   ├── 长期记忆（学习历史，PostgreSQL + 向量索引）
│   ├── 语义记忆检索
│   └── 记忆压缩
│
├── Skills 编排
│   ├── 教学类 Skill（友好解释、分步引导、可视化调试）
│   ├── 创作类 Skill（模板生成、智能提示、创意激发）
│   ├── 学习管理 Skill（难度自适应、路径推荐）
│   └── Skill 调度引擎（LangGraph）
│
└── 多模态接口
    ├── 画板理解（Vision 模型解析图片）
    ├── 语音请求转发（调用 ai-multimodal-service）
    └── 数字人驱动请求转发
```

### 8.2 数据存储架构

```
┌──────────────┐    ┌──────────────┐
│ Redis        │    │ PostgreSQL   │
│ (短期记忆)   │    │ (对话历史)   │
│              │    │              │
│ • Session    │    │ • Messages   │
│ • Context    │    │ • Summaries  │
│ • Temp Data  │    │              │
└──────────────┘    └──────────────┘

┌──────────────┐    ┌──────────────┐
│ Pinecone     │    │ 本地缓存     │
│ (向量检索)   │    │              │
│              │    │ • 常见问题   │
│ • 知识库     │    │ • 模板回复   │
│ • 记忆向量   │    │              │
└──────────────┘    └──────────────┘
```

### 8.3 数据库设计

```sql
-- 对话会话表
CREATE TABLE chat_sessions (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    context JSONB,
    summary TEXT,
    message_count INT DEFAULT 0
);

-- 对话消息表
CREATE TABLE chat_messages (
    id UUID PRIMARY KEY,
    session_id UUID REFERENCES chat_sessions(id),
    role ENUM('user', 'assistant'),
    content TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP
);

-- 记忆摘要表
CREATE TABLE memory_summaries (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    session_id UUID REFERENCES chat_sessions(id),
    summary_text TEXT NOT NULL,
    key_topics JSONB,
    embedding_id VARCHAR(255),
    created_at TIMESTAMP
);

-- 知识库表
CREATE TABLE knowledge_base (
    id UUID PRIMARY KEY,
    category VARCHAR(50),
    title VARCHAR(100),
    content TEXT NOT NULL,
    tool VARCHAR(50),
    difficulty ENUM('beginner', 'intermediate', 'advanced'),
    embedding_id VARCHAR(255),
    version VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

### 8.4 核心流程

```
用户提问 ─────────────────────────────────────────────────────►
                                                                │
    ┌─────────────────────────────────────────────────────────┤
    │                                                          │
    │  1. 加载上下文                                           │
    │     ├── Redis 获取当前会话短期记忆                        │
    │     ├── 获取用户当前学习进度                              │
    │     └── 获取用户画像（年龄、兴趣、学习风格）               │
    │                                                          │
    │  2. RAG 检索                                             │
    │     ├── Pinecone 检索相关知识点                          │
    │     ├── 检索历史对话记忆（语义相似）                      │
    │     └── 结果排序，取 Top 3                                │
    │                                                          │
    │  3. Skill 选择                                           │
    │     ├── 分析用户意图                                     │
    │     ├── 选择对应 Skill 模板                              │
    │     └── 组装 Prompt                                      │
    │                                                          │
    │  4. LLM 调用                                             │
    │     ├── Claude API 流式调用                              │
    │     ├── WebSocket 推送给前端                             │
    │     └── 处理响应                                         │
    │                                                          │
    │  5. 记忆更新                                             │
    │     ├── 短期记忆写入 Redis                                │
    │     ├── 会话结束时生成摘要                                │
    │     └── 摘要向量化存入 Pinecone                          │
    │                                                          │
    └─────────────────────────────────────────────────────────┤
                                                                │
响应推送 ◄─────────────────────────────────────────────────────┘
```

---

## 9. AI Multimodal Service

**职责**：语音识别、语音合成、数字人驱动（讯飞集成）

### 9.1 功能模块

```
AI Multimodal Service
├── 讯飞语音集成
│   ├── 语音识别（讯飞语音听写 API）
│   │   ├── 实时语音流识别
│   │   ├── 中文/英文支持
│   │   └── 儿童语音优化
│   │
│   └── 语音合成（讯飞语音合成 API）
│   │   ├── 文字转语音
│   │   ├── 儿童友好音色
│   │   ├── 语速调节
│   │   └── 情感表达
│   │
├── 讯飞数字人集成
│   ├── 数字人形象管理
│   │   ├── 预设形象（老师形象 3-5 种）
│   │   ├── 用户自定义（未来扩展）
│   │
│   ├── 表情/动作驱动
│   │   ├── 表情：开心、鼓励、思考、惊讶、庆祝
│   │   ├── 动作：点头、挥手、比心、鼓掌
│   │   ├── 口型同步
│   │
│   └── 实时渲染输出
│       ├── 视频流生成
│       ├── 低延迟推流（WebSocket）
│       └── 多端适配
│
└── 请求调度
    ├── 并发控制（讯飞 API 限流）
    ├── 降级策略
    └── 成本监控
```

### 9.2 API 设计

```
POST /api/voice/recognize
请求：音频流
响应：{
    "text": "识别的文字",
    "is_final": true,
    "segments": [...]
}

POST /api/voice/synthesize
请求：{
    "text": "要合成的文字",
    "voice_type": "xiaoyan",
    "speed": 50,
    "emotion": "happy"
}
响应：音频文件URL

WebSocket /api/digital-human/stream
消息格式：{
    "type": "video_frame",
    "data": "base64编码的视频帧",
    "audio_sync": "音频时间戳"
}
```

---

## 10. Sandbox Service

**职责**：代码执行、可视化渲染、安全隔离

### 10.1 功能模块

```
Sandbox Service
├── 代码执行模块
│   ├── 多语言支持（Python / JavaScript / HTML+CSS）
│   ├── 执行环境隔离（Docker 容器）
│   ├── 资源限制（CPU/内存/时间）
│   ├── 输出捕获（stdout/stderr/返回值）
│   └── 错误处理与提示
│
├── 可视化渲染模块
│   ├── 算法可视化（排序/搜索等）
│   ├── 数据结构可视化（数组/树/图）
│   ├── 代码执行过程可视化
│   ├── 图形化输出（Canvas/SVG）
│   └── 实时渲染推流
│
├── 项目运行模块
│   ├── 完整项目运行（网站/游戏）
│   ├── 文件系统模拟
│   ├── 依赖安装
│   ├── 端口映射
│   └── 长时运行支持
│
└── 安全隔离模块
│   ├── 网络隔离（无外网访问）
│   ├── 文件系统隔离
│   ├── 资源限制
│   ├── 恶意代码检测
│   └── 执行超时强制终止
```

### 10.2 安全隔离方案

| 方案 | 安全级别 | 适用阶段 |
|------|----------|----------|
| Docker + gVisor | 中-高 | MVP |
| Firecracker microVM | 高 | 生产环境 |

### 10.3 容器配置

```yaml
security:
  cpu_limit: 0.5
  memory_limit: 256MB
  time_limit: 30s
  network: none
  read_only_paths:
    - /usr
  writable_paths:
    - /workspace
  pid_limit: 64
  run_as_non_root: true
```

### 10.4 API 设计

```
POST /api/sandbox/execute
请求：{
    "code": "用户代码",
    "language": "python",
    "inputs": "可选输入",
    "visualize": true
}
响应：{
    "stdout": "标准输出",
    "stderr": "错误输出",
    "result": "返回值",
    "visualizations": [...],
    "execution_time": 1.2,
    "status": "success"
}

POST /api/sandbox/project/run
请求：{
    "project_type": "web",
    "files": {...},
    "dependencies": [...]
}
响应：{
    "run_id": "uuid",
    "access_url": "https://preview.codebuddy.ai/{run_id}",
    "status": "running",
    "expires_at": "..."
}
```

---

## 11. 服务间通信

### 11.1 同步通信（HTTP/REST）

```
服务调用规范：
├── HTTP/REST 协议
├── JSON 格式
├── 服务发现（K8s DNS）
├── 负载均衡
├── 超时设置（3秒默认，AI服务10秒）
├── 重试策略（幂等接口可重试）
└── 熔断降级
```

### 11.2 异步通信（消息队列）

```
消息队列选型：
├── Redis + Celery（初期）
│   └── 简单，已有基础设施
│
└── RabbitMQ（后期）
    └── 可靠性高，支持复杂路由
```

### 11.3 异步任务场景

| 场景 | 触发方 | 处理方 | 优先级 |
|------|--------|--------|--------|
| 学习进度更新 | Learning Service | AI Assistant | 普通 |
| 对话摘要生成 | AI Assistant | AI Assistant | 低 |
| 学习报告生成 | 定时任务 | Learning Service | 低 |
| 徽章解锁检查 | Learning Service | Learning Service | 普通 |
| 语音识别任务 | AI Assistant | Multimodal Service | 高 |

### 11.4 事件类型

```
├── user.progress_updated
├── user.badge_unlocked
├── chat.session_ended
├── code.execution_completed
└── voice.transcription_done
```

---

## 12. 可观测性

### 12.1 技术选型

| 类型 | 工具 |
|------|------|
| 指标监控 | Prometheus + Grafana |
| 日志收集 | Loki |
| 链路追踪 | Jaeger |
| 告警 | Alertmanager |

### 12.2 监控指标

```
系统级：CPU/内存/磁盘/网络IO/容器状态

服务级：QPS/响应时间(P50/P95/P99)/错误率/活跃连接数

业务级：活跃用户数/对话会话数/代码执行次数/LLM Token消耗/讯飞API调用量
```

### 12.3 日志格式

```json
{
    "timestamp": "2026-04-01T10:30:00Z",
    "level": "INFO",
    "service": "ai-assistant-service",
    "trace_id": "abc123",
    "span_id": "def456",
    "user_id": "user_uuid",
    "message": "LLM调用完成",
    "metadata": {
        "model": "claude-opus-4-6",
        "tokens_used": 1500,
        "latency_ms": 2300
    }
}
```

### 12.4 告警规则

```yaml
alerts:
  - name: service_down
    condition: up{job="service"} == 0
    severity: critical
    
  - name: high_latency
    condition: P95 > 3s
    severity: warning
    
  - name: high_error_rate
    condition: 5xx_rate > 5%
    severity: warning
    
  - name: high_llm_cost
    condition: tokens_1h > 1000000
    severity: warning
```

---

## 13. 技术栈汇总

| 层级 | 技术选型 |
|------|----------|
| 前端 | React 19 + TypeScript + Vite + Tailwind |
| 网关 | FastAPI |
| 业务服务 | FastAPI + PostgreSQL |
| AI 服务 | FastAPI + Redis + Pinecone + LangGraph |
| 多模态服务 | FastAPI + 讯飞 SDK |
| 沙箱服务 | FastAPI + Docker + gVisor |
| 消息队列 | Redis + Celery → RabbitMQ |
| 可观测性 | Prometheus + Grafana + Loki + Jaeger |
| 容器化 | Docker Compose → Kubernetes |

---

## 14. 数据库清单

| 数据库 | 用途 | 服务 |
|--------|------|------|
| PostgreSQL | 用户数据 | user-service |
| PostgreSQL | 学习数据 | learning-service |
| PostgreSQL | 对话历史 | ai-assistant-service |
| Redis | 短期记忆/缓存/队列 | ai-assistant-service |
| Pinecone | 向量检索 | ai-assistant-service |

---

## 15. 开发路线

```
Phase 1：基础架构（2周）
├── Gateway Service
├── User Service
├── 基础数据库
└── Docker Compose 环境

Phase 2：核心学习流程（3周）
├── Learning Service
├── 课程内容录入
├── 前端页面开发
└── 学习进度追踪

Phase 3：AI 对话能力（4周）
├── AI Assistant Service
├── LLM 对话（流式）
├── RAG 知识库
├── 记忆系统
└── Skills 编排

Phase 4：多模态+沙箱（3周）
├── 讯飞语音集成
├── 讯飞数字人集成
├── Sandbox Service
└── 代码执行+可视化

Phase 5：完善+上线（2周）
├── 成就系统
├── 可观测性
├── 性能优化
├── 安全加固
└── 正式上线
```

**总计：约 14 周（3.5 个月）**

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-04-01 | 初始版本 |