from pydantic import BaseModel


class TaskDTO(BaseModel):
    id: int
    title: str
    description: str


class TaskCreate(BaseModel):
    title: str
    description: str
