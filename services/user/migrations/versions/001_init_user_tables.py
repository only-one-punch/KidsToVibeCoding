"""init user tables

Revision ID: 001
Revises:
Create Date: 2026-04-01

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 创建 users 表
    op.execute("""
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
    """)

    op.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_users_created_at ON users(created_at);")

    # 创建 auth_credentials 表
    op.execute("""
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
    """)

    op.execute("CREATE INDEX IF NOT EXISTS idx_auth_credentials_user_id ON auth_credentials(user_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_auth_credentials_expires_at ON auth_credentials(expires_at);")

    # 创建 parent_links 表
    op.execute("""
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
    """)

    op.execute("CREATE INDEX IF NOT EXISTS idx_parent_links_child_id ON parent_links(child_id);")
    op.execute("CREATE INDEX IF NOT EXISTS idx_parent_links_parent_email ON parent_links(parent_email);")

    # 创建更新时间触发器
    op.execute("""
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    """)

    op.execute("""
        CREATE TRIGGER update_users_updated_at
            BEFORE UPDATE ON users
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
    """)

    op.execute("""
        CREATE TRIGGER update_parent_links_updated_at
            BEFORE UPDATE ON parent_links
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
    """)


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS update_parent_links_updated_at ON parent_links;")
    op.execute("DROP TRIGGER IF EXISTS update_users_updated_at ON users;")
    op.execute("DROP FUNCTION IF EXISTS update_updated_at_column();")
    op.execute("DROP TABLE IF EXISTS parent_links;")
    op.execute("DROP TABLE IF EXISTS auth_credentials;")
    op.execute("DROP TABLE IF EXISTS users;")