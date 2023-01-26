from app.formats.view_formats import ViewFormats
from typing import Any
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class ViewFormatHTML(ViewFormats):

    def __init__(self):
        super().__init__()
        self.templates_directory = Path.cwd() / "app" / "templates"
        self.env = Environment(loader=FileSystemLoader(self.templates_directory.absolute()))

    def reading(self, data, environ, start_response) -> Any:
        template = self.env.get_template('read-book.html')
        html = template.render(data)
        start_response('200 OK', [
            ("Content-Type", "text/html"),
            ("Cache-Control", "public, max-age=0, must-revalidate"),
        ])
        return [bytes(html, "utf-8")]
