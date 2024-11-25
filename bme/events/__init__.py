from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Register blueprints
    from bme.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()
