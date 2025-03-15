""" Machine learning - Linear Regression"""
import io
import base64
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg') # Para evitar que pylot se vaya en hilos secundarios
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
# Datos de ejemplo
data = {
    "Altura (cm)": [
        20.99835447, 92.8829578, 84.87123942, 47.387838, 66.62399205, 28.42168899, 78.67470081, 62.05629602, 
        47.44495645, 87.67539134, 96.58229446, 22.69031714, 82.06831727, 90.2958879, 91.15893024, 60.1232885, 
        40.8017561, 74.73331446, 15.9471511, 69.29043949, 55.14557335, 85.69927554, 13.62396556, 13.86716528, 
        54.56357499, 98.6665377, 98.25767273, 88.19933132, 13.31596371, 64.57865679, 52.73275254, 70.39394933, 
        71.60523166, 95.59786342, 53.95997255, 50.18842884, 31.75482327, 99.17517815, 30.99954075, 16.29403141, 
        93.62323701, 36.1520996, 45.81173743, 43.53267978, 59.58998219, 94.0409332, 72.44380772, 35.34413456, 
        15.89971896, 83.98415121
    ],
    "Peso (kg)": [
        222.1696391, 863.1420725, 784.6182442, 449.5939844, 624.0777226, 283.745651, 731.9327824, 577.6950679, 
        453.778969, 813.8904752, 891.0938201, 215.8083756, 760.9382527, 833.8272821, 856.3303884, 568.5125402, 
        392.5804967, 703.5283819, 178.7425238, 645.1189673, 520.9841694, 800.8011161, 140.7344582, 150.2459407, 
        516.406166, 903.8008207, 910.98314, 819.7966099, 143.6583153, 597.4573713, 500.6602133, 658.0364635, 
        670.5333377, 881.2006948, 519.2841707, 480.039552, 312.7190845, 917.1273884, 305.2425308, 181.1990297, 
        868.9047832, 348.4399788, 441.4831761, 414.6846696, 557.949938, 875.6711665, 666.4283871, 334.4304653, 
        162.9861197, 772.5206601
    ]
}
df = pd.DataFrame(data)

X = df[["Altura (cm)"]]
y = df["Peso (kg)"]
model = LinearRegression()
model.fit(X, y)

def generate_graph():
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Altura (cm)"], df["Peso (kg)"], color='blue', label="Datos reales")
    plt.plot(df["Altura (cm)"], model.predict(X), color='red', linewidth=2, label="Línea de regresión")
    plt.xlabel("Altura (cm)")
    plt.ylabel("Peso (kg)")
    plt.title("Regresión Lineal: Altura vs Peso")
    plt.legend()
    plt.grid(True)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close()
    return image_base64


if __name__ == '__main__':
    app.run(debug=True)
