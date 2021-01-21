from sql_alchemy import data


# Criação do Modelo de dado que é usado
class UserModel(data.Model):
    __tablename__ = 'users'

    user_id = data.Column(data.Integer, primary_key=True)
    name = data.Column(data.String(40), UNIQUE=True)
    password = data.Column(data.String(40))

    def __init__(self, login, password):
        self.login = login
        self.password = password
