from os import abort
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from modelEncoder import ModelEncoder
from models import *
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json_encoder = ModelEncoder

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
def get_animal(id):
    animal = Animal.query.get(id)
    if animal is None:
        abort(404)
    return jsonify(animal.to_json())

@app.route("/historicos/<int:id>", methods=["GET"])
def get_historico(id):
    historico = Historico.query.get(id)
    if historico is None:
        abort(404)
   # historico.entrada = datetime.strptime(historico.entrada, '%Y-%m-%d')    
    return jsonify(historico.to_json())
    
@app.route("/campos/<int:id>", methods=["DELETE"])
def delete_campo(id):
    campo = Campo.query.get(id)
    if campo is None:
        abort(404)
    db.session.delete(campo)
    db.session.commit()
    return jsonify({'result': True})

@app.route("/lotes/<int:id>", methods=["DELETE"])
def delete_lote(id):
    lote = Lote.query.get(id)
    if lote is None:
        abort(404)
    db.session.delete(lote)
    db.session.commit()
    return jsonify({'result': True})

@app.route("/animais/<int:id>", methods=["DELETE"])
def delete_animal(id):
    animal = Animal.query.get(id)
    if animal is None:
        abort(404)
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'result': True})

@app.route("/historicos/<int:id>", methods=["DELETE"])
def delete_historico(id):
    historico = Historico.query.get(id)
    if historico is None:
        abort(404)
    db.session.delete(historico)
    db.session.commit()
    return jsonify({'result': True})

#Post e Put de Historico 

@app.route('/historicos', methods=['POST'])
def create_historico():
    if not request.json:
        abort(400)
    if request.json.get('saida'):
        historico = Historico(
        #   entrada=datetime.strptime(request.json.get('entrada'), '%Y-%m-%d'),
        #   saida=datetime.strptime(request.json.get('saida'), '%Y-%m-%d'),
            entrada=request.json.get('entrada'),
            saida=request.json.get('saida'),
            campo_id=request.json.get('campo_id'),
            lote_id=request.json.get('lote_id')
        )
    else:
        historico = Historico(
            entrada=request.json.get('entrada'),
            campo_id=request.json.get('campo_id'),
            lote_id=request.json.get('lote_id')
        )

    db.session.add(historico)
    db.session.commit()
    return jsonify(historico.to_json()), 201

@app.route('/historicos/<int:id>', methods=['PUT'])
def update_historico(id):
    if not request.json:
        abort(400)
    historico = Historico.query.get(id)
    if historico is None:
        abort(404)
    
    if request.json.get('saida'):
            historico.entrada=request.json.get('entrada',historico.entrada),
            historico.saida=request.json.get('saida',historico.saida),
            historico.campo_id=request.json.get('campo_id',historico.campo_id),
            historico.lote_id=request.json.get('lote_id',historico.lote_id)
    else:
            historico.entrada=request.json.get('entrada',historico.entrada),
            historico.campo_id=request.json.get('campo_id',historico.campo_id),
            historico.lote_id=request.json.get('lote_id',historico.lote_id)

    db.session.merge(historico)
    db.session.commit()
    return jsonify(historico.to_json())

###############################################################################################

@app.route('/campos', methods=['POST'])
def create_campo():
    if not request.json:
        abort(400)
    campo = Campo(
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
    db.session.merge(campo)
    db.session.commit()
    return jsonify(campo.to_json())

@app.route('/lotes', methods=['POST'])
def create_lote():
    if not request.json:
        abort(400)
    lote = Lote(
        qtd=request.json.get('qtd'),
        descricao=request.json.get('descricao')
    )
    db.session.add(lote)
    db.session.commit()
    return jsonify(lote.to_json()), 201

@app.route('/lotes/<int:id>', methods=['PUT'])
def update_lote(id):
    if not request.json:
        abort(400)
    lote = Lote.query.get(id)
    if lote is None:
        abort(404)
    lote.qtd = request.json.get('qtd', lote.qtd)
    lote.descricao = request.json.get('descricao', lote.descricao)
    db.session.merge(lote)
    db.session.commit()
    return jsonify(lote.to_json())

@app.route('/animais', methods=['POST'])
def create_animal():
    if not request.json:
        abort(400)
    lote = Lote.query.get(request.json.get('lote_id'))
    if lote is None:
        abort(404)
    animal = Animal(
        raca=request.json.get('raca'),
        peso=request.json.get('peso'),
        lote_id=request.json.get('lote_id')
    )
    db.session.add(animal)
    db.session.commit()
    return jsonify(animal.to_json()), 201

@app.route('/animais/<int:id>', methods=['PUT'])
def update_animal(id):
    if not request.json:
        abort(400)
    animal = Animal.query.get(id)
    if animal is None:
        abort(404)
    lote = Lote.query.get(request.json.get('lote_id'))
    if lote is None:
        abort(404)
    animal.raca = request.json.get('raca', animal.raca)
    animal.peso = request.json.get('peso', animal.peso)
    animal.lote_id = request.json.get('lote_id', animal.lote_id)
    db.session.merge(animal)
    db.session.commit()
    return jsonify(animal.to_json())


if __name__=="__main__":
    app.run(debug=True)

