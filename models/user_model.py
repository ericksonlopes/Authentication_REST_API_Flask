from sql_alchemy import data


# Criação do Modelo de dado que é usado
class UserModel(data.Model):
    __tablename__ = 'users'

    user_id = data.Column(data.Integer, primary_key=True)
    login = data.Column(data.String(40), UNIQUE=True)
    password = data.Column(data.String(40))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    # Retorna os dados recebido no __init__ em json
    def json(self):
        return {
            "user_id": self.user_id,
            "login": self.login
        }

    # pesquisa usuario pelo login
    @classmethod
    def find_by_login(cls, login):
        # Pesquisa dentro do banco de dados o primeiro resultado encontrado do login
        user = cls.query_find_by(login=login).first()
        # se existir retorna o usuario
        if user:
            return user
        return False

    # pesquisa usuario pelo user_id
    @classmethod
    def find_user(cls, user_id):
        # Pesquisa dentro do banco de dados o primeiro resultado encontrado do login
        user = cls.query_find_by(user_id=user_id).first()
        # se existir retorna o usuario
        if user:
            return user
        return False

    def save_user(self):
        data.session.add(self)
        data.session.commit()

    def delete_user(self):
        data.session.delete(self)
        data.session.commit()
