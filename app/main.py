import uvicorn
from fastapi import FastAPI
from app.config import settings
from app.routers import health_routers
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(health_routers.router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.host, port=settings.port, reload=True)