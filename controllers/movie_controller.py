from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db
from schemas.movie_schema import MovieCreate, MovieOut
from services.movie_services import (
    get_all_movies,
    get_movie_by_id,
    get_movie_by_genre,
    create_movie,
    update_movie,
    delete_movie
)

movie_router = APIRouter()

@movie_router.get("/",response_class=HTMLResponse)
def home():
    return "welcome"

@movie_router.get("/movies", response_model=list[MovieOut])
def fetch_all_movies(db: Session = Depends(get_db)):
    return get_all_movies(db)

@movie_router.get("/movies/{movie_id}", response_model=MovieOut)
def fetch_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@movie_router.get("/movies/genre/{genre}", response_model=list[MovieOut])
def fetch_movie_by_genre(genre: str, db: Session = Depends(get_db)):
    movies = get_movie_by_genre(db, genre)
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found under this genre")
    return movies

@movie_router.post("/movies", response_model=MovieOut)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db, movie)

@movie_router.put("/movies/{movie_id}", response_model=MovieOut)
def modify_movie(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    updated_movie = update_movie(db, movie_id, movie)
    if not updated_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie

@movie_router.delete("/movies/{movie_id}")
def remove_movie(movie_id: int, db: Session = Depends(get_db)):
    deleted_movie = delete_movie(db, movie_id)
    if not deleted_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"detail": "Movie deleted successfully"}