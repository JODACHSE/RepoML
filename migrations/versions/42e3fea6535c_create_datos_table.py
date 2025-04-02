"""Create datos Table

Revision ID: 42e3fea6535c
Revises: b9198aca3963
Create Date: 2025-04-02 01:46:59.704179

"""
from alembic import op
import sqlalchemy as sa



revision = '42e3fea6535c'
down_revision = 'b9198aca3963'
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_table('datos',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('Caracteristica1', sa.Float(), nullable=False),
        sa.Column('Caracteristica2', sa.Float(), nullable=True),
        sa.Column('Resultado', sa.VARCHAR(50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    


def downgrade():
    op.drop_table('datos')
