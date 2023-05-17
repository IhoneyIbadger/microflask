from flask import Flask
from .api.user import user

# this is a test

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(user, url_prefix='/api/v1')

    return app
