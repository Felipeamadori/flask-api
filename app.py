from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/campos', methods=['GET'])
def get_campos():
    campos = Campo.query.all()
    return jsonify([campo.to_json() for campo in campos])

@app.route('/lotes', methods=['GET'])
def get_lotes():
    lotes = Lote.query.all()
    return jsonify([lote.to_json() for lote in lotes])

@app.route('/animais', methods=['GET'])
def get_animais():
    animais = Animal.query.all()
    return jsonify([animal.to_json() for animal in animais])

@app.route('/historicos', methods=['GET'])
def get_historicos():
    historicos = Historico.query.all()
    return jsonify([historico.to_json() for historico in historicos])

@app.route("/campos/<int:id>", methods=["GET"])
def get_campo(id):
    campo = Campo.query.get(id)
    if campo is None:
        abort(404)
    return jsonify(campo.to_json())

@app.route("/lotes/<int:id>", methods=["GET"])
def get_lote(id):
    lote = Lote.query.get(id)
    if lote is None:
        abort(404)
    return jsonify(lote.to_json())

@app.route("/animais/<int:id>", methods=["GET"])
def get_campo(id):
    animal = Animal.query.get(id)
    if animal is None:
        abort(404)
    return jsonify(animal.to_json())
    
@app.route("/campo/<int:id>", methods=["DELETE"])
def delete_campo(id):
    campo = Campo.query.get(id)
    if campo is None:
        abort(404)
    db.session.delete(campo)
    db.session.commit()
    return jsonify({'result': True})

@app.route('/campos', methods=['POST'])
def create_campo():
    if not request.json:
        abort(400)
    campo = campo(
        nome=request.json.get('nome'),
        tipo=request.json.get('tipo'),
        condicao=request.json.get('condicao')
    )
    db.session.add(campo)
    db.session.commit()
    return jsonify(campo.to_json()), 201

@app.route('/campos/<int:id>', methods=['PUT'])
def update_campo(id):
    if not request.json:
        abort(400)
    campo = Campo.query.get(id)
    if campo is None:
        abort(404)
    campo.nome = request.json.get('nome', campo.nome)
    campo.tipo = request.json.get('tipo', campo.tipo)
    campo.condicao = request.json.get('condicao', campo.condicao)
    db.session.commit()
    return jsonify(campo.to_json())




if __name__=="__main__":
    app.run(debug=True)

