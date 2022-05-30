from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from modelEncoder import ModelEncoder


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json_encoder = ModelEncoder

db = SQLAlchemy(app)