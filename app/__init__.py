from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, 
                static_folder = "static",
                static_url_path="/static",
                template_folder="templates")
    
    from .routes import main_bp
    app.register_blueprint(main_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", 'sqlite:///subjects.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from . import models
    return app