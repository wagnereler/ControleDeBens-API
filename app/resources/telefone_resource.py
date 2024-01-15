from flask import request
from flask_restx import Resource, fields
from app.resources import name_space
from app.services.telefone_service import criar_telefone

telefone_model = name_space.model('Telefone', {
    'id': fields.Integer(readonly=True),
    'tipo': fields.Integer(required=True),
    'ddi': fields.String(required=False),
    'dd': fields.String(required=True),
    'numero': fields.String(required=True),
})

@name_space.route('/telefone')
class TelefoneResource(Resource):
    @name_space.expect(telefone_model)
    @name_space.marshal_with(telefone_model, code=201)
    def post(self):
        data = request.json
        try:
            telefone = criar_telefone(data['tipo'], data('ddi'), data['dd'], data['numero'])
            return telefone, 201
        except Exception as e:
            return {'message': f'Erro ao criar telefone{e}'}, 500
