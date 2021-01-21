from flask_restful import Resource
from flask_jwt_extended import jwt_required


class AuthTestResource(Resource):
    def get(self):
        return {'Message': 'Retorna o método GET, Não precisa de acesso!'}

    # Decorador para que a requisição só seja realizada com usuário identificado
    @jwt_required
    def post(self):
        return {'Message': 'Retorna o método POST, O usuário precisa de acesso'}

