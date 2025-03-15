"""
Aplicación flask para Machine Learning (conceptos)
"""
from flask import Flask, render_template, request
from python.S3 import linear_regression
from python.S4 import linear_regression_weight_and_height

app = Flask(__name__)
app.config["DEBUG"] = True
# Usar en terminal: flask --app app run --debug


@app.route("/")
def index():
    """retornamos la pagina web"""
    return render_template("index.html")


@app.route("/andres")
def andres():
    """Ruta para la pagina de Andres"""
    return render_template("html/S1/andres.html")


@app.route("/nicolas")
def nicolas():
    """Ruta para la pagina de Nicolas"""
    return render_template("html/S1/nicolas.html")


@app.route("/python")
def ver_codigo():
    """Ruta para ver el 'hola_mundo.py' y el 'adios_mundo.py' en una pagina web"""
    with open("python/S1/hola_mundo.py", "r", encoding="utf8") as file:
        hola = file.read()
    with open("python/S1/adios_mundo.py", "r", encoding="utf8") as file:
        adios = file.read()
    with open("README.md", "r", encoding="utf8") as file:
        readme = file.read()
    return render_template("html/S1/ver_codigo.html", hola=hola, adios=adios, readme=readme)


@app.route("/installation_flask")
def installation_flask():
    """Ruta proceso de instalacion de Flask"""
    return render_template("html/S2/installation_flask.html")


@app.route("/history_flask")
def history_flask():
    """Ruta para la historia de flask"""
    return render_template("html/S2/history_flask.html")


@app.route("/caso_uso_ml_supervisado")
def caso_uso_ml_supervisado():
    """Ruta para Caso de uso de machine learning"""
    return render_template("html/S2/CasoUsoMLSupervisado.html")


@app.route("/snake_game")
def snake_game():
    """Ruta para el juego de la serpiente"""
    return render_template("html/S2/snake_game.html")


@app.route("/linearRegression", methods=["GET", "POST"])
def linear_regression_grades():
    """
    Pagina para predecir notas basado en horas de estudio
    """
    predicted_result = None
    graph_image = None
    if request.method == "POST":
        hours = float(request.form.get("hours"))
        predicted_result = linear_regression.calculate_grade(hours)
        graph_image = linear_regression.generate_graph(hours)
    return render_template("html/S3/linear_regression_grades.html",
                           result=predicted_result,
                           graph=graph_image)


@app.route("/linearRegression/weight_height", methods=["GET", "POST"])
def linear_regression_peso_altura():
    """
    Página para predecir el peso basado en la altura usando regresión lineal
    """
    predicted_result = None
    graph_image = linear_regression_weight_and_height.generate_graph()

    if request.method == "POST":
        try:
            altura = float(request.form.get("altura"))
            predicted_result = linear_regression_weight_and_height.model.predict([[altura]])[0]
        except ValueError:
            predicted_result = "Entrada no válida"

    return render_template("html/S4/linear_regression_peso_altura.html",
                           result=predicted_result,
                           graph=graph_image)


if __name__ == "__main__":
    app.run(debug=True)
