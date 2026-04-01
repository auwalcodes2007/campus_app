from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship, DeclarativeBase
from flask_login import UserMixin
from datetime import datetime, timezone
from typing import Optional

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    # Defaults so user could still change in profile settings
    university: Mapped[str] = mapped_column(default="Nile University")
    current_level: Mapped[int] = mapped_column(default=200)

    courses: Mapped[list["Course"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def get_gpa_stats(self):
        graded_units = 0
        total_units = 0
        quality_points = 0

        for course in self.courses:
            units = course.credit_units
            total_units += units

            if course.grade_point is not None:
                graded_units += units
                quality_points += (units * course.grade_point)
        # Current gpa for only finished courses
        current_gpa = (quality_points / graded_units) if graded_units > 0 else 0.0
        # Best case (assume 5.0 for unfinished courses)
        ungraded_units = total_units - graded_units
        best_case_points = quality_points + (ungraded_units * 5)
        best_case_gpa = best_case_points / total_units if total_units > 0 else 0.0
        # Safe case (assume 3.0 for unfinished courses)
        safe_case_points = quality_points + (ungraded_units * 3)
        safe_case_gpa = safe_case_points / total_units if total_units > 0 else 0.0

        return {
            "current": round(current_gpa, 2),
            "best": round(best_case_gpa, 2),
            "safe": round(safe_case_gpa, 2),
        }

    def __repr__(self):
        return f'<User {self.email}>'

class Course(db.Model):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_code: Mapped[str] = mapped_column(nullable=False)
    course_name: Mapped[str] = mapped_column(nullable=False) 
    credit_units: Mapped[int] = mapped_column(nullable=False)
    # --- THE PREDICTOR FIELDS ---
    # Actual grade received at end of sem (0.0 to 5.0)
    grade_point: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    # What the student IS AIMING for (e.g. 5.0)
    target_grade_point: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    # Their current test score (e.g. 22.5)
    ca_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    # The max possible for that test (usually 30 or 40)
    ca_max_score: Mapped[float] = mapped_column(Float, default=40.0)
    semester: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="courses")

    def __repr__(self):
        return f"<Course {self.course_code}>"
  