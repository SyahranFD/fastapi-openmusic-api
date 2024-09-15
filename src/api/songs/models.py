from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(String(255), primary_key=True)
    title = Column(String(255), index=True)
    year = Column(Integer, index=True)
    performer = Column(String(255), index=True)
    genre = Column(String(255), index=True)
    duration = Column(Integer, index=True)
    album_id = Column(String(255), ForeignKey("albums.id"))

    album = relationship("Album", back_populates="songs")