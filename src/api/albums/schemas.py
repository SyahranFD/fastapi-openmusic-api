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