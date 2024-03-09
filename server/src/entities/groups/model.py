from pydantic import BaseModel, ConfigDict


class GroupBase(BaseModel):
    name: str


class Group(GroupBase):
    model_config = ConfigDict(from_attributes=True)


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupCreate):
    pass
