from flask_marshmallow import Marshmallow
from .model import Clientes

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class ClienteSchema(ma.Schema):
    class Meta:
        model = Clientes
        fields = ('first_name',)