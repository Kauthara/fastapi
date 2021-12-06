"""add last few columns to posts table

Revision ID: 14c8d02f1224
Revises: 2ffb9359c2b9
Create Date: 2021-12-04 13:29:49.055669

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false


# revision identifiers, used by Alembic.
revision = '14c8d02f1224'
down_revision = '2ffb9359c2b9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
