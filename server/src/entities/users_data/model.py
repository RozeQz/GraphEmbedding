from typing import Optional

from pydantic import BaseModel, ConfigDict


class UsersDataBase(BaseModel):
    firstname: str
    lastname: str
    midname: Optional[str]
    email: str


class UsersData(UsersDataBase):
    model_config = ConfigDict(from_attributes=True)


class UsersDataCreate(UsersDataBase):
    pass


class UsersDataUpdate(UsersDataCreate):
    pass
