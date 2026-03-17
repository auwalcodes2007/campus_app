from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm
from ..models import db, User
from .. import bcrypt


auth_bp = Blueprint('auth' , __name__, template_folder="templates")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle registration logic here (e.g., create user, hash password, etc.)
        password = form.password.data
        password_hash = bcrypt.generate_password_hash(password)
        new_user = User(email=form.email.data, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('main.home'))
    return render_template("auth/register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here (e.g., verify user, check password, etc.)
        pass
    return render_template("auth/login.html", form=form)