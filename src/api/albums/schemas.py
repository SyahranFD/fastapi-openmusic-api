from pydantic import BaseModel

class AlbumBase(BaseModel):
    name: str
    year: int

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: str

    class Config:
        from_attributes = True