from pydantic import BaseModel, ConfigDict


class UsersTaskBase(BaseModel):
    user_id: int
    task_id: int


class UsersTask(UsersTaskBase):
    model_config = ConfigDict(from_attributes=True)


class UsersTaskCreate(UsersTaskBase):
    pass


class UsersTaskUpdate(UsersTaskCreate):
    pass
