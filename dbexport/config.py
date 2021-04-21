import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = "postgresql://user:password@localhost:5432/reviews"


@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = DB_URI or os.getenv("DB_URL")
    if not db_url:
        raise ValueError("database URL is required")
    print(f"Returning an engine for {db_url}")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url).connect()


@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))


try:
    Session = session_class()
except:
    print("Failed to create default Session class.")
    pass
