"""Create caracateristicas table

Revision ID: da38c8e24a21
Revises: 67faedcccc5f
Create Date: 2025-04-06 21:29:11.190950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da38c8e24a21'
down_revision = '67faedcccc5f'
branch_labels = None
depends_on = None


def upgrade():
    # Create the modelos table
    op.create_table(
        'caracateristicas',
        sa.Column('id_Caracteristica', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('id_Modelo', sa.Integer(), nullable=False),
        sa.Column('Descripcion', sa.Text, nullable=False),
        sa.Column('Referencia', sa.VARCHAR(255), nullable=False),
        sa.ForeignKeyConstraint(['id_Modelo'], ['modelos.id_Modelo'], name='fk_modelo_caracteristica')  # Foreign key
    )


def downgrade():
    # Drop the modelos table
    op.drop_table('caracateristicas')

