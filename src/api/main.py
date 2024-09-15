from fastapi import APIRouter

from albums import router as albums

api_router = APIRouter()
api_router.include_router(albums.router, prefix="/albums", tags=["albums"])