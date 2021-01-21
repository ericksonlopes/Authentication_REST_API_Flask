from flask_restful import Resource, reqparse

arguments = reqparse.RequestParser()
arguments.add_argument('name')
arguments.add_argument('password')


class UserResorce(Resource):
    def get(self, user_id):
        pass

    def post(self):
        dados = arguments.parse_args()

