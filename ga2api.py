from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load student data from JSON file
DATA_FILE = "q-vercel-python.json"
with open(DATA_FILE, "r") as f:
    students = json.load(f)

name_to_marks = {item["name"]: item["marks"] for item in students}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """
    Endpoint to retrieve marks for multiple names in order
    """
    result = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
