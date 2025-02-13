from abc import ABC, abstractmethod
from models.todo_item import TodoItem, TodoResponse

class IDuplicator(ABC):
    @abstractmethod
    async def duplicate_todo(self, todo: TodoItem) -> TodoResponse:
        pass
