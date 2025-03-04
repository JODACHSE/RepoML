"""
Aplicacion flask para Machine Learning (conceptos)
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    """retornamos la pagina web"""
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("html/home.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
