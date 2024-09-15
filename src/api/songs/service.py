import uuid
from sqlalchemy.orm import Session
from . import models, schemas


def get_all_songs(db: Session):
    return db.query(models.Song).all()

def get_song_by_id(db: Session, song_id: str):
    return db.query(models.Song).filter(models.Song.id == song_id).first()

def create_song(db: Session, song: schemas.SongCreate):
    song_id = f"song-{uuid.uuid4()}"
    db_song = models.Song(id=song_id, **song.model_dump())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

def update_song(db: Session, song_id: str, song: schemas.SongCreate):
    db_song = db.query(models.Song).filter(models.Song.id == song_id).first()
    db_song.title = song.title
    db_song.year = song.year
    db_song.performer = song.performer
    db_song.album_id = song.album_id
    db.commit()
    db.refresh(db_song)
    return db_song

def delete_song(db: Session, song_id: str):
    db_song = db.query(models.Song).filter(models.Song.id == song_id).first()
    db.delete(db_song)
    db.commit()
    return db_song