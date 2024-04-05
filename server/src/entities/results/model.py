from typing import Optional, Union, List

from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):
    task_id: int
    answer: Union[str, List[str]]


class ResultBase(BaseModel):
    user_id: int
    test_id: int
    points: float
    answers: Optional[List[AnswerBase]] = None
    time_spent: Optional[int] = None


class Result(ResultBase):
    model_config = ConfigDict(from_attributes=True)


class ResultCreate(ResultBase):
    pass


class ResultUpdate(ResultCreate):
    pass
