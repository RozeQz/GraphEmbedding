from pydantic import BaseModel, ConfigDict


class ResultBase(BaseModel):
    user_id: int
    test_id: int
    points: float
    answers: dict


class Result(ResultBase):
    model_config = ConfigDict(from_attributes=True)


class ResultCreate(ResultBase):
    pass


class ResultUpdate(ResultCreate):
    pass
