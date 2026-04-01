"""初始数据库迁移

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
    # 此迁移由 init.sql 处理
    # Alembic 用于后续增量迁移
    pass

def downgrade() -> None:
    pass
