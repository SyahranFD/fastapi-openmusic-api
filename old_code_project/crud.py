import uuid

from sqlalchemy.orm import Session

from . import models, schemas


def get_all_albums(db: Session):
    return db.query(models.Album).all()

def get_album_by_id(db: Session, album_id: str):
    return db.query(models.Album).filter(models.Album.id == album_id).first()

def get_songs_by_album_id(db: Session, album_id: str):
    return db.query(models.Song).filter(models.Song.album_id == album_id).all()

def create_album(db: Session, album: schemas.AlbumCreate):
    album_id = f"album-{uuid.uuid4()}"
    db_album = models.Album(id=album_id, **album.model_dump())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

def update_album(db: Session, album_id: str, album: schemas.AlbumCreate):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    db_album.name = album.name
    db_album.year = album.year
    db.commit()
    db.refresh(db_album)
    return db_album

def delete_album(db: Session, album_id: str):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    db.delete(db_album)
    db.commit()
    return db_album


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