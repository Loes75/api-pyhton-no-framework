from app.formats.view_formats import ViewFormats
from typing import Any
from werkzeug.wrappers import Response


class ViewFormatText(ViewFormats):

    def reading(self, data, environ, start_response) -> Any:
        response = Response(f"{data['book']['title']} page {data['page']} : "
                            f"\n {data['book']['pages'][str(data['page'])]}")
        return response(environ, start_response)
