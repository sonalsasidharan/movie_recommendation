from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import Depends

DB_URL = "mysql+pymysql://root:Psk%402706@localhost/Movie_DB"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        print("Database connection successful.")
    except Exception as e:
        print("Database connection failed:", e)
    finally:
        db.close()