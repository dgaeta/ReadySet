"""create user table

Revision ID: c1fb11c98b17
Revises: 
Create Date: 2016-01-06 10:53:06.678967

"""

# revision identifiers, used by Alembic.
revision = 'c1fb11c98b17'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
			'user',
			sa.Column('username', sa.String(50), primary_key=True),
			sa.Column('first_name',sa.String(50)),
			sa.Column('last_name',sa.String(50)),
		)


def downgrade():
    op.drop_table('user')
