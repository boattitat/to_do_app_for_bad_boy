from abc import ABC, abstractmethod
from typing import Dict
from models.todo_item import TodoResponse, TodoItem

class IFinalizer(ABC):
    @abstractmethod
    async def finalize_todo(self, todo: TodoItem) -> TodoResponse:
        pass
