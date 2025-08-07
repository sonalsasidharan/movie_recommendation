from sqlalchemy.orm import Session
from models.movie_model import User
from passlib.hash import bcrypt

def register_user(db: Session, username: str, email: str, password: str):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()