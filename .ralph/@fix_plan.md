# CodeBuddyAI - 任务清单

> Ralph 按顺序执行，每次循环完成一个 Section（#### 级别）的所有任务

---

## Phase 1：基础架构

### 1.1.1 项目初始化
- [x] 创建项目根目录结构（services/, shared/）
- [x] 创建 services/ 下各服务子目录（gateway/, user/, learning/, ai-assistant/, multimodal/, sandbox/）
- [x] 创建 shared/ 目录，存放公共代码
- [x] 配置 Python 项目根目录 pyproject.toml（统一依赖管理）
- [x] 各服务子目录创建独立的 pyproject.toml / requirements.txt
- [x] 配置代码规范（black、isort、flake8 配置文件）

### 1.1.2 数据库初始化
- [ ] 创建 docker-compose.yml（PostgreSQL + Redis）
- [ ] 设计 users 数据库 schema（SQL 文件）
- [ ] 设计 auth_credentials 表
- [ ] 设计 parent_links 表
- [ ] 初始化 Alembic 并创建数据库迁移脚本

### 1.1.3 环境配置
- [ ] 创建 .env.example 模板（包含所有服务所需环境变量）
- [ ] 配置开发环境变量
- [ ] 配置统一日志系统（JSON 格式，统一字段）
- [ ] 各服务实现 /health 健康检查端点

### 1.2.1 Gateway Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/gateway/）
- [ ] 配置 CORS 中间件
- [ ] 配置 Swagger 文档（/docs）

### 1.2.2 Gateway Service - 路由配置
- [ ] 实现 /api/v1/user/* 路由转发到 User Service
- [ ] 实现 /api/v1/learning/* 路由转发到 Learning Service
- [ ] 实现 /api/v1/chat/* 路由转发（WebSocket）到 AI Assistant Service
- [ ] 实现 /api/v1/voice/* 路由转发到 Multimodal Service
- [ ] 实现 /api/v1/code/* 路由转发到 Sandbox Service

### 1.2.3 Gateway Service - 认证中间件
- [ ] 实现 JWT 验证中间件（从 Header 提取并验证 Token）
- [ ] 实现 API Key 验证（服务间调用认证）
- [ ] 实现 Token 提取与用户信息注入（注入到请求上下文）

### 1.2.4 Gateway Service - 限流中间件
- [ ] 实现用户级限流（基于 user_id，Redis 计数）
- [ ] 实现 IP 级限流（基于 client IP）
- [ ] 实现 AI 接口特殊限流（更严格的调用频率限制）

### 1.3.1 User Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/user/）
- [ ] 配置 PostgreSQL 数据库连接（SQLAlchemy async）
- [ ] 配置 Redis 连接

### 1.3.2 User Service - 用户认证 API
- [ ] POST /api/v1/user/auth/register - 用户注册（含参数校验、密码 bcrypt 加密）
- [ ] POST /api/v1/user/auth/login - 用户登录（返回 access_token + refresh_token）
- [ ] POST /api/v1/user/auth/logout - 用户登出（Token 黑名单）
- [ ] POST /api/v1/user/auth/refresh - Token 刷新
- [ ] JWT Token 生成与验证工具函数（access 30min, refresh 7days）

### 1.3.3 User Service - 用户档案 API
- [ ] GET /api/v1/user/profile - 获取用户信息
- [ ] PUT /api/v1/user/profile - 更新用户信息
- [ ] PUT /api/v1/user/avatar - 更新头像
- [ ] PUT /api/v1/user/preferences - 更新学习偏好

### 1.3.4 User Service - 家长关联 API
- [ ] POST /api/v1/user/parent/link - 绑定家长邮箱
- [ ] DELETE /api/v1/user/parent/link - 解绑家长
- [ ] PUT /api/v1/user/parent/report-frequency - 设置报告频率

### 1.4.1 前端调整 - 年龄选项更新
- [ ] 修改 OnboardingView.tsx 年龄选项为 12-14 岁
- [ ] 更新表单验证逻辑（适配新年龄范围）

### 1.4.2 前端调整 - API 服务层
- [ ] 创建 services/api.ts - Axios 实例（baseURL、请求/响应拦截器）
- [ ] 创建 services/auth.ts - 认证相关 API（register, login, logout, refresh）
- [ ] 创建 services/user.ts - 用户相关 API（profile, avatar, preferences）

### 1.4.3 前端调整 - 状态管理
- [ ] 完善 useUserStore - 用户状态（user info, loading, error）
- [ ] 实现 Token 存储与自动刷新逻辑
- [ ] 实现登录状态持久化（localStorage）

### 1.4.4 前端调整 - 登录注册对接
- [ ] 对接注册 API（表单提交 → API 调用 → 成功跳转）
- [ ] 对接登录 API
- [ ] 实现登录后跳转逻辑

### 1.5.1 测试 - 单元测试
- [ ] 用户注册逻辑测试（密码加密、Token 生成）
- [ ] 用户登录逻辑测试（验证、Token 刷新）
- [ ] 用户档案 CRUD 测试

### 1.5.2 测试 - API 集成测试
- [ ] POST /api/v1/user/auth/register - 注册流程测试
- [ ] POST /api/v1/user/auth/login - 登录流程测试
- [ ] GET /api/v1/user/profile - 获取用户信息测试
- [ ] JWT 验证中间件测试

### 1.5.3 测试 - 端到端测试
- [ ] 用户注册 → 登录 → 访问受保护页面流程
- [ ] Token 过期自动刷新流程

---

## Phase 2：核心学习流程

### 2.1.1 Learning Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/learning/）
- [ ] 配置 PostgreSQL 数据库连接

### 2.1.2 Learning Service - 数据库设计
- [ ] 创建 courses 表
- [ ] 创建 learning_paths 表
- [ ] 创建 user_progress 表
- [ ] 创建 course_sessions 表
- [ ] 创建 badges 表
- [ ] 创建 user_badges 表
- [ ] 创建 points_log 表
- [ ] 创建 Alembic 数据库迁移脚本

### 2.1.3 Learning Service - 课程管理 API
- [ ] GET /api/v1/learning/courses - 获取课程列表（分页、筛选）
- [ ] GET /api/v1/learning/courses/{id} - 获取课程详情
- [ ] POST /api/v1/learning/courses - 创建课程（管理员）
- [ ] PUT /api/v1/learning/courses/{id} - 更新课程（管理员）
- [ ] DELETE /api/v1/learning/courses/{id} - 删除课程（管理员）

### 2.1.4 Learning Service - 学习路径 API
- [ ] GET /api/v1/learning/paths - 获取学习路径列表
- [ ] GET /api/v1/learning/paths/{id} - 获取路径详情
- [ ] POST /api/v1/learning/paths/{id}/enroll - 报名学习路径
- [ ] GET /api/v1/learning/paths/{id}/progress - 获取路径进度

### 2.1.5 Learning Service - 进度追踪 API
- [ ] POST /api/v1/learning/progress/start - 开始学习课程
- [ ] POST /api/v1/learning/progress/update - 更新学习进度
- [ ] POST /api/v1/learning/progress/complete - 完成课程
- [ ] GET /api/v1/learning/progress/me - 获取我的学习进度

### 2.1.6 Learning Service - 成就系统 API
- [ ] GET /api/v1/learning/badges - 获取徽章列表
- [ ] GET /api/v1/learning/badges/me - 获取我的徽章
- [ ] GET /api/v1/learning/points/me - 获取我的积分
- [ ] GET /api/v1/learning/points/history - 获取积分历史

### 2.2.1 课程内容 - 网站开发路径课程
- [ ] 创建"网站开发路径"学习路径数据
- [ ] 录入 Figma 入门课程内容
- [ ] 录入 Claude Code 基础课程内容
- [ ] 录入 Cloudflare 部署课程内容
- [ ] 创建课程素材（图片、示例代码）

### 2.2.2 课程内容 - 课程版本管理
- [ ] 设计课程版本号规范
- [ ] 实现课程版本切换
- [ ] 实现课程更新通知

### 2.3.1 前端对接 - 课程浏览
- [ ] 创建 services/learning.ts - 学习相关 API 封装
- [ ] 对接课程列表 API（ExplorerView 改造）
- [ ] 对接学习路径 API
- [ ] 实现课程详情页

### 2.3.2 前端对接 - 学习进度
- [ ] 创建 useLearningStore - 学习状态管理
- [ ] 对接进度追踪 API
- [ ] 更新 DashboardView 展示真实进度
- [ ] 实现课程开始/完成流程

### 2.3.3 前端对接 - 成就展示
- [ ] 对接徽章 API
- [ ] 对接积分 API
- [ ] 更新成就展示组件

### 2.4.1 测试 - 单元测试
- [ ] 课程 CRUD 逻辑测试
- [ ] 学习路径解锁逻辑测试
- [ ] 进度计算逻辑测试
- [ ] 积分计算规则测试

### 2.4.2 测试 - API 集成测试
- [ ] GET /api/v1/learning/courses - 课程列表测试
- [ ] GET /api/v1/learning/paths/{id} - 学习路径测试
- [ ] POST /api/v1/learning/progress/start - 开始学习测试
- [ ] POST /api/v1/learning/progress/complete - 完成课程测试
- [ ] 徽章解锁触发测试

### 2.4.3 测试 - 端到端测试
- [ ] 选择学习路径 → 开始课程 → 完成课程 → 获得徽章流程
- [ ] 积分累计展示测试

---

## Phase 3：AI 对话能力

### 3.1.1 AI Assistant Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/ai-assistant/）
- [ ] 配置 Redis 连接（短期记忆）
- [ ] 配置 PostgreSQL 连接（长期记忆）
- [ ] 配置 Pinecone 连接（向量检索）

### 3.1.2 AI Assistant Service - 数据库设计
- [ ] 创建 chat_sessions 表
- [ ] 创建 chat_messages 表
- [ ] 创建 memory_summaries 表
- [ ] 创建 knowledge_base 表

### 3.1.3 AI Assistant Service - LLM 对话模块
- [ ] 集成 Claude API（anthropic SDK）
- [ ] 实现流式输出（SSE/WebSocket）
- [ ] 实现多轮对话管理（上下文拼接）
- [ ] 实现对话历史存储
- [ ] 实现 Prompt 模板管理

### 3.1.4 AI Assistant Service - RAG 检索模块
- [ ] 初始化 Pinecone 索引
- [ ] 实现文本向量化（embedding）
- [ ] 实现知识库检索（top-k 搜索）
- [ ] 实现检索结果排序与过滤
- [ ] 实现知识库管理 API（CRUD）

### 3.1.5 AI Assistant Service - 记忆系统
- [ ] 实现短期记忆（Redis 存储，会话级）
- [ ] 实现长期记忆（PostgreSQL 存储）
- [ ] 实现记忆向量化（存入 Pinecone）
- [ ] 实现语义记忆检索
- [ ] 实现会话摘要生成

### 3.1.6 AI Assistant Service - Skills 编排
- [ ] 设计 Skills 定义规范（JSON Schema）
- [ ] 实现 explain_concept Skill（概念解释）
- [ ] 实现 guide_step_by_step Skill（步骤引导）
- [ ] 实现 debug_code Skill（代码调试）
- [ ] 实现 generate_template Skill（代码模板生成）
- [ ] 实现 Skill 调度引擎（意图识别 → Skill 匹配）

### 3.1.7 AI Assistant Service - 对话 API
- [ ] WS /api/v1/chat/stream - 流式对话
- [ ] POST /api/v1/chat/sessions - 创建会话
- [ ] GET /api/v1/chat/sessions/{id} - 获取会话历史
- [ ] DELETE /api/v1/chat/sessions/{id} - 删除会话

### 3.2.1 知识库 - 编程知识
- [ ] 整理 Python 基础知识点
- [ ] 整理 JavaScript 基础知识点
- [ ] 整理 HTML/CSS 基础知识点

### 3.2.2 知识库 - 工具知识
- [ ] 整理 Figma 使用教程
- [ ] 整理 Claude Code 使用教程
- [ ] 整理 Cloudflare 部署教程

### 3.2.3 知识库 - 常见问题
- [ ] 整理常见错误及解决方案
- [ ] 整理常见概念解释

### 3.3.1 前端对话界面 - ChatView
- [ ] 创建 ChatView.tsx - AI 对话页面
- [ ] 实现消息列表组件（区分用户/AI 消息）
- [ ] 实现消息输入组件（文本框 + 发送按钮）
- [ ] 实现流式消息展示（逐字渲染）

### 3.3.2 前端对话界面 - 对话功能
- [ ] 创建 services/chat.ts - 对话 API 封装
- [ ] 实现 WebSocket 连接管理
- [ ] 实现消息发送/接收逻辑
- [ ] 实现对话历史加载

### 3.3.3 前端对话界面 - 交互优化
- [ ] 实现打字机效果（AI 回复动画）
- [ ] 实现消息加载状态（骨架屏/Loading）
- [ ] 实现错误处理与自动重连

### 3.4.1 测试 - 单元测试
- [ ] RAG 检索逻辑测试（向量相似度计算）
- [ ] 记忆系统测试（短期/长期记忆存储与检索）
- [ ] Skills 调度逻辑测试
- [ ] Prompt 模板渲染测试

### 3.4.2 测试 - API 集成测试
- [ ] WS /api/v1/chat/stream - 流式对话测试
- [ ] POST /api/v1/chat/sessions - 会话创建测试
- [ ] 对话历史存储与检索测试
- [ ] RAG 检索与 LLM 调用集成测试

### 3.4.3 测试 - 端到端测试
- [ ] 用户提问 → RAG 检索 → LLM 回复 → 流式展示流程
- [ ] 多轮对话上下文保持测试
- [ ] 会话摘要生成测试

### 3.4.4 测试 - 性能测试
- [ ] 流式输出延迟测试（首字节 < 500ms）
- [ ] RAG 检索性能测试（< 100ms）
- [ ] 并发对话压力测试（10 并发用户）

---

## Phase 4：多模态+沙箱

### 4.1.1 Multimodal Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/multimodal/）
- [ ] 申请讯飞 API 凭证
- [ ] 配置讯飞 SDK

### 4.1.2 Multimodal Service - 语音识别
- [ ] 集成讯飞语音听写 API
- [ ] POST /api/v1/voice/recognize - 语音识别端点
- [ ] 实现音频流处理
- [ ] 实现儿童语音优化配置（语速、口音适配）

### 4.1.3 Multimodal Service - 语音合成
- [ ] 集成讯飞语音合成 API
- [ ] POST /api/v1/voice/synthesize - 语音合成端点
- [ ] 实现音色选择（适合青少年的声音）
- [ ] 实现语速/情感控制

### 4.1.4 Multimodal Service - 数字人
- [ ] 集成讯飞数字人 SDK
- [ ] WS /api/v1/digital-human/stream - 数字人视频流
- [ ] 实现表情驱动
- [ ] 实现动作驱动
- [ ] 实现口型同步

### 4.2.1 Sandbox Service - 项目搭建
- [ ] 初始化 FastAPI 项目（services/sandbox/）
- [ ] 配置 Docker 连接（Docker SDK for Python）
- [ ] 准备基础执行镜像（Python + Node.js）

### 4.2.2 Sandbox Service - 容器管理
- [ ] 实现容器创建与销毁
- [ ] 实现资源限制配置（CPU/内存/磁盘）
- [ ] 实现网络隔离（无外网访问）
- [ ] 实现执行超时控制

### 4.2.3 Sandbox Service - 代码执行 API
- [ ] POST /api/v1/sandbox/execute - 执行代码
- [ ] 实现 Python 执行器
- [ ] 实现 JavaScript 执行器
- [ ] 实现 HTML/CSS 预览
- [ ] 实现输出捕获（stdout/stderr）

### 4.2.4 Sandbox Service - 可视化渲染
- [ ] 实现排序算法可视化
- [ ] 实现数据结构可视化
- [ ] 实现图形输出渲染

### 4.2.5 Sandbox Service - 项目运行 API
- [ ] POST /api/v1/sandbox/project/run - 运行项目
- [ ] GET /api/v1/sandbox/project/{id}/status - 获取运行状态
- [ ] DELETE /api/v1/sandbox/project/{id} - 停止项目
- [ ] 实现端口映射
- [ ] 实现依赖安装（npm install / pip install）

### 4.3.1 前端集成 - 语音组件
- [ ] 创建 VoiceInput.tsx - 语音输入组件（录音按钮）
- [ ] 创建 VoiceOutput.tsx - 语音播放组件
- [ ] 对接语音识别 API
- [ ] 对接语音合成 API

### 4.3.2 前端集成 - 数字人组件
- [ ] 创建 DigitalHuman.tsx - 数字人展示组件
- [ ] 实现视频流播放
- [ ] 实现表情/动作控制 UI

### 4.3.3 前端集成 - 代码编辑器
- [ ] 创建 CodeLabView.tsx - 代码实验室页面
- [ ] 集成 Monaco Editor
- [ ] 实现代码高亮（Python/JS/HTML）
- [ ] 实现代码自动补全

### 4.3.4 前端集成 - 执行结果展示
- [ ] 创建 services/sandbox.ts - 代码执行 API 封装
- [ ] 实现执行结果展示面板
- [ ] 实现错误提示高亮
- [ ] 实现可视化渲染展示

### 4.4.1 测试 - 单元测试
- [ ] 容器创建/销毁逻辑测试
- [ ] 资源限制配置测试
- [ ] 代码输出捕获测试

### 4.4.2 测试 - API 集成测试
- [ ] POST /api/v1/voice/recognize - 语音识别测试
- [ ] POST /api/v1/voice/synthesize - 语音合成测试
- [ ] WS /api/v1/digital-human/stream - 数字人流测试
- [ ] POST /api/v1/sandbox/execute - 代码执行测试
- [ ] POST /api/v1/sandbox/project/run - 项目运行测试

### 4.4.3 测试 - 安全测试
- [ ] 沙箱网络隔离测试（无外网访问）
- [ ] 沙箱文件系统隔离测试（无法访问宿主机）
- [ ] 资源限制测试（CPU/内存/时间超限自动终止）
- [ ] 恶意代码检测测试（危险命令拦截）

### 4.4.4 测试 - 端到端测试
- [ ] 语音输入 → 识别 → AI 对话流程
- [ ] 代码输入 → 执行 → 结果展示流程
- [ ] 项目创建 → 运行 → 访问预览流程

---

## Phase 5：完善+上线

### 5.1 成就系统完善
- [ ] 实现徽章解锁逻辑（条件触发）
- [ ] 实现积分计算规则（课程完成、连续学习等）
- [ ] 实现排行榜功能（Redis sorted set）
- [ ] 实现成就通知（WebSocket 推送）

### 5.2.1 可观测性 - 监控系统
- [ ] 部署 Prometheus（docker-compose 新增服务）
- [ ] 部署 Grafana
- [ ] 配置各服务指标采集（FastAPI Prometheus middleware）
- [ ] 创建监控仪表盘

### 5.2.2 可观测性 - 日志系统
- [ ] 部署 Loki
- [ ] 配置各服务日志采集
- [ ] 创建日志查询面板

### 5.2.3 可观测性 - 链路追踪
- [ ] 部署 Jaeger
- [ ] 配置 OpenTelemetry SDK
- [ ] 实现链路追踪中间件

### 5.2.4 可观测性 - 告警配置
- [ ] 配置服务可用性告警
- [ ] 配置性能告警（响应时间、错误率）
- [ ] 配置成本告警
- [ ] 配置告警通知渠道

### 5.3 性能优化
- [ ] 数据库查询优化（索引、N+1 问题）
- [ ] API 响应时间优化（缓存策略）
- [ ] 前端加载优化（代码分割、懒加载）
- [ ] 缓存策略优化（Redis TTL 设计）

### 5.4 安全加固
- [ ] API 安全审计
- [ ] SQL 注入防护（参数化查询检查）
- [ ] XSS 防护（输出转义检查）
- [ ] CSRF 防护（Token 机制）
- [ ] 敏感数据加密（传输层 + 存储层）

### 5.5.1 测试 - 单元测试（补充）
- [ ] 徽章解锁逻辑测试
- [ ] 积分计算规则测试
- [ ] 排行榜排序逻辑测试

### 5.5.2 测试 - API 集成测试（全量回归）
- [ ] 用户模块全量 API 回归测试
- [ ] 学习模块全量 API 回归测试
- [ ] AI 对话模块全量 API 回归测试
- [ ] 多模态模块全量 API 回归测试
- [ ] 沙箱模块全量 API 回归测试

### 5.5.3 测试 - 端到端测试（核心流程）
- [ ] 新用户注册 → 选择路径 → 学习课程 → AI 对话 → 完成课程 → 获得徽章
- [ ] 语音交互学习流程
- [ ] 代码编写 → 执行 → 可视化流程

### 5.5.4 测试 - 性能测试
- [ ] API 响应时间测试（P95 < 500ms）
- [ ] 数据库查询性能测试
- [ ] 前端首屏加载时间测试（< 3s）
- [ ] 并发用户压力测试（50 并发用户）

### 5.5.5 测试 - 安全测试
- [ ] SQL 注入防护验证
- [ ] XSS 防护验证
- [ ] CSRF 防护验证
- [ ] JWT Token 安全测试
- [ ] API 限流验证

### 5.6 部署上线
- [ ] 准备生产环境配置（docker-compose.prod.yml）
- [ ] 配置 CI/CD 流水线（GitHub Actions）
- [ ] 执行数据库迁移
- [ ] 部署各服务
- [ ] 验证服务可用性（健康检查 + 冒烟测试）
- [ ] 监控上线（确认指标采集正常）
