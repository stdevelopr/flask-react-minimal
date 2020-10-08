
from flask import current_app, request, jsonify
from flask_restful import Resource
from app.model import Cliente
from app.serializer import ClienteSchema

class Clientes(Resource):
    def get(self):
        cs = ClienteSchema(many=True)
        result = Cliente.query.all()
        return cs.jsonify(result)

    def post(self):
        json_data = request.get_json()
        cs = ClienteSchema()
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        try:
            data = cs.load(json_data)
        except Exception as err:
            return err.messages, 422
        
        new_client = Cliente(**data)

        current_app.db.session.add(new_client)
        current_app.db.session.commit()

        result = cs.dump(Cliente.query.get(new_client.id))
        return {"message": "Created new client.", "client": result}

    
class ClienteId(Resource):
    def get(self, id):
        cs = ClienteSchema()
        result = Cliente.query.get(id)

        return cs.jsonify(result)
    
    def put(self, id):
        json_data = request.get_json()
        cs = ClienteSchema()

        # Validate and deserialize input
        try:
            data = cs.load(json_data)
        except Exception as err:
            return err.messages, 422

        query = Cliente.query.filter_by(id=id)
        query.update(data)
        current_app.db.session.commit()
        
        return cs.jsonify(query.first())

    def delete(self, id):
        Cliente.query.filter_by(id=id).delete()
        current_app.db.session.commit()
        return jsonify('Deleted!')