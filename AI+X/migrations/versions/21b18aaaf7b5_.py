"""empty message

Revision ID: 21b18aaaf7b5
Revises: 811d8166b492
Create Date: 2023-04-28 20:50:55.041304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21b18aaaf7b5'
down_revision = '811d8166b492'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['title'])
        batch_op.create_unique_constraint(None, ['file'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
