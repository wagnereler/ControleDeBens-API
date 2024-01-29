#app/domain/empresa/setor_resource.py
from flask import request
from flask_restx import Resource
from app.infraestructure.orm.controlde_bens.setor import Setor as OrmSetor
from app.domain.empresa.setor_service import inserir_setor, obter_setores
from app.domain.empresa.setor_model import (inserir_setor_model,
                                            obter_setor_model,
                                            listar_setores_por_empresa_model)
from app.domain.empresa import empresa_ns


@empresa_ns.route('/setor')
@empresa_ns.doc({'setor'})
class Setor(Resource):

    @empresa_ns.marshal_list_with(obter_setor_model)
    def get(self):
        _setor = obter_setores()
        return _setor

    @empresa_ns.expect(inserir_setor_model)
    @empresa_ns.marshal_with(inserir_setor_model, code=201)
    def post(self):
        data = request.json
        _setor = inserir_setor(data['nome'], data['id_empresa'])
        return _setor, 201


@empresa_ns.route('/setor/<int:id_empresa>')
class ListarSetoresPorEmpresaId(Resource):

    @empresa_ns.marshal_with(listar_setores_por_empresa_model)
    def get(self, id_empresa):
        _setor = OrmSetor.query.filter_by(id_empresa=id_empresa).all()
        return _setor
