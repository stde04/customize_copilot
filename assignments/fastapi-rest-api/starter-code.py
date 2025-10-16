# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory database
items_db: List[Item] = []

# TODO: Implement API endpoints for CRUD operations

# Example GET endpoint
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

# Add more endpoints below...
