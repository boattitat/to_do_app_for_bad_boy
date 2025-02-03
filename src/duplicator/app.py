from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class ProcessedTodo(BaseModel):
    original: TodoItem
    duplicate: TodoItem

@app.post("/processStep")
async def process_step(todo: TodoItem) -> ProcessedTodo:
    # TODO: Implement duplication logic
    duplicate = TodoItem(
        title=f"Copy of {todo.title}",
        description=todo.description,
        due_date=todo.due_date
    )
    
    return ProcessedTodo(
        original=todo,
        duplicate=duplicate
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)