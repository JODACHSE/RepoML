"""
Aplicacion flask para Machine Learning (conceptos)
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """Retornamos una pagina html con bootstrap"""
    return render_template('index.html')
