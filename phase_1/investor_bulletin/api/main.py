from uvicorn import run
from fastapi import FastAPI

from api.routes import init_routes

from db.models import engine
from db.models.model_base import Base

app = init_routes(FastAPI())

if __name__ == "__main__":

    run("api.main:app")
