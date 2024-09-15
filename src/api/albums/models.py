from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base

class Album(Base):
    __tablename__ = "albums"

    id = Column(String(255), primary_key=True)
    name = Column(String(255), index=True)
    year = Column(Integer, index=True)

    songs = relationship("Song", back_populates="album")