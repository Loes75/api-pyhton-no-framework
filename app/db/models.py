from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, JSON
from typing import Dict
from app import db
from .modelbase import SqlAlchemyBase


class Book(SqlAlchemyBase):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    pages = Column(JSON, nullable=True)

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'title': self.title,
            'author': self.author,
            'pages': self.pages
        }