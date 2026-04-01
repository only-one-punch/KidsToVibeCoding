# CodeBuddyAI 实施计划

**版本**: v1.0
**创建日期**: 2026-04-01
**预计总工期**: 14 周（3.5 个月）

---

## 前置说明

### 团队分工建议

| 角色 | 人数 | 职责 |
|------|------|------|
| 前端开发 | 1人 | 前端 API 对接、新页面开发 |
| 后端开发 | 1人 | User Service、Learning Service、Gateway |
| AI 开发 | 2-3人 | AI Assistant Service、Multimodal Service、Sandbox Service |

### 前端现状

- UI 框架已完成，不需要重写
- 需要调整：年龄选项、API 对接层、状态管理
- 需要新增：AI 对话界面、代码编辑界面

---

## Phase 1：基础架构（2周）

**目标**：搭建 Gateway + User Service + 基础数据库，完成用户注册登录流程

### 1.1 基础设施（第1周）

#### 1.1.1 项目初始化
- [ ] 创建项目根目录结构
- [ ] 创建 `services/` 目录，初始化各服务子目录
- [ ] 创建 `shared/` 目录，存放公共代码
- [ ] 配置 Python 项目依赖（requirements.txt / pyproject.toml）
- [ ] 配置代码规范（black、isort、flake8）

#### 1.1.2 数据库初始化
- [ ] 创建 `docker-compose.yml`（PostgreSQL + Redis）
- [ ] 设计 `users` 数据库 schema
- [ ] 设计 `auth_credentials` 表
- [ ] 设计 `parent_links` 表
- [ ] 创建数据库迁移脚本（Alembic）

#### 1.1.3 环境配置
- [ ] 创建 `.env.example` 模板
- [ ] 配置开发环境变量
- [ ] 配置日志系统（统一格式）
- [ ] 配置健康检查端点

### 1.2 Gateway Service（第1周）

#### 1.2.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 配置 CORS
- [ ] 配置 Swagger 文档

#### 1.2.2 路由配置
- [ ] 实现 `/api/user/*` 路由转发
- [ ] 实现 `/api/learning/*` 路由转发
- [ ] 实现 `/api/chat/*` 路由转发（WebSocket）
- [ ] 实现 `/api/voice/*` 路由转发
- [ ] 实现 `/api/code/*` 路由转发

#### 1.2.3 认证中间件
- [ ] 实现 JWT 验证中间件
- [ ] 实现 API Key 验证（服务间调用）
- [ ] 实现 Token 提取与用户信息注入

#### 1.2.4 限流中间件
- [ ] 实现用户级限流
- [ ] 实现 IP 级限流
- [ ] 实现 AI 接口特殊限流

### 1.3 User Service（第1-2周）

#### 1.3.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 配置数据库连接
- [ ] 配置 Redis 连接

#### 1.3.2 用户认证 API
- [ ] POST `/api/user/auth/register` - 用户注册
- [ ] POST `/api/user/auth/login` - 用户登录
- [ ] POST `/api/user/auth/logout` - 用户登出
- [ ] POST `/api/user/auth/refresh` - Token 刷新
- [ ] 密码加密（bcrypt）
- [ ] JWT Token 生成与验证

#### 1.3.3 用户档案 API
- [ ] GET `/api/user/profile` - 获取用户信息
- [ ] PUT `/api/user/profile` - 更新用户信息
- [ ] PUT `/api/user/avatar` - 更新头像
- [ ] PUT `/api/user/preferences` - 更新学习偏好

#### 1.3.4 家长关联 API
- [ ] POST `/api/user/parent/link` - 绑定家长邮箱
- [ ] DELETE `/api/user/parent/link` - 解绑家长
- [ ] PUT `/api/user/parent/report-frequency` - 设置报告频率

### 1.4 前端调整（第2周）

#### 1.4.1 年龄选项更新
- [ ] 修改 `OnboardingView.tsx` 年龄选项为 12-14 岁
- [ ] 更新表单验证逻辑

#### 1.4.2 API 服务层
- [ ] 创建 `services/api.ts` - API 请求封装
- [ ] 创建 `services/auth.ts` - 认证相关 API
- [ ] 创建 `services/user.ts` - 用户相关 API
- [ ] 配置 Axios 实例（baseURL、拦截器）

#### 1.4.3 状态管理
- [ ] 完善 `useUserStore` - 用户状态
- [ ] 实现 Token 存储与自动刷新
- [ ] 实现登录状态持久化

#### 1.4.4 登录注册对接
- [ ] 对接注册 API
- [ ] 对接登录 API
- [ ] 实现登录后跳转逻辑

---

## Phase 2：核心学习流程（3周）

**目标**：完成 Learning Service，实现课程浏览、学习进度追踪

### 2.1 Learning Service（第2-4周）

#### 2.1.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 配置数据库连接

#### 2.1.2 数据库设计
- [ ] 创建 `courses` 表
- [ ] 创建 `learning_paths` 表
- [ ] 创建 `user_progress` 表
- [ ] 创建 `course_sessions` 表
- [ ] 创建 `badges` 表
- [ ] 创建 `user_badges` 表
- [ ] 创建 `points_log` 表
- [ ] 创建数据库迁移脚本

#### 2.1.3 课程管理 API
- [ ] GET `/api/learning/courses` - 获取课程列表
- [ ] GET `/api/learning/courses/{id}` - 获取课程详情
- [ ] POST `/api/learning/courses` - 创建课程（管理员）
- [ ] PUT `/api/learning/courses/{id}` - 更新课程（管理员）
- [ ] DELETE `/api/learning/courses/{id}` - 删除课程（管理员）

#### 2.1.4 学习路径 API
- [ ] GET `/api/learning/paths` - 获取学习路径列表
- [ ] GET `/api/learning/paths/{id}` - 获取路径详情
- [ ] POST `/api/learning/paths/{id}/enroll` - 报名学习路径
- [ ] GET `/api/learning/paths/{id}/progress` - 获取路径进度

#### 2.1.5 进度追踪 API
- [ ] POST `/api/learning/progress/start` - 开始学习课程
- [ ] POST `/api/learning/progress/update` - 更新学习进度
- [ ] POST `/api/learning/progress/complete` - 完成课程
- [ ] GET `/api/learning/progress/me` - 获取我的学习进度

#### 2.1.6 成就系统 API
- [ ] GET `/api/learning/badges` - 获取徽章列表
- [ ] GET `/api/learning/badges/me` - 获取我的徽章
- [ ] GET `/api/learning/points/me` - 获取我的积分
- [ ] GET `/api/learning/points/history` - 获取积分历史

### 2.2 课程内容（第4周）

#### 2.2.1 网站开发路径课程
- [ ] 创建"网站开发路径"学习路径
- [ ] 录入 Figma 入门课程
- [ ] 录入 Claude Code 基础课程
- [ ] 录入 Cloudflare 部署课程
- [ ] 创建课程素材（图片、示例代码）

#### 2.2.2 课程版本管理
- [ ] 设计课程版本号规范
- [ ] 实现课程版本切换
- [ ] 实现课程更新通知

### 2.3 前端对接（第3-4周）

#### 2.3.1 课程浏览
- [ ] 创建 `services/learning.ts` - 学习相关 API
- [ ] 对接课程列表 API（ExplorerView）
- [ ] 对接学习路径 API
- [ ] 实现课程详情页

#### 2.3.2 学习进度
- [ ] 创建 `useLearningStore` - 学习状态管理
- [ ] 对接进度追踪 API
- [ ] 更新 DashboardView 展示真实进度
- [ ] 实现课程开始/完成流程

#### 2.3.3 成就展示
- [ ] 对接徽章 API
- [ ] 对接积分 API
- [ ] 更新成就展示组件

---

## Phase 3：AI 对话能力（4周）

**目标**：完成 AI Assistant Service，实现 AI 老师对话功能

### 3.1 AI Assistant Service（第5-8周）

#### 3.1.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 配置 Redis 连接
- [ ] 配置 PostgreSQL 连接
- [ ] 配置 Pinecone 连接

#### 3.1.2 数据库设计
- [ ] 创建 `chat_sessions` 表
- [ ] 创建 `chat_messages` 表
- [ ] 创建 `memory_summaries` 表
- [ ] 创建 `knowledge_base` 表

#### 3.1.3 LLM 对话模块
- [ ] 集成 Claude API（anthropic SDK）
- [ ] 实现流式输出（SSE/WebSocket）
- [ ] 实现多轮对话管理
- [ ] 实现对话历史存储
- [ ] 实现 Prompt 模板管理

#### 3.1.4 RAG 检索模块
- [ ] 初始化 Pinecone 索引
- [ ] 实现文本向量化（embedding）
- [ ] 实现知识库检索
- [ ] 实现检索结果排序
- [ ] 实现知识库管理 API

#### 3.1.5 记忆系统
- [ ] 实现短期记忆（Redis 存储）
- [ ] 实现长期记忆（PostgreSQL 存储）
- [ ] 实现记忆向量化
- [ ] 实现语义记忆检索
- [ ] 实现会话摘要生成

#### 3.1.6 Skills 编排
- [ ] 设计 Skills 定义规范
- [ ] 实现 `explain_concept` Skill
- [ ] 实现 `guide_step_by_step` Skill
- [ ] 实现 `debug_code` Skill
- [ ] 实现 `generate_template` Skill
- [ ] 实现 Skill 调度引擎

#### 3.1.7 对话 API
- [ ] WS `/api/chat/stream` - 流式对话
- [ ] POST `/api/chat/sessions` - 创建会话
- [ ] GET `/api/chat/sessions/{id}` - 获取会话历史
- [ ] DELETE `/api/chat/sessions/{id}` - 删除会话

### 3.2 知识库建设（第6-7周）

#### 3.2.1 编程知识
- [ ] 整理 Python 基础知识点
- [ ] 整理 JavaScript 基础知识点
- [ ] 整理 HTML/CSS 基础知识点

#### 3.2.2 工具知识
- [ ] 整理 Figma 使用教程
- [ ] 整理 Claude Code 使用教程
- [ ] 整理 Cloudflare 部署教程

#### 3.2.3 常见问题
- [ ] 整理常见错误及解决方案
- [ ] 整理常见概念解释

### 3.3 前端对话界面（第7-8周）

#### 3.3.1 ChatView 组件
- [ ] 创建 `ChatView.tsx` - AI 对话页面
- [ ] 实现消息列表组件
- [ ] 实现消息输入组件
- [ ] 实现流式消息展示

#### 3.3.2 对话功能
- [ ] 创建 `services/chat.ts` - 对话 API
- [ ] 实现 WebSocket 连接
- [ ] 实现消息发送/接收
- [ ] 实现对话历史加载

#### 3.3.3 交互优化
- [ ] 实现打字机效果
- [ ] 实现消息加载状态
- [ ] 实现错误处理与重连

---

## Phase 4：多模态+沙箱（3周）

**目标**：完成语音、数字人、代码执行功能

### 4.1 AI Multimodal Service（第8-10周）

#### 4.1.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 申请讯飞 API 凭证
- [ ] 配置讯飞 SDK

#### 4.1.2 语音识别
- [ ] 集成讯飞语音听写 API
- [ ] POST `/api/voice/recognize` - 语音识别
- [ ] 实现音频流处理
- [ ] 实现儿童语音优化配置

#### 4.1.3 语音合成
- [ ] 集成讯飞语音合成 API
- [ ] POST `/api/voice/synthesize` - 语音合成
- [ ] 实现音色选择
- [ ] 实现语速/情感控制

#### 4.1.4 数字人
- [ ] 集成讯飞数字人 SDK
- [ ] WS `/api/digital-human/stream` - 数字人视频流
- [ ] 实现表情驱动
- [ ] 实现动作驱动
- [ ] 实现口型同步

### 4.2 Sandbox Service（第9-10周）

#### 4.2.1 项目搭建
- [ ] 初始化 FastAPI 项目
- [ ] 配置 Docker 连接
- [ ] 准备基础执行镜像

#### 4.2.2 容器管理
- [ ] 实现容器创建与销毁
- [ ] 实现资源限制配置
- [ ] 实现网络隔离
- [ ] 实现执行超时控制

#### 4.2.3 代码执行 API
- [ ] POST `/api/sandbox/execute` - 执行代码
- [ ] 实现 Python 执行器
- [ ] 实现 JavaScript 执行器
- [ ] 实现 HTML/CSS 预览
- [ ] 实现输出捕获

#### 4.2.4 可视化渲染
- [ ] 实现排序算法可视化
- [ ] 实现数据结构可视化
- [ ] 实现图形输出渲染

#### 4.2.5 项目运行 API
- [ ] POST `/api/sandbox/project/run` - 运行项目
- [ ] GET `/api/sandbox/project/{id}/status` - 获取状态
- [ ] DELETE `/api/sandbox/project/{id}` - 停止项目
- [ ] 实现端口映射
- [ ] 实现依赖安装

### 4.3 前端集成（第9-10周）

#### 4.3.1 语音组件
- [ ] 创建 `VoiceInput.tsx` - 语音输入组件
- [ ] 创建 `VoiceOutput.tsx` - 语音播放组件
- [ ] 对接语音识别 API
- [ ] 对接语音合成 API

#### 4.3.2 数字人组件
- [ ] 创建 `DigitalHuman.tsx` - 数字人展示组件
- [ ] 实现视频流播放
- [ ] 实现表情/动作控制

#### 4.3.3 代码编辑器
- [ ] 创建 `CodeLabView.tsx` - 代码实验室页面
- [ ] 集成 Monaco Editor
- [ ] 实现代码高亮
- [ ] 实现代码自动补全

#### 4.3.4 执行结果展示
- [ ] 创建 `services/sandbox.ts` - 代码执行 API
- [ ] 实现执行结果展示
- [ ] 实现错误提示
- [ ] 实现可视化展示

---

## Phase 5：完善+上线（2周）

**目标**：系统完善、测试、部署上线

### 5.1 成就系统完善（第11周）

- [ ] 实现徽章解锁逻辑
- [ ] 实现积分计算规则
- [ ] 实现排行榜功能
- [ ] 实现成就通知

### 5.2 可观测性部署（第11周）

#### 5.2.1 监控系统
- [ ] 部署 Prometheus
- [ ] 部署 Grafana
- [ ] 配置各服务指标采集
- [ ] 创建监控仪表盘

#### 5.2.2 日志系统
- [ ] 部署 Loki
- [ ] 配置日志采集
- [ ] 创建日志查询面板

#### 5.2.3 链路追踪
- [ ] 部署 Jaeger
- [ ] 配置 OpenTelemetry
- [ ] 实现链路追踪中间件

#### 5.2.4 告警配置
- [ ] 配置服务可用性告警
- [ ] 配置性能告警
- [ ] 配置成本告警
- [ ] 配置告警通知渠道

### 5.3 性能优化（第12周）

- [ ] 数据库查询优化
- [ ] API 响应时间优化
- [ ] 前端加载优化
- [ ] 缓存策略优化

### 5.4 安全加固（第12周）

- [ ] API 安全审计
- [ ] SQL 注入防护
- [ ] XSS 防护
- [ ] CSRF 防护
- [ ] 敏感数据加密

### 5.5 测试（第12周）

- [ ] 单元测试（核心模块）
- [ ] API 集成测试
- [ ] 端到端测试
- [ ] 性能测试
- [ ] 安全测试

### 5.6 部署上线（第12周）

- [ ] 准备生产环境配置
- [ ] 配置 CI/CD 流水线
- [ ] 执行数据库迁移
- [ ] 部署各服务
- [ ] 验证服务可用性
- [ ] 监控上线

---

## 任务统计

| Phase | 周数 | 任务数 |
|-------|------|--------|
| Phase 1 | 2周 | 42 项 |
| Phase 2 | 3周 | 35 项 |
| Phase 3 | 4周 | 41 项 |
| Phase 4 | 3周 | 38 项 |
| Phase 5 | 2周 | 33 项 |
| **总计** | **14周** | **189 项** |

---

## 里程碑

| 里程碑 | 时间 | 交付物 |
|--------|------|--------|
| M1: 用户系统可用 | 第2周末 | 用户注册、登录、个人信息管理 |
| M2: 学习流程可用 | 第5周末 | 课程浏览、学习进度追踪 |
| M3: AI 对话可用 | 第9周末 | AI 老师对话、知识问答 |
| M4: 完整功能可用 | 第12周末 | 语音、数字人、代码执行 |
| M5: 正式上线 | 第14周末 | 系统稳定运行、监控完善 |

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-04-01 | 初始版本 |