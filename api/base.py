from fastapi import APIRouter
from api.routes import route_metric, route_pill

api_router = APIRouter()


api_router.include_router(route_metric.router, prefix="", tags=["metrics"])
api_router.include_router(route_pill.router, prefix="", tags=["pills"])
