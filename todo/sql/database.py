from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

root_path = os.path.dirname(os.path.abspath(__file__))
SQLITE_FALLBACK = f"sqlite:///{root_path}/todo.db"
SQLACLHEMY_DATABASE_URL = os.getenv("DATABASE_URL") or SQLITE_FALLBACK

engine = create_engine(SQLACLHEMY_DATABASE_URL)
if SQLACLHEMY_DATABASE_URL == SQLITE_FALLBACK:
    engine = create_engine(
        SQLACLHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
