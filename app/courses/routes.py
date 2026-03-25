from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Course, db
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
        new_course = Course(user=current_user)
        form.populate_obj(new_course)  # Automatically populate the Course object from the form data

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