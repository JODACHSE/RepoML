"""Regresión logística para transporte de paquetes con dataset aleatorio y evaluación de métricas"""
import io
import base64
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as mcm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# Diccionarios para mapear variables categóricas (se mantienen igual)
clima_map = {
    "soleado": 0,
    "lluvioso": 1,
    "nublado": 2,
    "tormenta": 3
}

trafico_map = {
    "bajo": 0,
    "medio": 1,
    "alto": 2
}

def plot_confusion_matrix(cm):
    """
    Genera un gráfico de la matriz de confusión y lo retorna como un string en formato base64.
    """
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=mcm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set_xticks(np.arange(cm.shape[1]))
    ax.set_yticks(np.arange(cm.shape[0]))
    ax.set_xlabel("Etiqueta Predicha")
    ax.set_ylabel("Etiqueta Real")

    # Añadir los valores en cada celda
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    fig.tight_layout()

    # Convertir el gráfico a un string en base64
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf8")
    plt.close(fig)
    return img_base64

def generate_dataset(num_samples=100):
    """
    Genera un dataset aleatorio para la predicción.
    - Distancia: valores en el rango [10, 70] km.
    - Peso: valores en el rango [5, 40] kg.
    - Clima: 4 categorías (0 a 3).
    - Tráfico: 3 categorías (0 a 2).
    
    La regla de etiquetado es un ejemplo:
      Si la distancia es menor a 40 km y el peso es menor a 20 kg se asume que el paquete se puede transportar (1),
      de lo contrario (0). Puedes modificar esta regla o agregarle ruido para mayor aleatoriedad.
    """
    # Generar las características aleatorias
    distances = np.random.uniform(10, 70, num_samples)
    peso   = np.random.uniform(5, 40, num_samples)
    # Clima: enteros de 0 a 3
    climas    = np.random.randint(0, 4, num_samples)
    # Tráfico: enteros de 0 a 2
    traficos  = np.random.randint(0, 3, num_samples)
    # Combinar las características en un arreglo (dataset)
    x = np.column_stack((distances, peso, climas, traficos))
    # Generar las etiquetas usando una regla simple
    y = []
    for d, p, c, t in x:
        # Regla de ejemplo: transportable si la distancia es menor a 40 km y el peso menor a 20 kg
        # Puedes agregar condiciones adicionales según clima o tráfico si lo deseas.
        if d < 40 and p < 20:
            y.append(1)
        else:
            y.append(0)
    y = np.array(y)
    return x, y

def predict_transport(distancia, peso, clima, trafico):
    """
    Predice si el paquete se podrá transportar en función de distancia, peso, clima y tráfico.
    Además, retorna un diccionario con las métricas de evaluación (accuracy, precision, recall, 
    matriz de confusión numérica y la imagen de la matriz de confusión en base64).
    """
    # Generar el dataset aleatorio
    x, y = generate_dataset(num_samples=100)
    
    # Dividir el dataset: 70% para entrenamiento y 30% para prueba (sin random_state para variabilidad)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    
    # Crear y ajustar el modelo utilizando los datos de entrenamiento
    model = LogisticRegression(max_iter=200)
    model.fit(x_train, y_train)
    
    # Predicciones en el conjunto de prueba para evaluar el modelo
    y_pred = model.predict(x_test)
    
    # Calcular métricas clave
    accuracy  = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall    = recall_score(y_test, y_pred)
    cm        = confusion_matrix(y_test, y_pred)
    
    # Generar la imagen de la matriz de confusión
    cm_image = plot_confusion_matrix(cm)
    
    # Codificar las variables categóricas de la entrada nueva
    clima_code  = clima_map.get(clima.lower(), 0)
    trafico_code = trafico_map.get(trafico.lower(), 0)
    x_new = np.array([[distancia, peso, clima_code, trafico_code]])
    
    # Realizar la predicción con la nueva muestra
    prediction = int(model.predict(x_new)[0])
    
    # Retornar la predicción y las métricas en un diccionario
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        # Convertimos la matriz a lista para que Jinja la pueda procesar
        'conf_matrix': cm.tolist(),
        # Incluir la imagen en base64
        'cm_image': cm_image
    }
    return prediction, metrics

# Ejemplo de uso:
if __name__ == "__main__":
    # Valores de ejemplo para la nueva muestra
    pred, metrics = predict_transport(30, 10, "soleado", "medio")
    print("Predicción:", pred)
    print("Métricas:", metrics)
