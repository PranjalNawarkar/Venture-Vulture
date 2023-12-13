from flask import Flask
from .routes import main  # Ensure routes are imported correctly

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(main)
    return app