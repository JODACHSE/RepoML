"""Create caracteristicas seeder

Revision ID: c8763bf8eabe
Revises: bcd75a442c42
Create Date: 2025-04-07 00:13:25.399086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8763bf8eabe'
down_revision = 'bcd75a442c42'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        sa.table(
            'caracateristicas',
            sa.column('id_Caracteristica', sa.Integer),
            sa.column('id_Modelo', sa.Integer),
            sa.column('Descripcion', sa.Text),
            sa.column('Referencia', sa.String(255))
        ),
        [
            {
                'id_Caracteristica': 1,
                'id_Modelo': 1,
                'Descripcion': 'Descripción: La regresión logística es un modelo estadístico utilizado para predecir la probabilidad de que una observación pertenezca a una clase particular. Es especialmente útil para problemas de clasificación binaria. Características:\r\n\r\n- Función Sigmoide: Transforma la salida lineal en una probabilidad entre 0 y 1.\r\n\r\n- Coeficientes: Los coeficientes indican la dirección y magnitud de la relación entre las variables independientes y la probabilidad de pertenecer a una clase.\r\n\r\n- Umbral: Clasifica las observaciones basándose en un umbral predefinido (por ejemplo, 0.5).',
                'Referencia': '¿Qué es la regresión logística? (2024, mayo 7). Ibm.com. https://www.ibm.com/es-es/topics/logistic-regression\r\n\r\nRodríguez, D. (2018, julio 23). La regresión logística. Analytics Lane. https://www.analyticslane.com/2018/07/23/la-regresion-logistica/\r\n\r\n'
            },
            {
                'id_Caracteristica': 2,
                'id_Modelo': 2,
                'Descripcion': 'Descripción: KNN es un algoritmo de aprendizaje supervisado que clasifica las observaciones basándose en la proximidad a sus vecinos más cercanos. Características:\r\n\r\n- No Paramétrico: No hace suposiciones sobre la distribución de los datos.\r\n\r\n- Distancia Euclidiana: Utiliza la distancia euclidiana para medir la similitud entre puntos de datos.\r\n\r\n- Votación por Mayoría: Clasifica una observación basándose en la mayoría de votos de sus vecinos más cercanos.',
                'Referencia': '¿Qué es k vecino más cercano (kNN)? (s/f). Elastic.co. Recuperado el 7 de abril de 2025, de https://www.elastic.co/es/what-is/knn\r\n\r\n¿Qué es el algoritmo de k vecinos más próximos? (2024, octubre 10). Ibm.com. https://www.ibm.com/es-es/topics/knn\r\n\r\n'
            },
            {
                'id_Caracteristica': 3,
                'id_Modelo': 3,
                'Descripcion': 'Descripción: Los árboles de decisión son modelos de clasificación y regresión que utilizan una estructura de árbol para tomar decisiones basadas en reglas. Características:\r\n\r\n- Nodos y Hojas: Los nodos representan decisiones y las hojas representan resultados.\r\n\r\n- División de Datos: Divide los datos en subconjuntos basándose en las características más importantes.\r\n\r\n- Visualización: Fácil de interpretar y visualizar.',
                'Referencia': 'Ortega, C. (2024, abril 16). Árbol de decisión: Qué es, tipos, ventajas y ejemplo. QuestionPro. https://www.questionpro.com/blog/es/arbol-de-decision/\r\n\r\ntiyeii. (2024, marzo 13). Árbol de Decisiones: Beneficios, Características y Ejemplos. tiyeii. https:'
            },
            {
                'id_Caracteristica': 4,
                'id_Modelo': 4,
                'Descripcion': 'Descripción: Random Forest es un conjunto de árboles de decisión que mejora la precisión mediante la combinación de múltiples árboles. Características:\r\n\r\n- Bagging: Utiliza el método de bagging para crear múltiples árboles de decisión.\r\n\r\n- Promedio: Promedia las predicciones de los árboles individuales para obtener una predicción final.\r\n\r\n- Robustez: Es robusto frente al sobreajuste y puede manejar grandes conjuntos de datos.',
                'Referencia': '¿Qué es Random Forest? (2025, febrero 27). Ibm.com. https://www.ibm.com/mx-es/think/topics/random-forest\r\n\r\nWikipedia contributors. (s/f). Random forest. Wikipedia, The Free Encyclopedia. https://es.wikipedia.org/w/index.php?title=Random_forest&oldid=1603'
            },
            {
                'id_Caracteristica': 5,
                'id_Modelo': 5,
                'Descripcion': 'Descripción: SVM es un algoritmo de aprendizaje supervisado que clasifica los datos al encontrar el hiperplano óptimo que maximiza la distancia entre clases. Características:\r\n\r\n- Hiperplano: Encuentra el hiperplano que mejor separa las clases.\r\n\r\n- Vectores de Soporte: Utiliza vectores de soporte para definir el margen máximo.\r\n\r\n- Kernels: Puede utilizar diferentes funciones de kernel para manejar datos no linealmente separables.',
                'Referencia': 'Boyd, A. (s/f). Cuándo utilizar máquinas de vectores soporte (SVM): Una guía completa. Shallbd.com. Recuperado el 7 de abril de 2025, de https://shallbd.com/es/cuando-utilizar-maquinas-de-vectores-soporte-svm-una-guia-completa/\r\n\r\n¿Qué es Support Vector M'
            },
            {
                'id_Caracteristica': 6,
                'id_Modelo': 6,
                'Descripcion': 'Descripción: Gradient Boosting es una técnica de conjunto que crea modelos fuertes mediante la combinación de múltiples modelos débiles, optimizando una función de pérdida. Características:\r\n\r\n- Secuencial: Construye modelos secuencialmente, cada uno corrigiendo los errores del anterior.\r\n\r\n- Flexibilidad: Puede utilizar diferentes funciones de pérdida y modelos base.\r\n\r\n- Regularización: Incluye técnicas de regularización para prevenir el sobreajuste.',
                'Referencia': 'mljourney. (2025, abril 6). Is AdaBoost better than Gradient Boosting? ML Journey. https://mljourney.com/is-adaboost-better-than-gradient-boosting/\r\n\r\nXGBoost vs AdaBoost. (s/f). Xgboosting.com. Recuperado el 7 de abril de 2025, de https://xgboosting.com/'
            },
            {
                'id_Caracteristica': 7,
                'id_Modelo': 7,
                'Descripcion': 'Descripción: Naive Bayes es un clasificador probabilístico basado en el teorema de Bayes, que asume la independencia entre las características. Características:\r\n\r\n- Probabilidad Condicional: Calcula la probabilidad de que una observación pertenezca a una clase dada.\r\n\r\n- Independencia: Asume que las características son independientes entre sí.\r\n\r\n- Eficiencia: Es eficiente y funciona bien con grandes conjuntos de datos.',
                'Referencia': 'Alonso, J. C., & Hoyos, C. C. (2025, marzo 4). 5 Clasificador bayesiano ingenuo (Naive Bayes). Edu.co. https://www.icesi.edu.co/editorial/intro-clasificacion-web/Naive.html\r\n\r\n¿Qué son los clasificadores Naive Bayes? (2025, enero 29). Ibm.com. https://www'
            }
        ]
    )


def downgrade():
    op.execute("DELETE FROM caracateristicas WHERE id_Caracteristica BETWEEN 1 AND 7")
