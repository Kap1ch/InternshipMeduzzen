import uuid
from typing import Any

from sqlalchemy import String, Boolean, UUID, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, Mapped

from app.db import Base
from app.logger import custom_logger


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    def to_dict(self, schema):
        schema_fields = [field for field in schema.__fields__]
        obj = {field: getattr(self, field) for field in schema_fields}
        return obj

    @classmethod
    async def get(cls, db: AsyncSession, obj_id: uuid.UUID):
        query = select(cls).filter(cls.id == obj_id)
        result = await db.execute(query)
        return result.scalars().one()

    @classmethod
    async def get_all(cls, db: AsyncSession):
        query = select(cls)
        result = await db.execute(query)
        return result.scalars().all()

    @classmethod
    async def create(cls, db: AsyncSession, **kwargs: dict[str, Any]):
        obj = cls(**kwargs)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        custom_logger.logger.info('Create user')
        return obj

    @classmethod
    async def delete(cls, db: AsyncSession, obj_id: uuid.UUID):
        query = delete(cls).where(cls.id == obj_id)
        await db.execute(query)
        await db.commit()

    async def update(self, db: AsyncSession, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        await db.commit()
        custom_logger.logger.info('Update user')
        return self


class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    user_name: Mapped[str] = mapped_column(String(200), nullable=False)
    first_name: Mapped[str] = mapped_column(String(200), nullable=False)
    last_name: Mapped[str] = mapped_column(String(200), nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)

    phone_number: Mapped[str] = mapped_column(String(20), nullable=True, unique=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
