from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class TodoItem():
    title: str
    description: Optional[str]
    due_date: Optional[datetime]

@dataclass
class TodoResponse():
    id: str
    title: str
    description: Optional[str]
    created_at: datetime