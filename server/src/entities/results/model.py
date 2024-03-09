from pydantic import BaseModel, ConfigDict


class ResultBase(BaseModel):
    question: str
    answer: str
    type: int
    options: str


class Result(ResultBase):
    model_config = ConfigDict(from_attributes=True)


class ResultCreate(ResultBase):
    pass


class ResultUpdate(ResultCreate):
    pass
