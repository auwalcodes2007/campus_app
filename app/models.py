from . import db
from sqlalchemy.orm import mapped_column, Mapped
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'