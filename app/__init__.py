from flask import Flask
from .api import api as api_blueprint
from .views import main as main_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.register_blueprint(main_blueprint)

    return app