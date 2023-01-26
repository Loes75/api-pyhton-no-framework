import os
import time

from app import app
from werkzeug.serving import run_simple
from dotenv import load_dotenv
from app.db import db_init

load_dotenv()  # Loads environment variables from .env file
db_init()  # Initialize DB session

if __name__ == "__main__":
    try:
        PORT = int(os.getenv("PORT", 3000))
        run_simple('localhost', PORT, app, use_reloader=True)
        print(f"{time.asctime()} Server listening on http://localhost:{PORT}")
    except KeyboardInterrupt:
        print(f"{time.asctime()} Server down")
    #         httpd.server_close()
