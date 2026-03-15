from flask import Blueprint, render_template
from .forms import RegisterForm, LoginForm

auth_bp = Blueprint('auth' , __name__, template_folder="templates")

@auth_bp.route("/register")
def register():
    form = RegisterForm()
    return render_template("auth/register.html")

@auth_bp.route("/login")
def login():
    form = LoginForm()
    return render_template("auth/login.html")