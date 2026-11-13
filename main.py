from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="CRUD API - Create and Read")

# Add CORS middleware so the HTML file can communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data structure
class Record(BaseModel):
    title: str
    details: str

# In-memory database
database = []

@app.get("/records", response_model=List[Record])
def read_records():
    """Reads and returns all stored records."""
    return database

@app.post("/records")
def create_record(record: Record):
    """Creates a new record and saves it to the database."""
    database.append(record)
    return {"message": "Record created successfully", "data": record}
