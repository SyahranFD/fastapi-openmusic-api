from fastapi import APIRouter

from .albums.router import router as albums
from .songs.router import router as songs

api_router = APIRouter()
api_router.include_router(albums, prefix="/albums")
api_router.include_router(songs, prefix="/songs")