from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import service, schemas
from ..deps import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Album)
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    return service.create_album(db=db, album=album)

@router.get("/", response_model=list[schemas.Album])
def read_albums(db: Session = Depends(get_db)):
    albums = service.get_all_albums(db)
    return albums

@router.get("/{album_id}", response_model=schemas.Album)
def read_album(album_id: str, db: Session = Depends(get_db)):
    db_album = service.get_album_by_id(db, album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.put("/{album_id}", response_model=schemas.Album)
def update_album(album_id: str, album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    db_album = service.update_album(db, album_id, album)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@router.delete("/{album_id}", response_model=schemas.Album)
def delete_album(album_id: str, db: Session = Depends(get_db)):
    db_album = service.delete_album(db, album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album
