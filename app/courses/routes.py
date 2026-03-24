from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .forms import CourseForm

courses_bp = Blueprint("courses", __name__, template_folder="templates")

@courses_bp.route("/")
@login_required
def courses():
    pass

@courses_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        pass
    return render_template("courses/add_course.html", form=form)


@courses_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_course(id):
    pass

@courses_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete_course(id):
    pass