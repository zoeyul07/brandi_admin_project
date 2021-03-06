from flask import Flask
from flask_cors import CORS

from custom_encoder import JsonCustomEncoder
from controllers.user_controllers import user_app
from controllers.main_controllers import main_app
from controllers.product_controllers import product_app


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['JSON_SORT_KEYS'] = False
    app.json_encoder = JsonCustomEncoder
    app.register_blueprint(user_app, url_prefix='/user')
    app.register_blueprint(main_app, url_prefix='/main')
    app.register_blueprint(product_app, url_prefix='/product')
    return app
