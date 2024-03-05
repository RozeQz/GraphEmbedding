from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    question: str
    answer: str
    type: int
    options: str


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskCreate):
    pass
