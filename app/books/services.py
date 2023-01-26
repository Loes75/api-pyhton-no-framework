import json
from werkzeug.exceptions import NotFound
from werkzeug.wrappers import Response

from app.commons.commons import Commons
from app.db import Book, create_session
from app.formats.view_format_factory import ViewFormatFactory


class BookService:

    def __init__(self):
        self.__view_format_factory = ViewFormatFactory()

    @staticmethod
    def get_all_books(environ: dict, start_response, args):
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

    @staticmethod
    def get_book(environ: dict, start_response, args):
        session = create_session()
        book = session.query(Book).get(args['id'])
        if book is not None:
            book = book.to_dict()
        response = Response(json.dumps(book, indent=4, sort_keys=True, default=str),
                            content_type="application/json")
        return response(environ, start_response)

    def read_book(self, environ: dict, start_response, args):
        page = args['page']
        view_format = args['format']
        session = create_session()
        book = session.query(Book).get(args['id'])
        if book is not None:
            book = book.to_dict()
            if page > len(book['pages']):
                raise NotFound
            else:
                data = {
                    'book': book,
                    'page': str(page)
                }
                view_format_service = self.__view_format_factory.get_format(view_format=view_format)
                return view_format_service.reading(data=data, environ=environ, start_response=start_response)
        else:
            raise NotFound
