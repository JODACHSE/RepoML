from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

mySql = MySQL()
app = Flask(__name__)

load_dotenv()
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mySql.init_app(app)
__all__ = ["app", "mySql"]
