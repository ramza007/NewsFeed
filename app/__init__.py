from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configuraion
    app.config.from_object(config_options[config_name])

    # Initialising flas extensions
    bootstrap.init_app(app)

    # Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Settings
    from .request import configure_reqest
    configure_request(app)

    return app
