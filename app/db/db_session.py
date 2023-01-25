import os

from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session, sessionmaker

from .modelbase import SqlAlchemyBase

__factory = None


def db_init():
    """Initializes database with given URI from .env"""
    global __factory

    if __factory:
        return

    database_uri = os.getenv("DATABASE_URI", "sqlite:///books.db")

    if database_uri.startswith("sqlite"):
        engine = create_engine(
            database_uri,
            echo=False,
            connect_args={"check_same_thread": False},
        )
    else:
        engine = create_engine(database_uri, echo=False)

    __factory = sessionmaker(bind=engine)
    print("Successfully connected to DB")

    from ..db import models

    # If table don't exist, Create.
    if not inspect(engine).has_table("books"):
        SqlAlchemyBase.metadata.tables["books"].create(engine)


def create_session() -> Session:
    """Returns the database session"""
    global __factory
    return __factory()