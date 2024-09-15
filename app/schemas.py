from pydantic import BaseModel


class AlbumBase(BaseModel):
    name: str
    year: int

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: str
    songs: list["Song"] = []

    class Config:
        orm_mode = True


class SongBase(BaseModel):
    title: str
    year: int
    performer: str
    album_id: str

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: str

    class Config:
        orm_mode = True
