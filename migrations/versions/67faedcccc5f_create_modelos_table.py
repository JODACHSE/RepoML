"""Create Modelos table

Revision ID: 67faedcccc5f
Revises: 
Create Date: 2025-04-06 21:28:30.716396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67faedcccc5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the modelos table
    op.create_table(
        'modelos',
        sa.Column('id_Modelo', sa.Integer(), primary_key=True , autoincrement=True),
        sa.Column('Nombre_Modelo', sa.String(255), nullable=False),
    )

def downgrade():
    # Drop the modelos table
    op.drop_table('modelos')
