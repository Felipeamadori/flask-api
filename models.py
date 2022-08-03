from app import *
from models import db

class Campo(db.Model):
    __tablename__ = 'campo'
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    condicao = db.Column(db.String(80), nullable=False)
    historicos = db.relationship('Historico', backref='campo', lazy=True)

    def to_json(self):
        return {"id" : self.id,
                "nome" : self.nome,
                "tipo" : self.tipo,
                "condicao" : self.condicao}


class Lote(db.Model):
    __tablename__ = 'lote'
    id = db.Column(db.Integer, primary_key=True) 
    qtd = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.Integer, nullable=False)
    animais = db.relationship('Animal', backref='lote', lazy=True)
    historicos = db.relationship('Historico', backref='lote', lazy=True)

    def to_json(self):
        return {"id" : self.id,
                "qtd" : self.qtd,
                "descricao" : self.descricao,
                "animais" : self.animais}

class Animal(db.Model):
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True) 
    raca = db.Column(db.String(80), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    lote_id = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)

    def to_json(self):
        return {"id" : self.id,
                "raca" : self.raca,
                "peso" : self.peso,
                "lote_id" : self.lote_id}

class Historico(db.Model):
    __tablename__='historico'
    entrada = db.Column(db.Date, primary_key=True)
    saida = db.Column(db.Date)
    lote_id = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    campo_id = db.Column(db.Integer, db.ForeignKey('campo.id'), nullable=False)

    def to_json(self):
        return {"entrada" : self.entrada,
                "saida" : self.saida,
                "campo_id" : self.campo_id,
                "lote_id" : self.lote_id}