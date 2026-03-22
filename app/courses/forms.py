from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class CourseForm(FlaskForm):
    course_code = StringField("Course Code", validators=[DataRequired()])
    course_name = StringField("Course Name", validators=[DataRequired()])
    credit_units = IntegerField("Credit Units", validators=[DataRequired(), NumberRange(min=0)])
    grade_points = FloatField("Grade Points", validators=[NumberRange(min=0, max=5)])
    semester = StringField("Semester", validators=[DataRequired()])