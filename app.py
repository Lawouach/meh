from typing import Union

import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World beyond!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return httpx.get("https://www.google.com").text



