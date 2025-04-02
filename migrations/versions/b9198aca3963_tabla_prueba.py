"""add tabla_prueba table

Revision ID: b9198aca3963
Revises: None
Create Date: 2025-04-02 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# Revisiones
revision = 'b9198aca3963'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'tabla_prueba',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(length=100), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, unique=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('tabla_prueba')