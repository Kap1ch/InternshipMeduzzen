import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI

from app.routers import routers

env_vars = dotenv_values('../.env')

app = FastAPI()


app.include_router(routers.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=env_vars["HOST"], port=int(env_vars["PORT"]), reload=True)