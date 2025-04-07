"""Create modelos seeder

Revision ID: bcd75a442c42
Revises: e15f47f76549
Create Date: 2025-04-07 00:07:10.886670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd75a442c42'
down_revision = 'e15f47f76549'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        sa.table(
            'modelos',
            sa.column('id_Modelo', sa.Integer),
            sa.column('Nombre_Modelo', sa.String(255))
        ),
        [
            {'id_Modelo': 1, 'Nombre_Modelo': 'Regresión Logística'},
            {'id_Modelo': 2, 'Nombre_Modelo': 'K-Nearest Neighbors (KNN)'},
            {'id_Modelo': 3, 'Nombre_Modelo': 'Árboles de Decisión'},
            {'id_Modelo': 4, 'Nombre_Modelo': 'Random Forest'},
            {'id_Modelo': 5, 'Nombre_Modelo': 'Support Vector Machine (SVM)'},
            {'id_Modelo': 6, 'Nombre_Modelo': 'Gradient Boosting'},
            {'id_Modelo': 7, 'Nombre_Modelo': 'Naive Bayes'}
        ]
    )


def downgrade():
    op.execute("DELETE FROM modelos WHERE id_Modelo BETWEEN 1 AND 7")
