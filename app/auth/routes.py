from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm
from ..models import db, User
from .. import bcrypt
from urllib.parse import urlparse


auth_bp = Blueprint('auth' , __name__, template_folder="templates")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle registration logic here (e.g., create user, hash password, etc.)
        password = form.password.data
        password_hash = bcrypt.generate_password_hash(password)
        new_user = User(email=form.email.data, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('main.dashboard'))
    return render_template("auth/register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here (e.g., verify user, check password, etc.)
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            print(next_page)
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('main.dashboard')
            return redirect(next_page)
        flash('Invalid username or password. Please try again.', 'error')
    return render_template("auth/login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))