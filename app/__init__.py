from flask import Flask

# Configurations

def create_app():
    app = Flask(__name__)

    # Initialize extensions

    # Register blueprints
    from .main.routes import main_bp
    from .auth.routes import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp,  url_prefix='/auth')
    
    return app