from pydantic import BaseModel, ConfigDict


class TopicBase(BaseModel):
    title: str
    file_name: str


class Topic(TopicBase):
    model_config = ConfigDict(from_attributes=True)


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicCreate):
    pass
