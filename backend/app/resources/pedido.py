from flask_restful import Resource

class Pedido(Resource):
    def get(self):
        return "Pedidos API"
    def post(self):
        pass