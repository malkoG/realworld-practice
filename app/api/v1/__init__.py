from fastapi import APIRouter

from app.api.v1 import products, lectures

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(lectures.router, prefix="/lectures", tags=["lectures"])
