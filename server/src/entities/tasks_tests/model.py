from pydantic import BaseModel, ConfigDict


class TasksTestBase(BaseModel):
    test_id: int
    task_id: int


class TasksTest(TasksTestBase):
    model_config = ConfigDict(from_attributes=True)


class TasksTestCreate(TasksTestBase):
    pass


class TasksTestUpdate(TasksTestCreate):
    pass
