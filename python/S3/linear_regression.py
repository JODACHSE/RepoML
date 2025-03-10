""" Machine learning - Linear Regression"""
import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
data = {
    "Study Hours": [10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1],
    "Final Grade": [3.8, 4.2, 3.6, 3.0, 4.5, 2.5, 4.8, 2.8, 3.7, 4.0, 3.2, 2.2, 5.0, 1.8, 4.9, 2.7, 4.4, 1.5, 5.0, 1.0]
}

df = pd.DataFrame(data)

# Definir variables independientes y dependientes
x = df[["Study Hours"]]
y = df["Final Grade"]

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(x, y)


def calculate_grade(hours):
    """
    Calcular la calificación de un estudiante basada en sus horas de estudio.
    """
    result = model.predict([[hours]])
    return result[0]


def generate_graph(user_hours):
    """
    Generar un gráfico de dispersión con la línea de regresión y el punto del usuario.
    """
    # Crear el gráfico de dispersión
    plt.figure(figsize=(14, 10))
    plt.scatter(x, y, color='blue', label='Datos reales')

    # Dibujar la línea de regresión
    plt.plot(x, model.predict(x), color='red',
             linewidth=2, label='Línea de regresión')

    # Dibujar el punto del usuario
    user_grade = calculate_grade(user_hours)
    plt.scatter([user_hours], [user_grade], color='green',
                s=150, zorder=5, label='Tu predicción')

    # Añadir etiquetas y título
    plt.xlabel('Horas de estudio', fontsize=14)
    plt.ylabel('Calificación final', fontsize=14)
    plt.title(
        'Regresión Lineal: Horas de Estudio vs. Calificación Final', fontsize=16)
    plt.legend(fontsize=12)

    # Guardar el gráfico en un objeto BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()

    # Codificar la imagen en base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf8')
    return image_base64
