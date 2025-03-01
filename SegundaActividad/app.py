"""
Aplicacion flask para Machine Learning (conceptos)
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """retornamos la pagina web"""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
