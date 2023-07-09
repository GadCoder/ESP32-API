from fastapi import FastAPI
from sqlalchemy.orm import Session
from db.session import Base
from db.session import engine
from api.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app


app = start_application()
