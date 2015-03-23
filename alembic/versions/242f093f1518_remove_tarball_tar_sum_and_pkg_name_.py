"""Remove tarball, tar_sum and pkg_name from files table

Revision ID: 242f093f1518
Revises: 54a8edb25b5d
Create Date: 2015-03-23 05:19:51.133950

"""

# revision identifiers, used by Alembic.
revision = '242f093f1518'
down_revision = '54a8edb25b5d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("files") as batch_op:
        batch_op.drop_column('tarball'),
        batch_op.drop_column('tar_sum'),
        batch_op.drop_column('pkg_name')

def downgrade():
    with op.batch_alter_table("files") as batch_op:
        batch_op.add_column(sa.Column('tarball', sa.Text, nullable=False, server_default=''))
        batch_op.add_column(sa.Column('tar_sum', sa.String(64), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('pkg_name', sa.Text, nullable=False, server_default=''))
        batch_op.create_index('ix_files_tar_sum', ['tar_sum'])
        batch_op.create_index('ix_files_pkg_name', ['pkg_name'])
        batch_op.create_unique_constraint('uq_files_tar_sum_filename_key', ['tar_sum', 'filename'])
