from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
Simple AWS API 🙌🏻
Example of how to deploy FastAPI application to an AWS EC2 instance.
  """
    return note


