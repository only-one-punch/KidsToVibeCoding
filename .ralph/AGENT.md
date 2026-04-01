# CodeBuddyAI - 技术信息与构建命令

## 项目结构
```
TESTGstack/
├── frontend/              # React 前端
├── services/
│   ├── gateway/           # API 网关 (FastAPI)
│   ├── user/              # 用户服务 (FastAPI)
│   ├── learning/          # 学习服务 (FastAPI)
│   ├── ai-assistant/      # AI 对话服务 (FastAPI)
│   ├── multimodal/        # 多模态服务 (FastAPI)
│   └── sandbox/           # 代码沙箱服务 (FastAPI)
├── shared/                # 公共库
├── docker-compose.yml
└── docs/
```

## 前端构建命令

```bash
# 安装依赖
cd frontend && npm install

# 开发服务器 (端口 3000)
cd frontend && npm run dev

# 构建
cd frontend && npm run build

# 类型检查 (lint)
cd frontend && npm run lint

# 预览构建结果
cd frontend && npm run preview
```

## 后端构建命令

```bash
# 安装依赖（各服务独立）
cd services/<service-name> && pip install -r requirements.txt
# 或
cd services/<service-name> && pip install -e .

# 启动开发服务器
cd services/<service-name> && uvicorn app.main:app --reload --port <port>

# 运行测试
cd services/<service-name> && pytest
cd services/<service-name> && pytest tests/ -v

# 代码格式化
black .
isort .

# 代码检查
flake8
```

## 服务端口分配

| 服务 | 端口 | 启动命令 |
|------|------|----------|
| Gateway | 8000 | `uvicorn app.main:app --reload --port 8000` |
| User Service | 8001 | `uvicorn app.main:app --reload --port 8001` |
| Learning Service | 8002 | `uvicorn app.main:app --reload --port 8002` |
| AI Assistant | 8003 | `uvicorn app.main:app --reload --port 8003` |
| Multimodal | 8004 | `uvicorn app.main:app --reload --port 8004` |
| Sandbox | 8005 | `uvicorn app.main:app --reload --port 8005` |
| Frontend | 3000 | `npm run dev` |

## Docker 命令

```bash
# 启动基础设施 (PostgreSQL + Redis)
docker-compose up -d

# 停止
docker-compose down

# 查看日志
docker-compose logs -f

# 重建
docker-compose up -d --build
```

## 数据库迁移

```bash
# 创建迁移
cd services/<service-name> && alembic revision --autogenerate -m "description"

# 执行迁移
cd services/<service-name> && alembic upgrade head

# 回滚
cd services/<service-name> && alembic downgrade -1
```

## Python 依赖（各服务通用）

```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
sqlalchemy[asyncio]>=2.0.0
asyncpg>=0.29.0
alembic>=1.12.0
redis>=5.0.0
pydantic>=2.5.0
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
python-multipart>=0.0.6
httpx>=0.25.0
```

## 前端依赖（已安装）

- React 19 + ReactDOM
- React Router DOM 7
- TailwindCSS 4
- Lucide React (图标)
- Motion (动画)
- clsx + tailwind-merge (样式工具)
- Vite 6 + TypeScript 5.8

## API 规范

- 所有 API 使用 `/api/v1/` 前缀
- 认证使用 JWT Bearer Token（Header: `Authorization: Bearer <token>`）
- 服务间调用使用 API Key（Header: `X-API-Key: <key>`）
- 响应格式统一：`{ "code": 0, "data": {}, "message": "success" }`
- 错误响应：`{ "code": <error_code>, "data": null, "message": "<error_detail>" }`
- 分页参数：`?page=1&page_size=20`
- 时间格式：ISO 8601（`2026-04-01T00:00:00Z`）

## 环境变量模板

```env
# 数据库
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/codebuddy
REDIS_URL=redis://localhost:6379/0

# JWT
JWT_SECRET=your-secret-key
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# AI
ANTHROPIC_API_KEY=your-api-key
PINECONE_API_KEY=your-api-key
PINECONE_ENVIRONMENT=your-env

# 讯飞
XFYUN_APP_ID=your-app-id
XFYUN_API_KEY=your-api-key
XFYUN_API_SECRET=your-api-secret

# 服务间认证
SERVICE_API_KEY=your-service-api-key
```


## 命令执行约束
- 仅运行与当前任务直接相关的最小必要命令
- 不要主动安装依赖，除非被依赖缺失阻塞
- 不要默认执行高成本命令，如全量 build、docker rebuild、全项目测试
- 命令失败时，记录失败原因，不得声称验证通过
