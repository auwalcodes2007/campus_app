from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Optional


class CourseForm(FlaskForm):
    course_code = StringField("Course Code", validators=[DataRequired()])
    course_name = StringField("Course Name", validators=[DataRequired()])
    credit_units = SelectField("Credit Units", choices=[(i, str(i)) for i in range(1, 7)], coerce=int, validators=[DataRequired()])    
    grade_point = SelectField("Final Grade", choices=[(None, "Ongoing"), (5.0, "A"), (4.0, "B"), (3.0, "C"), (2.0, "D"), (0.0, "F")], coerce= lambda x: float(x) if x not in ["None", None, ""] else None,validators=[Optional()])
    target_grade_point = SelectField("Target Grade", choices=[(5.0, "A"), (4.0, "B"), (3.0, "C"), (2.0, "D"), (0.0, "F")], validators=[Optional()])
    ca_score = DecimalField("Your CA Score", validators=[NumberRange(min=0, max=40), Optional()])
    ca_max_score = DecimalField("Max CA Score", default=40.0, validators=[NumberRange(min=0, max=40), Optional()])
    semester = SelectField("Semester", choices=[
        ("2024/2025-1", "2024/2025 - Semester 1"),
        ("2024/2025-2", "2024/2025 - Semester 2"),
        ("2025/2026-1", "2025/2026 - Semester 1"),
        ("2025/2026-2", "2025/2026 - Semester 2"),
    ], validators=[DataRequired()])
    submit = SubmitField("Save Course")