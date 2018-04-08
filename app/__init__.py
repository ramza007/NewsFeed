from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from newsapi import NewsApiClient

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # App config
    app.config.from_object(config_options[config_name])

    # Intitializing flask ext.
    bootstrap.init_app(app)

    # Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting conigurations
    from .requests import configure_request
    configure_request(app)

    return app
