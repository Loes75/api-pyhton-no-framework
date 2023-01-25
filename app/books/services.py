from werkzeug.wrappers import Request, Response

from app.commons.commons import Commons
from app.db import Book, create_session
import json


class BookService:

    def __init__(self):
        pass

    def get_all_books(self, environ: dict, start_response, args):
        session = create_session()
        books = session.query(Book)
        total = 0
        if books is not None:
            total = session.query(Book).count()
            books = Commons.serialize_generics_models(books)
        else:
            books = []
        ressponse_data = {
            'books': books,
            'total': total
        }
        response = Response(json.dumps(ressponse_data, indent=4, sort_keys=True, default=str),
                            content_type="application/json")
        return response(environ, start_response)

    def get_book(self, environ: dict, start_response, args):
        session = create_session()
        book = session.query(Book).get(args['id'])
        if book is not None:
            book = book.to_dict()
        response = Response(json.dumps(book, indent=4, sort_keys=True, default=str),
                            content_type="application/json")
        return response(environ, start_response)

    def read_book(self, environ: dict, start_response, args):
        response = Response(f"reading book")
        return response(environ, start_response)
