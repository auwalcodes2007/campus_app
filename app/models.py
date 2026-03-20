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

    courses: Mapped[list["Course"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.email}>'

class Course(db.Model):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_code: Mapped[str] = mapped_column(nullable=False)
    course_name: Mapped[str] = mapped_column(nullable=False) 
    credit_units: Mapped[int] = mapped_column(nullable=False)
    grade_points: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    semester: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="courses")

    def __repr__(self):
        return f"<Course {self.course_code}>"
  