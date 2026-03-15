from flask import Blueprint

main_bp = Blueprint('main', __name__, template_folder="templates")

@main_bp.route("/")
def home():
    return "Welcome to the Campus App!"