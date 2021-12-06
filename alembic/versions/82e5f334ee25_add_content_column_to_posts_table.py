"""add content column to posts table

Revision ID: 82e5f334ee25
Revises: 3ab6d672e0dd
Create Date: 2021-12-04 12:31:34.586959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '82e5f334ee25'
down_revision = '3ab6d672e0dd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
