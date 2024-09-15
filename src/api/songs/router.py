from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import service, schemas
from src.api.deps import get_db


router = APIRouter()

@router.post("/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return service.create_song(db=db, song=song)

@router.get("/", response_model=list[schemas.Song])
def read_songs(db: Session = Depends(get_db)):
    songs = service.get_all_songs(db)
    return songs

@router.get("/{song_id}", response_model=schemas.Song)
def read_song(song_id: str, db: Session = Depends(get_db)):
    db_song = service.get_song_by_id(db, song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@router.put("/{song_id}", response_model=schemas.Song)
def update_song(song_id: str, song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song = service.update_song(db, song_id, song)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@router.delete("/{song_id}", response_model=schemas.Song)
def delete_song(song_id: str, db: Session = Depends(get_db)):
    db_song = service.delete_song(db, song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
