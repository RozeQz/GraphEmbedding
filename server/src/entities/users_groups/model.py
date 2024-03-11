from pydantic import BaseModel, ConfigDict


class UsersGroupBase(BaseModel):
    user_id: int
    group_id: int


class UsersGroup(UsersGroupBase):
    model_config = ConfigDict(from_attributes=True)


class UsersGroupCreate(UsersGroupBase):
    pass


class UsersGroupUpdate(UsersGroupCreate):
    pass
