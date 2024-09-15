from fastapi import APIRouter

from .albums.router import router as albums

api_router = APIRouter()
api_router.include_router(albums, prefix="/albums", tags=["albums"])