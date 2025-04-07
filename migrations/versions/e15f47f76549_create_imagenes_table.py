"""Create imagenes table

Revision ID: e15f47f76549
Revises: da38c8e24a21
Create Date: 2025-04-06 21:29:45.560415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e15f47f76549'
down_revision = 'da38c8e24a21'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'imagenes',
        sa.Column('id_Imagen', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('id_Modelo', sa.Integer(), nullable=False),
        sa.Column('link_Imagen', sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(['id_Modelo'], ['modelos.id_Modelo'], name='fk_modelo_imagenes')
    )

def downgrade():
    # Drop the imagenes table
    op.drop_table('imagenes')
