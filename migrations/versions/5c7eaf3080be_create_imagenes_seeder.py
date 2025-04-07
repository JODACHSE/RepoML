"""Create imagenes seeder

Revision ID: 5c7eaf3080be
Revises: c8763bf8eabe
Create Date: 2025-04-07 00:13:38.163201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c7eaf3080be'
down_revision = 'c8763bf8eabe'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        sa.table(
            'imagenes',
            sa.column('id_Imagen', sa.Integer),
            sa.column('id_Modelo', sa.Integer),
            sa.column('link_Imagen', sa.String(255))
        ),
        [
            {'id_Imagen': 1, 'id_Modelo': 1, 'link_Imagen': 'Regresion Logistica.png'},
            {'id_Imagen': 2, 'id_Modelo': 2, 'link_Imagen': 'K Nearest Neighbors.png'},
            {'id_Imagen': 3, 'id_Modelo': 3, 'link_Imagen': 'Árboles de Decisión.png'},
            {'id_Imagen': 4, 'id_Modelo': 4, 'link_Imagen': 'ramdom forest.png'},
            {'id_Imagen': 5, 'id_Modelo': 5, 'link_Imagen': 'Support Vector Machine.png'},
            {'id_Imagen': 6, 'id_Modelo': 6, 'link_Imagen': 'Gradient Boosting.png'},
            {'id_Imagen': 7, 'id_Modelo': 7, 'link_Imagen': 'Naive Bayes.png'}
        ]
    )


def downgrade():
    op.execute("DELETE FROM imagenes WHERE id_Imagen BETWEEN 1 AND 7")
