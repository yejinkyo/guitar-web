"""empty message

Revision ID: f8f878079e3d
Revises: 6e466b42729b
Create Date: 2024-12-04 22:41:48.251170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8f878079e3d'
down_revision = '6e466b42729b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=sa.DATETIME(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=sa.Integer(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
