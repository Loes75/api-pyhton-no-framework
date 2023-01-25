from werkzeug.routing import Rule

books_urls = [
    Rule('/library/', endpoint='library/'),
    Rule('/library/book/<int:id>/', endpoint='library/book/'),
    Rule('/library/book/<int:id>/page/<format>', endpoint='library/book/page/')
]
