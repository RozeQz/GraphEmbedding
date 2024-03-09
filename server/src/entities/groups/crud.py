from sqlalchemy.orm import Session
from typing import List, Optional, Type

from server.src.entities.schema import Group
from server.src.entities.groups.schemas import GroupCreate, GroupUpdate


def get_one(session: Session, obj_id: int) -> Optional[Group]:
    return session.query(Group).where(Group.id == obj_id).first()


def get_all(session: Session) -> List[Type[Group]]:
    return session.query(Group).all()


def create(session: Session, obj_create: GroupCreate) -> Group:
    obj_dict = obj_create.model_dump()
    group = Group(**obj_dict)
    session.add(group)
    session.commit()
    session.refresh(group)
    return group


def update(session: Session, obj: Group,
           obj_update: GroupUpdate) -> Group:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Group) -> Group:
    session.delete(obj)
    session.commit()
    return obj
