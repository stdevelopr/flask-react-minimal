
from flask import current_app, request
from flask_restful import Resource
from app.model import Clientes
from app.serializer import ClienteSchema

class Cliente(Resource):
    def get(self):
        cs = ClienteSchema(many=True)
        result = Clientes.query.all()
        return cs.jsonify(result)

    def post(self):
        json_data = request.get_json()
        cs = ClienteSchema()
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        try:
            data = cs.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        
        first_name = data["first_name"]
        new_client = Clientes(first_name=first_name)

        current_app.db.session.add(new_client)
        current_app.db.session.commit()

        result = cs.dump(Clientes.query.get(new_client.id))
        return {"message": "Created new client.", "client": result}