import httpx
from fastapi import HTTPException
from datetime import datetime
from models.todo_item import TodoItem, TodoResponse
from services.IDuplicator import IDuplicator

class HttpDuplicatorService(IDuplicator):
    def __init__(self, duplicator_url: str = "http://duplicator:8001"):
        self.duplicator_url = duplicator_url
    
    async def duplicate_todo(self, todo: TodoItem) -> TodoResponse:
        async with httpx.AsyncClient() as client:
            duplicator_response = await client.post(
                f"{self.duplicator_url}/processStep",
                json=todo.dict()
            )
            if duplicator_response.status_code != 200:
                raise HTTPException(status_code=duplicator_response.status_code, 
                                 detail="Duplicator service error")
            return TodoResponse(**duplicator_response.json())

class MockDuplicatorService(IDuplicator):
    """Mock implementation of the duplicator service for testing purposes."""
    
    async def duplicate_todo(self, todo: TodoItem) -> TodoResponse:
        """Creates a mock duplicate of the todo item."""
        # Simply create a new TodoResponse with the same data
        # In a real mock, you might want to modify some fields to simulate duplication
        return TodoResponse(
            id="dummy_duplicate",
            title=todo.title,
            description=todo.description,
            created_at=datetime.now(),
        )
