import uuid

from sqlalchemy import String, Boolean, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)

    email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    user_name: Mapped[str] = mapped_column(String(200), nullable=False)
    first_name: Mapped[str] = mapped_column(String(200), nullable=False)
    last_name: Mapped[str] = mapped_column(String(200), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    phone_number: Mapped[str] = mapped_column(String(20), nullable=True, unique=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
