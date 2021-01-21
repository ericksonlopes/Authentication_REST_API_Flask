from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

from models.user_model import UserModel

arguments = reqparse.RequestParser()
arguments.add_argument('name')
arguments.add_argument('password')


class UserRegister(Resource):
    def post(self):
        dados = arguments.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'message', f"The login '{dados['login']}' already exists"}

        user = UserModel(**dados)
        user.save_user()

        return {'message': 'user saved successfully'}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        # Recebo os dados recebidos no data do post
        dados = arguments.parse_args()

        user = UserModel.find_by_login(dados['login'])
        # verifica se o login do usuario E se a senha for compativel com a do user do banco
        if user and safe_str_cmp(user.password, dados['senha']):
            pass
