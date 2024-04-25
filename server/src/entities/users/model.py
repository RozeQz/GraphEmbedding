from pydantic import BaseModel, ConfigDict
import enum


class RoleEnum(str, enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"


class UserBase(BaseModel):
    login: str
    password: str
    role: RoleEnum
    user_data_id: int


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass
