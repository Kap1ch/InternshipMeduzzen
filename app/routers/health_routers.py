from fastapi import APIRouter

from app.db.base import redis_connect

router = APIRouter()


@router.get('/')
async def health_check():
    await redis_connect.set('key', 'value')
    data = await redis_connect.get('key')
    return {
        "status_code": 200,
        "detail": "ok",
        "message": "working",
        "redis": data
    }


@router.on_event('shutdown')
async def shutdown_event():
    await redis_connect.close()
