"""foreignKeys

Revision ID: 75ed499f8d6b
Revises: 4f5d48f6d868
Create Date: 2023-11-20 21:47:51.305442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ed499f8d6b'
down_revision = '4f5d48f6d868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('signups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('camper_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('activity_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_signups_activity_id_activities'), 'activities', ['activity_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_signups_camper_id_campers'), 'campers', ['camper_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('signups', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_signups_camper_id_campers'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_signups_activity_id_activities'), type_='foreignkey')
        batch_op.drop_column('activity_id')
        batch_op.drop_column('camper_id')

    # ### end Alembic commands ###
