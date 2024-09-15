import uuid
from sqlalchemy.orm import Session
from . import models, schemas


def get_all_albums(db: Session):
    return db.query(models.Album).all()

def get_album_by_id(db: Session, album_id: str):
    return db.query(models.Album).filter(models.Album.id == album_id).first()

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