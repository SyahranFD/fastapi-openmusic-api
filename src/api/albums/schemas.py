from pydantic import BaseModel
from src.api.songs.schemas import Song


class AlbumBase(BaseModel):
    name: str
    year: int

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: str
    songs: list["Song"] = []

    class Config:
        from_attributes = True