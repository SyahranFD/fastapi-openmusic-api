from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Album(Base):
    __tablename__ = "albums"

    id = Column(String, primary_key=True)
    name = Column(String, index=True)
    year = Column(Integer, index=True)

    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = "songs"

    id = Column(String, primary_key=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    performer = Column(String, index=True)
    album_id = Column(String, ForeignKey("albums.id"))

    album = relationship("Album", back_populates="songs")