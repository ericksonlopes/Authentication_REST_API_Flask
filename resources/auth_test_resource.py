from flask_restful import Resource


class AuthTestResource(Resource):
    def get(self):
        return {'Message': 'Retorna o método GET, Não precisa de acesso!'}

    def post(self):
        return {'Message': 'Retorna o método POST, O usuário precisa de acesso'}

