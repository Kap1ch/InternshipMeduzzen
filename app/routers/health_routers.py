from fastapi import APIRouter

from app.db.base import redis_connect

router = APIRouter()


@router.get('/')
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "message": "working",
        "redis": await redis_connect.ping()

    }
