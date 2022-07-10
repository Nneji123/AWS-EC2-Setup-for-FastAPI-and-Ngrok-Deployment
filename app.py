# USE_NGROK=True uvicorn server:app

import os
import sys

from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.logger import logger
from pydantic import BaseSettings


class Settings(BaseSettings):
    # ... The rest of our FastAPI settings

    BASE_URL = "http://localhost:8000"
    USE_NGROK = os.environ.get("USE_NGROK", "False") == "True"


settings = Settings()


def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass


# Initialize the FastAPI app for a simple web server
app = FastAPI()

if settings.USE_NGROK:
    # pyngrok should only ever be installed or initialized in a dev environment when this flag is set
    from pyngrok import ngrok

    # Get the dev server port (defaults to 8000 for Uvicorn, can be overridden with `--port`
    # when starting the server
    port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 8000

    # Open a ngrok tunnel to the dev server
    public_url = ngrok.connect(port)
    logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, port))

    # Update any base URLs or webhooks to use the public ngrok URL
    settings.BASE_URL = public_url
    init_webhooks(public_url)

# ... Initialize routers and the rest of our app

@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
Recommendation Engine API 🙌🏻
This API recommends content such as games, movies, music, books and even anime!
Note: add "/redoc" to get the complete documentation.
  """
    return note