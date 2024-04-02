from typing import Optional

from pydantic import BaseModel, ConfigDict


class ResultBase(BaseModel):
    user_id: int
    test_id: int
    points: float
    answers: Optional[str] = None
    time_spent: Optional[int] = None


class Result(ResultBase):
    model_config = ConfigDict(from_attributes=True)


class ResultCreate(ResultBase):
    pass


class ResultUpdate(ResultCreate):
    pass
