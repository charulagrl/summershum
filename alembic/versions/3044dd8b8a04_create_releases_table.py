"""Create releases table

Revision ID: 54a8edb25b5d
Revises: 982e21d5349
Create Date: 2015-03-16 22:55:52.267179

"""

# revision identifiers, used by Alembic.
revision = '54a8edb25b5d'
down_revision = '982e21d5349'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'releases',
        sa.Column('tarball', sa.Text, primary_key=True),
        sa.Column('tar_sum', sa.String(64), primary_key=True),
        sa.Column('pkg_name', sa.Text, nullable=False, index=True),
        sa.ForeignKeyConstraint(["pkg_name"], ["packages.pkg_name"],
        onupdate='CASCADE',)
    )
    op.create_unique_constraint('uq_releases_tarball_tarsum', 'releases', ['tarball', 'tar_sum'])




def downgrade():
    op.drop_constraint('uq_releases_tarball_tarsum', 'releases','unique')
    op.drop_table("releases")
