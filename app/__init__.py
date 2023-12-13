from flask import Flask   # We have created blueprints of each component and the used flask
from .routes import main  #This ensures that the routes are imported correctly

def create_app():        
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(main)
    return app
