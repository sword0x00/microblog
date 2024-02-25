"""new fields in user model

Revision ID: 7db5ef070efa
Revises: 4ec47e478eb3
Create Date: 2024-02-18 15:18:07.975751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7db5ef070efa'
down_revision = '4ec47e478eb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
