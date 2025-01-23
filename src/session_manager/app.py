from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import httpx
from datetime import datetime

app = FastAPI()

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TodoResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    created_at: datetime

@app.post("/submit", response_model=TodoResponse)
async def submit_todo(todo: TodoItem):
    # Validate & transform TODO
    validated_todo = await validate_todo(todo)
    
    # Call duplicator service
    async with httpx.AsyncClient() as client:
        duplicator_response = await client.post(
            "http://duplicator:8001/processStep",
            json=validated_todo.dict()
        )
        if duplicator_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Duplicator service error")
        
        # Call finalizer service
        finalizer_response = await client.post(
            "http://finalizer:8002/finalize",
            json=duplicator_response.json()
        )
        if finalizer_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Finalizer service error")
        
        # TODO: Insert into database
        return store_in_database(finalizer_response.json())

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    # TODO: Implement database retrieval
    return []

async def validate_todo(todo: TodoItem) -> TodoItem:
    # TODO: Implement validation logic
    return todo

def store_in_database(todo_data: dict) -> TodoResponse:
    # TODO: Implement database storage
    return TodoResponse(
        id="placeholder_id",
        title=todo_data["title"],
        description=todo_data.get("description"),
        due_date=todo_data.get("due_date"),
        created_at=datetime.now()
    )