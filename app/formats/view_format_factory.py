from werkzeug.exceptions import NotFound

from app.formats.view_format_html import ViewFormatHTML
from app.formats.view_format_text import ViewFormatText
from app.formats.view_formats import ViewFormats


class ViewFormatFactory:
    """
        Factory to handle view formats
    """

    @staticmethod
    def get_format(view_format: str) -> ViewFormats:
        """
        Gets the class of the requested format
        :param view_format: str
        :return: View format class
        """
        if view_format == 'html':
            return ViewFormatHTML()
        if view_format == 'text':
            return ViewFormatText()
        else:
            raise NotFound
