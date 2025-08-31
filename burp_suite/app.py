from flask import Flask
from routes.main import main_bp
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = ""  # Needed for sessions

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app

