from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI()

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class ProcessedTodo(BaseModel):
    original: TodoItem
    duplicate: TodoItem

class FinalizedTodo(BaseModel):
    todos: List[TodoItem]
    processed_at: datetime
    metadata: dict

@app.post("/finalize")
async def finalize(processed_todo: ProcessedTodo) -> FinalizedTodo:
    # TODO: Implement finalization logic
    todos = [processed_todo.original, processed_todo.duplicate]
    
    return FinalizedTodo(
        todos=todos,
        processed_at=datetime.now(),
        metadata={
            "source": "finalizer",
            "version": "1.0"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)