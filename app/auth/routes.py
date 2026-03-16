from flask import Blueprint, render_template
from .forms import RegisterForm, LoginForm

auth_bp = Blueprint('auth' , __name__, template_folder="templates")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle registration logic here (e.g., create user, hash password, etc.)
        pass
    return render_template("auth/register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here (e.g., verify user, check password, etc.)
        pass
    return render_template("auth/login.html", form=form)