from flask_sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)


class Campo(db.Model):
    __tablename__ = 'campo'
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    condicao = db.Column(db.String(80), nullable=False)


class Lote(db.Model):
    pass


class Historico(db.Model):
    pass


class Animal(db.Model):
    pass