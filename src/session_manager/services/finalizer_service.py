import httpx
from datetime import datetime
from fastapi import HTTPException
from app import TodoResponse
from services.IFinalizer import IFinalizer
from models.todo_item import TodoItem

class HttpFinalizerService(IFinalizer):
    def __init__(self, finalizer_url: str = "http://finalizer:8002"):
        self.finalizer_url = finalizer_url
    
    async def finalize_todo(self, todo: TodoItem) -> TodoResponse:
        async with httpx.AsyncClient() as client:
            finalizer_response = await client.post(
                f"{self.finalizer_url}/finalize",
                json={
                    'title': todo.title,
                    'description': todo.description,
                    'due_date': todo.due_date.isoformat() if todo.due_date else None
                }
            )
            if finalizer_response.status_code != 200:
                raise HTTPException(status_code=finalizer_response.status_code, 
                                 detail="Finalizer service error")
            return TodoResponse(**finalizer_response.json())

class MockFinalizerService(IFinalizer):
    """Mock implementation of the finalizer service for testing purposes."""
    
    async def finalize_todo(self, todo: TodoItem) -> TodoResponse:
        """Creates a mock finalized version of the todo item."""
        # Simply create a new TodoResponse with the same data
        # In a real mock, you might want to modify some fields to simulate finalization
        return TodoResponse(
            id='dummy_finalized',
            title=todo.title,
            description=todo.description,
            created_at=datetime.now(),
        )
