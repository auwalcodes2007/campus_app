from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configurations

    # Initialize extensions

    # Register blueprints
    from .main.routes import main_bp
    from .auth.routes import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app