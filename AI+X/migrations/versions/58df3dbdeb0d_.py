"""empty message

Revision ID: 58df3dbdeb0d
Revises: 415aba235ab2
Create Date: 2023-04-28 21:49:17.633808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58df3dbdeb0d'
down_revision = '415aba235ab2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questionnaire_answer', schema=None) as batch_op:
        batch_op.drop_constraint('questionnaire_answer_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'questionnaire_question', ['question_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('questionnaire_option', schema=None) as batch_op:
        batch_op.drop_constraint('questionnaire_option_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'questionnaire_question', ['question_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questionnaire_option', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('questionnaire_option_ibfk_1', 'questionnaire_question', ['question_id'], ['id'])

    with op.batch_alter_table('questionnaire_answer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('questionnaire_answer_ibfk_2', 'questionnaire_question', ['question_id'], ['id'])

    # ### end Alembic commands ###
