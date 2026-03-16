from flask import Flask
from .models import db
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

load_dotenv()
# Configurations
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return db.session.get(User, user_id)
    migrate = Migrate(app, db)

    # Register blueprints
    from .main.routes import main_bp
    from .auth.routes import auth_bp
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp,  url_prefix='/auth')
    
    return app