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

@app.route("/snake_game")
def snake_game():
    return render_template("html/snake_game.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
