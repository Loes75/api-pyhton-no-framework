from werkzeug.exceptions import NotFound

from app.formats.view_format_html import ViewFormatHTML
from app.formats.view_format_text import ViewFormatText
from app.formats.view_formats import ViewFormats


class ViewFormatFactory:

    @staticmethod
    def get_format(view_format: str) -> ViewFormats:
        if view_format == 'html':
            return ViewFormatHTML()
        if view_format == 'text':
            return ViewFormatText()
        else:
            raise NotFound
