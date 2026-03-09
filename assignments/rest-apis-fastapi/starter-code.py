from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory data store
items = []

class Item(BaseModel):
    id: int
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}

# TODO: Add your CRUD endpoints here