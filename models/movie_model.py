from sqlalchemy import Column, Integer, String
from database import Base

class Movie(Base):
    __tablename__ = 'movies'

    id= Column(Integer, primary_key= True, index= True)
    title= Column(String(255), nullable=False)
    genre= Column(String(255), nullable=False  )

class User(Base):
    __tablename__ = 'users'
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String(50), nullable=False, unique=True)
    email= Column(String(50), nullable=False, unique= True)
    password_hash= Column(String(255), nullable=False)
    liked_genre= Column(String(100), nullable=False)


