from werkzeug.exceptions import NotFound, HTTPException
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from app.books.routes import books_urls
from app.books.controllers import books_router

welcome_urls = [
    Rule('/', endpoint='welcome'),
    Rule('/favicon.ico ', endpoint='welcome')
]
all_urls = welcome_urls + books_urls
url_map = Map(all_urls)


def app(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
        path = environ["PATH_INFO"]
        print(f"path: {path}, endpoint: {endpoint}, args: {str(args)}")
        if 'library' in endpoint:
            return books_router(environ=environ, start_response=start_response, endpoint=endpoint, args=args)
        elif 'welcome' in endpoint:
            request = Request(environ)
            response = Response(f"Welcome to the Library API")
            return response(environ, start_response)
        else:
            raise NotFound
    except HTTPException as e:
        return e(environ, start_response)
