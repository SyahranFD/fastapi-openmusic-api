from typing import Optional
from pydantic import BaseModel

class SongBase(BaseModel):
    title: str
    year: int
    performer: str
    genre: str
    duration: int
    album_id: Optional[str] = None

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: str

    class Config:
        from_attributes = True
