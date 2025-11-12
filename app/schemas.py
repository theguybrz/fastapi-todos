from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    completed: bool | None = None

class TodoOut(TodoBase):
    id: int

    class Config:
        from_attributes = True