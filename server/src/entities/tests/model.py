from pydantic import BaseModel, ConfigDict


class TestBase(BaseModel):
    name: str


class Test(TestBase):
    model_config = ConfigDict(from_attributes=True)


class TestCreate(TestBase):
    pass


class TestUpdate(TestCreate):
    pass
