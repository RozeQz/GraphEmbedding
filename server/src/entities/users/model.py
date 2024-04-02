from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    login: str
    password: str
    role_id: int
    user_data_id: int


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass
