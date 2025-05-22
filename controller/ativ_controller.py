from flask import Blueprint, request, jsonify
from models.ativ_model import Atividades
from database import db
import requests

routes = Blueprint("routes", __name__)


def validar_professor(professor_id):
    r = requests.get(f"http://192.168.0.69:5000/{professor_id}")
    return r.status_code == 200


@routes.route('/')
def index():
    return 'API de Atividades funcionando! Adicione "/atividades" para visualizar'

@routes.route("/atividades", methods=["POST"])
def criar_atividade():
    dados = request.json
    professor_id = dados.get("professor_id")

    if not validar_professor(professor_id):
        return jsonify({"erro": "Professor não encontrado."}), 400

    atividade = Atividades(
        professor_id=professor_id,
        tipo=dados.get("tipo"),
        data_entrega=dados.get("data_entrega"),
        titulo=dados.get("titulo"),
        descricao=dados.get("descricao")
    )

    db.session.add(atividade)
    db.session.commit()

    return jsonify({"mensagem": "Atividade criada com sucesso"}), 201

@routes.route("/atividades", methods=["GET"])
def listar_atividades():
    atividades = Atividades.query.all()
    return jsonify([
        {
            "id": r.id,
            "professor_id": r.professor_id,
            "tipo": r.tipo,
            "data_entrega": r.data_entrega,
            "titulo": r.titulo,
            "descricao": r.descricao
        } for r in atividades
    
    ])
