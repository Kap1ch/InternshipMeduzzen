from sqlalchemy import Column, Integer, String, Boolean

from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    email = Column(String(length=255), nullable=False, unique=True)
    user_name = Column(String(200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    password = Column(String(50), nullable=False)

    phone_number = Column(String(20), nullable=True, unique=True)

    is_active = Column(Boolean, default=False)
