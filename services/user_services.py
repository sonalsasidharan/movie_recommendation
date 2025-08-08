from sqlalchemy.orm import Session
from models.movie_model import User
from passlib.hash import bcrypt
from schemas.user_schema import UserCreate

def register_user(db: Session, user_data: UserCreate):
    hashed_password = bcrypt.hash(user_data.password)
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password,
        liked_genre=user_data.liked_genre
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def verify_user_credentials(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not bcrypt.verify(password, user.password_hash):
        return None
    return user