from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.auth_test_resource import AuthTestResource
from resources.users_resource import UserRegister

app = Flask(__name__)
# configurações do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_users.db'
app.config['SQLALCHEMT_TRACK_MODIFICATIONS'] = False

# Informa ao sistema que o app irá conter uma blacklist
app.config['JWT_BLACKLIST_ENABLED'] = True
# especifica a chave sercreta
app.config['JWT_SECRET_KEY'] = 'Chavesecreta'

api = Api(app)

jwt = JWTManager()

# Decorar que ativa a função qunado a primeira requests for feita
@app.before_first_request
def create_db():
    data.create_all()


api.add_resource(AuthTestResource, 'test/')
api.add_resource(UserRegister, 'register/')
# api.add_resource(UserLogin, 'login/')
# api.add_resource(UserLogout, 'logout/')

if __name__ == '__main__':
    from sql_alchemy import data

    # especificando onde o banco de dados irá ser utilizado
    data.init_app(app)
    app.run(debug=True)
