from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

from blacklist import BLACKLIST
from models.user_model import UserModel

arguments = reqparse.RequestParser()
arguments.add_argument('login', type=str, required=True, help="The filnds 'Login' cannot be left blank")
arguments.add_argument('password', type=str, required=True, help="The filnds 'password' cannot be left blank")


class User(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}

    # decorar para que a requisição só seja feita por usuario autenticado
    @jwt_required
    def delete(self, user_id):
        # Busca o obj do id requisitado
        user = UserModel.find_user(user_id)
        # Se o usuario existir
        if user:
            try:
                # Tenta deletar o usuário
                user.delete_user()
                return {'message': f"User deleted."}
            except Exception as error:
                return {'message error': f'Erro ao Deletar os dados {error}'}
        return {'message': f'User not found.'}


# classe para Registrar usuario
class UserRegister(Resource):
    def post(self):
        # recebe os dados da requisição via post e cria um dict
        dados = arguments.parse_args()

        # Pesquisa se o login do usuario ja existe no sistema
        if UserModel.find_by_login(dados['login']):
            # se caso existir exibe uma mensagem
            return {'message': f"The login '{dados['login']}' already exists"}

        # caso não exista tenta criar
        try:
            user = UserModel(**dados)
            user.save_user()
        except Exception as error:
            return {'message error': f"{error}"}

        return {'message': 'user saved successfully'}, 201


# Classe para Logar usuario
class UserLogin(Resource):
    @classmethod
    def post(cls):
        # Recebo os dados recebidos no data do post
        dados = arguments.parse_args()
        # pesquisa o login dentro
        user = UserModel.find_by_login(dados['login'])
        # Se a o usuario existir e a senha for compativel com a do usuario dentro do sistema, cria um token ao usuario
        if user and safe_str_cmp(user.password, dados['password']):
            # Cria um token de acesso para o id do usuario logado
            token_access = create_access_token(identity=user.user_id)
            # Retorna o token
            return {'access': token_access}, 200

        return {'message': 'The username or password is incorrect.'}, 401  # nao autorizado


# Classe para Logout do usuario
class UserLogout(Resource):
    # decorador - é preciso estar logado para fazer logout
    @jwt_required
    def post(self):
        # Pega o id do token do usuario logado
        jwt_id = get_raw_jwt()['jti']
        # adiciona dentro da blacklist
        BLACKLIST.add(jwt_id)
        return {'message': 'Successfully Logged Out'}
