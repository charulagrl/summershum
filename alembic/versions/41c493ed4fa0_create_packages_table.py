"""create package table

Revision ID: 982e21d5349
Revises: 
Create Date: 2015-03-15 19:39:58.923655

"""

# revision identifiers, used by Alembic.
revision = '982e21d5349'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'packages',
        sa.Column('pkg_name', sa.Text, primary_key=True)
    )


def downgrade():
    op.drop_table('packages')
