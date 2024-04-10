import uvicorn
from fastapi import FastAPI
from app.config import settings
from app.routers import routers


app = FastAPI()


app.include_router(routers.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.host, port=settings.port, reload=True)