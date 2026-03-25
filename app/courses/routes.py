from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Course, db
from .forms import CourseForm
from flask_wtf.csrf import generate_csrf

courses_bp = Blueprint("courses", __name__, template_folder="templates")

@courses_bp.route("/")
@login_required
def courses():
    # Current user already has a .courses attribute
    return render_template("courses/courses.html")

@courses_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        new_course = Course(
            course_code=form.course_code.data,
            course_name=form.course_name.data,
            credit_units=form.credit_units.data,
            grade_point=form.grade_point.data,
            semester=form.semester.data,
            user=current_user
        )

        try:
            db.session.add(new_course)
            db.session.commit()
            flash(f"Nice! {new_course.course_code} has been added to your tracker.", "success")
            return redirect(url_for("courses.courses")) 
        except Exception as e:
            db.session.rollback()
            flash("Omo, something went wrong with the database. Try again!", "error")
            print(f"Error: {e}")
    return render_template("courses/add_course.html", form=form)


@courses_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_course(id):
    pass

@courses_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete_course(id):
    pass