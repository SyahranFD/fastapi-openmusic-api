from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/albums/", response_model=schemas.Album)
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    return crud.create_album(db=db, album=album)

@app.get("/albums/", response_model=list[schemas.Album])
def read_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    albums = crud.get_all_albums(db)
    return albums

@app.get("/albums/{album_id}", response_model=schemas.Album)
def read_album(album_id: str, db: Session = Depends(get_db)):
    db_album = crud.get_album_by_id(db, album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@app.put("/albums/{album_id}", response_model=schemas.Album)
def update_album(album_id: str, album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    db_album = crud.update_album(db, album_id, album)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@app.delete("/albums/{album_id}", response_model=schemas.Album)
def delete_album(album_id: str, db: Session = Depends(get_db)):
    db_album = crud.delete_album(db, album_id)
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db_album

@app.post("/songs/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return crud.create_song(db=db, song=song)

@app.get("/songs/", response_model=list[schemas.Song])
def read_songs(db: Session = Depends(get_db)):
    songs = crud.get_all_songs(db)
    return songs

@app.get("/songs/{song_id}", response_model=schemas.Song)
def read_song(song_id: str, db: Session = Depends(get_db)):
    db_song = crud.get_song_by_id(db, song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@app.put("/songs/{song_id}", response_model=schemas.Song)
def update_song(song_id: str, song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song = crud.update_song(db, song_id, song)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@app.delete("/songs/{song_id}", response_model=schemas.Song)
def delete_song(song_id: str, db: Session = Depends(get_db)):
    db_song = crud.delete_song(db, song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song
