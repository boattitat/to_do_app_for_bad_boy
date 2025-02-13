from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import httpx
from datetime import datetime
from models.todo_item import TodoItem, TodoResponse
from services.duplicator_service import HttpDuplicatorService
from services.finalizer_service import HttpFinalizerService
from services.duplicator_service import MockDuplicatorService
from services.finalizer_service import MockFinalizerService

app = FastAPI()
duplicator_service = MockDuplicatorService()
finalizer_service = MockFinalizerService()

# class TodoItem(BaseModel):
#     title: str
#     description: Optional[str] = None
#     due_date: Optional[datetime] = None

# class TodoResponse(BaseModel):
#     id: str
#     title: str
#     description: Optional[str] = None
#     due_date: Optional[datetime] = None
#     created_at: datetime
    

@app.post("/submit", response_model=TodoResponse)
async def submit_todo(todo: TodoItem):

    validated_todo = await validate_todo(todo)
    
    # Call duplicator service
    duplicated_todo = await duplicator_service.duplicate_todo(validated_todo)
    
    # Call finalizer service
    finalized_todo = await finalizer_service.finalize_todo(duplicated_todo)
    
    return finalized_todo

async def validate_todo(todo: TodoItem) -> TodoItem:
    # TODO: Implement validation logic
    return todo

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    # TODO: Implement database retrieval
    return []

def store_in_database(todo_data: dict) -> TodoResponse:
    # TODO: Implement database storage
    return TodoResponse(
        id="placeholder_id",
        title=todo_data["title"],
        description=todo_data.get("description"),
        due_date=todo_data.get("due_date"),
        created_at=datetime.now()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)