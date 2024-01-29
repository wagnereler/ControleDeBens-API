#app/domain/__init__.py
from flask_restx import Namespace, Resource, fields
api_ms = Namespace('api', description='''Esta é uma API RestFull para uma aplicação de controle de bens''')


def get_versao():
    versao = '1.0'
    return versao

versao_model = api_ms.model('Versao', {
    'versao': fields.String(),
})

@api_ms.route('/')
class Versao(Resource):

    @api_ms.marshal_with(versao_model)
    def get(self):
        get_versao()
        return {'versao': get_versao()}
