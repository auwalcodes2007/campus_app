from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class CourseForm(FlaskForm):
    course_code = StringField("Course Code", validators=[DataRequired()])
    course_name = StringField("Course Name", validators=[DataRequired()])
    credit_units = SelectField('Credit Units', choices=[(i, str(i)) for i in range(1, 7)], coerce=int, validators=[DataRequired()])    
    grade_point = FloatField("Grade Point (0.0 - 5.0)", validators=[NumberRange(min=0, max=5), Optional()])
    semester = SelectField("Semester", choices=[
        ("2024/2025-1", "2024/2025 - Semester 1"),
        ("2024/2025-2", "2024/2025 - Semester 2"),
        ("2025/2026-1", "2025/2026 - Semester 1"),
        ("2025/2026-2", "2025/2026 - Semester 2"),
    ], validators=[DataRequired()])
    submit = SubmitField("Save Course")