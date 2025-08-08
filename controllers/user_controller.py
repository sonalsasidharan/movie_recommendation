from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.user_schema import UserCreate, UserOut , UserLogin
from services.user_services import register_user, get_user_by_username,verify_user_credentials
from services.movie_services import get_movie_by_genre

user_router = APIRouter()

@user_router.post("/users/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    print("Incoming user data:", user.dict())
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return register_user(db, user)

@user_router.get("/users/{username}", response_model=UserOut)
def get_user(username: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/users/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = verify_user_credentials(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "liked_genre": db_user.liked_genre}

@user_router.get("/users/{username}/recommendations")
def recommend_movies(username: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    movies = get_movie_by_genre(db, user.liked_genre)
    return {"recommended_movies": movies}