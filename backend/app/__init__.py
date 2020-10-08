import os

from flask import Flask, Blueprint, render_template
from flask_restful import Api
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db/stdev"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)
    Migrate(app, app.db)

    from .resources import cliente, pedido
    api.init_app(app)
    api.add_resource(cliente.Cliente, '/cliente/')
    api.add_resource(pedido.Pedido, '/pedido/')
    app.register_blueprint(api_bp)


    @app.route('/')
    def hello():
        return render_template('index.html')

    return app