from redis import asyncio as redis

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.config import settings

redis_connect = redis.Redis(host=settings.redis_host, port=settings.redis_port)

engine = create_async_engine(
    url=settings.database_url,
    echo=settings.echo,
)

Session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
