"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2026-04-01

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 启用 UUID 扩展
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    # 创建 users 表
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('username', sa.String(50), unique=True, nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('nickname', sa.String(100)),
        sa.Column('avatar_url', sa.String(500)),
        sa.Column('age', sa.Integer),
        sa.Column('role', sa.String(20), server_default='student'),
        sa.Column('learning_preferences', sa.JSON(), server_default='{}'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
    )
    op.create_index('idx_users_email', 'users', ['email'])
    op.create_index('idx_users_username', 'users', ['username'])

    # 创建 auth_credentials 表
    op.create_table(
        'auth_credentials',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('access_token_hash', sa.String(255)),
        sa.Column('refresh_token_hash', sa.String(255)),
        sa.Column('token_expires_at', sa.DateTime(timezone=True)),
        sa.Column('last_login_at', sa.DateTime(timezone=True)),
        sa.Column('login_count', sa.Integer(), server_default='0'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
    )
    op.create_index('idx_auth_credentials_user_id', 'auth_credentials', ['user_id'])

    # 创建 parent_links 表
    op.create_table(
        'parent_links',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('student_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('parent_email', sa.String(255), nullable=False),
        sa.Column('parent_name', sa.String(100)),
        sa.Column('is_verified', sa.Boolean(), server_default='false'),
        sa.Column('verification_token', sa.String(255)),
        sa.Column('report_frequency', sa.String(20), server_default='weekly'),
        sa.Column('last_report_at', sa.DateTime(timezone=True)),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
    )
    op.create_index('idx_parent_links_student_id', 'parent_links', ['student_id'])
    op.create_index('idx_parent_links_parent_email', 'parent_links', ['parent_email'])
    op.create_unique_constraint('uq_parent_links_student_email', 'parent_links', ['student_id', 'parent_email'])


def downgrade():
    op.drop_table('parent_links')
    op.drop_table('auth_credentials')
    op.drop_table('users')
