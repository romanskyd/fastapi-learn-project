from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    role: str = 'USER'
    description: Optional[str] = None # или str | None


class STask(STaskAdd):
    id: int
