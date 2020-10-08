import os

from flask import Flask, Blueprint, render_template
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return render_template('index.html')


    api.init_app(app)

    from .resources import clientes, pedidos

    api.add_resource(clientes.Clientes, '/clientes/')
    api.add_resource(pedidos.Pedidos, '/pedidos/')
    app.register_blueprint(api_bp)

    return app