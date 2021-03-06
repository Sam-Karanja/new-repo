"""update post table

Revision ID: 33f39b299295
Revises: a36adb15003e
Create Date: 2022-03-12 17:57:41.804242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33f39b299295'
down_revision = 'a36adb15003e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.drop_column('users', 'profile_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
