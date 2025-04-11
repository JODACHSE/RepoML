"""
Aplicación flask para Machine Learning (conceptos)
"""
from flask import render_template, request
from python.db_connection import app
from python.S4 import linear_regression
from python.S4 import linear_regression_weight_and_height
from python.S6 import logistic_regression
from python.S7.mc_classification_methods import get_models_data
from python.S8.mc_transport_package_upload import get_predict_data_from_file

app.config["DEBUG"] = True
# pip install -r requirements.txt
# Usar en terminal: flask --app app run --debug


@app.route("/")
def index():
    """retornamos la pagina web"""
    return render_template("index.html")


@app.route("/andres")
def andres():
    """Ruta para la pagina de Andres"""
    return render_template("html/S2/andres.html")


@app.route("/nicolas")
def nicolas():
    """Ruta para la pagina de Nicolas"""
    return render_template("html/S2/nicolas.html")


@app.route("/python")
def ver_codigo():
    """Ruta para ver el 'hola_mundo.py' y el 'adios_mundo.py' en una pagina web"""
    with open("python/S2/hola_mundo.py", "r", encoding="utf8") as file:
        hola = file.read()
    with open("python/S2/adios_mundo.py", "r", encoding="utf8") as file:
        adios = file.read()
    with open("README.md", "r", encoding="utf8") as file:
        readme = file.read()
    return render_template("html/S2/ver_codigo.html", hola=hola, adios=adios, readme=readme)


@app.route("/installation_flask")
def installation_flask():
    """Ruta proceso de instalacion de Flask"""
    return render_template("html/S3/installation_flask.html")


@app.route("/history_flask")
def history_flask():
    """Ruta para la historia de flask"""
    return render_template("html/S3/history_flask.html")


@app.route("/caso_uso_ml_supervisado")
def caso_uso_ml_supervisado():
    """Ruta para Caso de uso de machine learning"""
    return render_template("html/S3/CasoUsoMLSupervisado.html")


@app.route("/snake_game")
def snake_game():
    """Ruta para el juego de la serpiente"""
    return render_template("html/S3/snake_game.html")


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
    return render_template("html/S4/linear_regression_grades.html",
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
            predicted_result = linear_regression_weight_and_height.model.predict([[altura]])[
                0]
        except ValueError:
            predicted_result = "Entrada no válida"

    return render_template("html/S4/linear_regression_peso_altura.html",
                           result=predicted_result,
                           graph=graph_image)


@app.route("/logistic_regression_mind_map")
def logistic_regression_mind_map():
    """
    Página para mostrar mapa mental sobre Regresión logistica
    """
    return render_template("html/S5/logistic_regression_mind_map.html")


@app.route("/logistic_regression_case", methods=["GET", "POST"])
def logistic_regression_case():
    """
    Página para predecir si un paquete se podrá transportar y mostrar métricas de evaluación.
    """
    predicted_result = None
    metrics = None

    if request.method == "POST":
        try:
            distancia = float(request.form.get("distancia"))
            peso = float(request.form.get("peso"))
            clima = request.form.get("clima")
            trafico = request.form.get("trafico")

            # Ahora la función retorna una tupla (predicción, métricas)
            predicted_result, metrics = logistic_regression.predict_transport(
                distancia, peso, clima, trafico)

        except (ValueError, TypeError):
            predicted_result = "Entrada no válida"

    return render_template("html/S6/logistic_regression_case.html",
                           result=predicted_result,
                           metrics=metrics)


@app.route("/mc_classification_methods")
def mc_classification_methods():

    models_data = get_models_data()
    return render_template("html/S7/mc_classification_methods.html", data=models_data)

@app.route("/mc_transport_package_upload", methods=["GET", "POST"])
def mc_transport_package_upload():
    output_file = None
    error_message = None

    try:
        if request.method == "POST":
            file = request.files['file']
            if str(file.filename).endswith(".csv") or str(file.filename).endswith(".xlsx"):
                file_path = f"./static/files/upload/{file.filename}"
                file.save(file_path)
                output_file = get_predict_data_from_file(file.filename)
            else:
                raise ValueError("Solo se permiten archivos .csv o .xlsx")
    except Exception as e:
        error_message = str(e)

    return render_template(
        "html/S8/mc_transport_package_upload.html",
        output_file=output_file,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)
