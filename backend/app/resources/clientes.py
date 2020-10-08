from flask_restful import Resource

class Clientes(Resource):
    def get(self):
        return "Clientes API"
    def post(self):
        pass