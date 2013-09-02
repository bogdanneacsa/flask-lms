"""Initial database migration.

Revision ID: 57a880d09a40
Revises: None
Create Date: 2013-08-29 09:46:44.155941

"""

# revision identifiers, used by Alembic.
revision = '57a880d09a40'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=120), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    

def downgrade():
    op.drop_table('roles')
    op.drop_table('users')
