from pydantic import BaseModel, ConfigDict


class UsersTopicBase(BaseModel):
    user_id: int
    topic_id: int


class UsersTopic(UsersTopicBase):
    model_config = ConfigDict(from_attributes=True)


class UsersTopicCreate(UsersTopicBase):
    pass


class UsersTopicUpdate(UsersTopicCreate):
    pass
