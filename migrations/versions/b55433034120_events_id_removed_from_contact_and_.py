"""events id removed from contact and foreign key added to events

Revision ID: b55433034120
Revises: 217c2420f97f
Create Date: 2018-04-25 09:41:48.587117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b55433034120'
down_revision = '217c2420f97f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('contacts_events_id_fkey', 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'events_id')
    op.add_column('events', sa.Column('contacts_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'contacts', ['contacts_id'], ['id'])
    op.drop_column('events', 'who')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('who', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'contacts_id')
    op.add_column('contacts', sa.Column('events_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('contacts_events_id_fkey', 'contacts', 'events', ['events_id'], ['id'])
    # ### end Alembic commands ###
