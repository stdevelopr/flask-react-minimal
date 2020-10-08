from flask_restful import Resource

class Pedidos(Resource):
    def get(self):
        return "Pedidos API"
    def post(self):
        pass