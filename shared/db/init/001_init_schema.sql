-- CodeBuddyAI 数据库初始化脚本
-- 创建时间: 2026-04-01

-- ============================================
-- 用户表
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nickname VARCHAR(100),
    avatar_url VARCHAR(500),
    birth_date DATE,
    grade INTEGER CHECK (grade >= 6 AND grade <= 9),
    learning_goal TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_created_at ON users(created_at);

COMMENT ON TABLE users IS '用户基础信息表';
COMMENT ON COLUMN users.grade IS '年级 (6-9 对应 12-14 岁)';

-- ============================================
-- 认证凭证表
-- ============================================
CREATE TABLE IF NOT EXISTS auth_credentials (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    refresh_token_hash VARCHAR(255) NOT NULL,
    device_info JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_revoked BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_auth_credentials_user_id ON auth_credentials(user_id);
CREATE INDEX idx_auth_credentials_expires_at ON auth_credentials(expires_at);
CREATE INDEX idx_auth_credentials_refresh_token ON auth_credentials(refresh_token_hash);

COMMENT ON TABLE auth_credentials IS 'Refresh Token 存储表';

-- ============================================
-- 家长关联表
-- ============================================
CREATE TABLE IF NOT EXISTS parent_links (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    child_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    parent_email VARCHAR(255) NOT NULL,
    parent_name VARCHAR(100),
    verification_code VARCHAR(10),
    is_verified BOOLEAN DEFAULT FALSE,
    report_frequency VARCHAR(20) DEFAULT 'weekly' CHECK (report_frequency IN ('daily', 'weekly', 'monthly')),
    report_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_parent_child UNIQUE (child_id, parent_email)
);

CREATE INDEX idx_parent_links_child_id ON parent_links(child_id);
CREATE INDEX idx_parent_links_parent_email ON parent_links(parent_email);
CREATE INDEX idx_parent_links_verification_code ON parent_links(verification_code);

COMMENT ON TABLE parent_links IS '家长关联表 - 支持学习进度报告推送';

-- ============================================
-- 触发器: 自动更新 updated_at
-- ============================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_parent_links_updated_at
    BEFORE UPDATE ON parent_links
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- 清理过期 Token 的函数
-- ============================================
CREATE OR REPLACE FUNCTION cleanup_expired_tokens()
RETURNS void AS $$
BEGIN
    DELETE FROM auth_credentials
    WHERE expires_at < CURRENT_TIMESTAMP OR is_revoked = TRUE;
END;
$$ LANGUAGE plpgsql;