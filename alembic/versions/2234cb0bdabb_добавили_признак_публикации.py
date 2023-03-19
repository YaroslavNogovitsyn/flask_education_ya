"""добавили признак публикации

Revision ID: 2234cb0bdabb
Revises: 
Create Date: 2023-03-19 22:18:22.882320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2234cb0bdabb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('is_published', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'is_published')
    # ### end Alembic commands ###
