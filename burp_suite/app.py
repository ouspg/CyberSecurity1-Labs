from flask import Flask
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = ""  # Needed for sessions

    # Register blueprints
    app.register_blueprint(main_bp)

    return app

