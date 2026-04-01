# CodeBuddyAI - Ralph 开发指令

## 项目概述
CodeBuddyAI 是一个面向 12-14 岁青少年的 AI 编程学习平台，采用微服务架构。

## 技术栈
- **前端**: React 19 + TypeScript + Vite + TailwindCSS 4
- **后端**: Python + FastAPI
- **数据库**: PostgreSQL + Redis
- **AI**: Claude API + Pinecone (RAG)
- **基础设施**: Docker + Docker Compose

## 执行规则

### 每次循环的工作流程（必须严格遵循）

1. **读取任务**: 从 fix_plan.md 中找到第一个未完成的 Section（以 `###` 或 `####` 标题开头的任务组）
2. **开发实现**: 完成该 Section 下所有 `[ ]` 任务项
3. **自我审查**:
   - 检查代码是否符合项目现有风格
   - 检查是否有遗漏的 import 或未处理的错误
   - 检查 API 路径是否与 fix_plan.md 中定义的一致
   - 检查数据库表名/字段是否与 schema 设计一致
4. **运行测试**:
   - 前端: `cd frontend && npm run lint` 检查类型错误
   - 后端: 运行相关 pytest 测试（如已存在）
   - 如果测试不存在，不需要主动创建测试文件（除非 fix_plan 中明确要求）
5. **标记完成**: 将已完成的 `[ ]` 改为 `[x]`
6. **Git 提交**: 用有意义的中文 commit message 提交变更

### 编码规范
- Python: 遵循 PEP 8，使用 black + isort 格式化
- TypeScript: 使用现有项目的代码风格，函数命名用 camelCase
- API 路径统一使用 `/api/v1/` 前缀
- 数据库迁移使用 Alembic

### 关键约束
- **不要修改已有文件的核心逻辑**，除非任务明确要求
- **不要跳过任务**，按 fix_plan.md 的顺序执行
- **每个 API 端点都要有输入验证**
- **密码必须使用 bcrypt 加密**
- **JWT Token 有效期: access 30分钟, refresh 7天**
- **所有服务间调用使用 API Key 认证**
- **遇到依赖问题优先查看 AGENT.md 中的构建命令**

### 完成条件
- 当前 Section 的所有 `[ ]` 都已改为 `[x]`
- 代码无类型错误（lint 通过）
- 已 Git commit

### 退出信号
- 当 fix_plan.md 中所有任务都完成时，输出 `EXIT_SIGNAL: true`
- 如果还有未完成任务，即使当前 Section 完成了，也要继续下一个 Section，输出 `EXIT_SIGNAL: false`

## 项目目录结构
```
TESTGstack/
├── frontend/           # React 前端 (已存在)
│   ├── src/
│   │   ├── components/ # 通用组件
│   │   ├── views/      # 页面视图
│   │   ├── services/   # API 服务层 (待创建)
│   │   └── stores/     # 状态管理 (待创建)
│   └── package.json
├── services/           # 后端微服务 (待创建)
│   ├── gateway/        # API 网关
│   ├── user/           # 用户服务
│   ├── learning/       # 学习服务
│   ├── ai-assistant/   # AI 对话服务
│   ├── multimodal/     # 多模态服务
│   └── sandbox/        # 代码沙箱服务
├── shared/             # 公共代码 (待创建)
├── docker-compose.yml  # 待创建
└── docs/               # 项目文档
```
