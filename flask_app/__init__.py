from flask import Flask
from .api.user import service

# this is a test

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(service, url_prefix='/api/v1')

    return app
