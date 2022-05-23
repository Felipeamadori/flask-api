from app import *


class Campo(db.Model):
    __tablename__ = 'campo'
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    condicao = db.Column(db.String(80), nullable=False)

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

class Animal(db.Model):
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True) 
    raca = db.Column(db.String(80), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    lote_id = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)