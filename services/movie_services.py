from sqlalchemy.orm import Session
from models.movie_model import Movie,User

def get_movie_by_id(db:Session,movie_id:int):
    return db.query(Movie).all(Movie.id==movie_id).first()

def get_all_movies(db:Session):
    return db.query(Movie).all()

def create_movie(db:Session,id:int,title:str,genre:str,user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    db_movie=Movie(id=id,title=title,genre=genre)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db:Session,movie_id:int,user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    movie=db.query(Movie).filter(Movie.id==movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie

def update_movie(db:Session,movie_id:int,title:str,genre:str,user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    movie=db.query(Movie).filter(Movie.id==movie_id).first()
    if movie:
        movie.title=title
        movie.genre=genre
        db.commit()
        db.refresh(movie)
    return movie

def get_movie_by_genre(db:Session,genre:str):
    return db.query(Movie).all(Movie.genre==genre)
