from flask_jwt_extended import create_access_token
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
        # pesquisa o login dentro
        user = UserModel.find_by_login(dados['login'])
        # Se a o usuario existir e a senha for compativel com a do usuario dentro do sistema, cria um token ao usuario
        if user and safe_str_cmp(user.password, dados['senha']):
            # Cria um token de acesso para o id do usuario logado
            token_access = create_access_token(identity=user.user_id)
            # Retorna o token
            return {'access': token_access}, 200
