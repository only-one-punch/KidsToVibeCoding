"""initial schema

Revision ID: 001
Revises: 
Create Date: 2026-04-01

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 启用 UUID 扩展
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    
    # 用户表
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), primary_key=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('nickname', sa.String(100)),
        sa.Column('avatar_url', sa.String(500)),
        sa.Column('age', sa.Integer),
        sa.Column('role', sa.String(20), nullable=False, server_default='student'),
        sa.Column('status', sa.String(20), nullable=False, server_default='active'),
        sa.Column('learning_preferences', postgresql.JSONB, server_default='{}'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.CheckConstraint('age >= 12 AND age <= 14', name='check_age_range'),
        sa.CheckConstraint("role IN ('student', 'parent', 'admin')", name='check_role'),
        sa.CheckConstraint("status IN ('active', 'inactive', 'suspended')", name='check_status'),
    )
    
    # 认证凭据表
    op.create_table(
        'auth_credentials',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('device_id', sa.String(255)),
        sa.Column('refresh_token_hash', sa.String(255), nullable=False),
        sa.Column('token_expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('ip_address', sa.String(45)),
        sa.Column('user_agent', sa.String(500)),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('is_revoked', sa.Boolean, server_default='false'),
    )
    
    # 家长关联表
    op.create_table(
        'parent_links',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), primary_key=True),
        sa.Column('child_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('parent_email', sa.String(255), nullable=False),
        sa.Column('parent_user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL')),
        sa.Column('status', sa.String(20), nullable=False, server_default='pending'),
        sa.Column('verification_code', sa.String(6)),
        sa.Column('verification_expires_at', sa.DateTime(timezone=True)),
        sa.Column('report_frequency', sa.String(20), server_default='weekly'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.CheckConstraint("status IN ('pending', 'confirmed', 'rejected')", name='check_link_status'),
        sa.CheckConstraint("report_frequency IN ('daily', 'weekly', 'monthly')", name='check_report_frequency'),
        sa.UniqueConstraint('child_id', 'parent_email', name='uq_child_parent'),
    )
    
    # 创建索引
    op.create_index('idx_users_email', 'users', ['email'])
    op.create_index('idx_users_username', 'users', ['username'])
    op.create_index('idx_auth_credentials_user_id', 'auth_credentials', ['user_id'])
    op.create_index('idx_auth_credentials_refresh_token', 'auth_credentials', ['refresh_token_hash'])
    op.create_index('idx_parent_links_child_id', 'parent_links', ['child_id'])
    op.create_index('idx_parent_links_parent_email', 'parent_links', ['parent_email'])


def downgrade() -> None:
    op.drop_index('idx_parent_links_parent_email', table_name='parent_links')
    op.drop_index('idx_parent_links_child_id', table_name='parent_links')
    op.drop_index('idx_auth_credentials_refresh_token', table_name='auth_credentials')
    op.drop_index('idx_auth_credentials_user_id', table_name='auth_credentials')
    op.drop_index('idx_users_username', table_name='users')
    op.drop_index('idx_users_email', table_name='users')
    op.drop_table('parent_links')
    op.drop_table('auth_credentials')
    op.drop_table('users')
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp"')
