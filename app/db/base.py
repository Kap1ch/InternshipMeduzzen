from redis import asyncio as redis

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

database_url = (f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@localhost:5432/"
                f"{settings.postgres_db}")
redis_connect = redis.Redis(host=settings.redis_host, port=settings.redis_port)

engine = create_async_engine(
    url=database_url,
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