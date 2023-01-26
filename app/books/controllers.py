from app.books.services import BookService
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound, MethodNotAllowed

books_service = BookService()


def books_router(environ, start_response, endpoint, args):
    """
      Routes to the requested services
    """
    method = environ['REQUEST_METHOD']
    if method == 'GET':
        if endpoint == 'library/':
            return books_service.get_all_books(environ=environ, start_response=start_response, args=args)
        elif endpoint == 'library/book/':
            return books_service.get_book(environ=environ, start_response=start_response, args=args)
        elif endpoint == 'library/book/page/':
            return books_service.read_book(environ=environ, start_response=start_response, args=args)
        else:
            raise NotFound
    elif method == 'POST':
        raise MethodNotAllowed
    elif method == 'PUT':
        raise MethodNotAllowed
    elif method == 'DELETE':
        raise MethodNotAllowed
