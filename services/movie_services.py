from sqlalchemy.orm import Session
from models.movie_model import Movie
from schemas.movie_schema import MovieCreate

def get_all_movies(db: Session):
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def get_movie_by_genre(db: Session, genre: str):
    return db.query(Movie).filter(Movie.genre == genre).all()

def create_movie(db: Session, movie_data: MovieCreate):
    movie = Movie(title=movie_data.title, genre=movie_data.genre)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def update_movie(db: Session, movie_id: int, movie_data: MovieCreate):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        movie.title = movie_data.title
        movie.genre = movie_data.genre
        db.commit()
        db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie