from sqlalchemy.orm import Session
from typing import List, Optional, Type

from server.src.entities.schema import UsersData
from server.src.entities.users_data.schemas import UsersDataCreate, UsersDataUpdate


def get_one(session: Session, obj_id: int) -> Optional[UsersData]:
    return session.query(UsersData).where(UsersData.id == obj_id).first()


def get_all(session: Session) -> List[Type[UsersData]]:
    return session.query(UsersData).all()


def create(session: Session, obj_create: UsersDataCreate) -> UsersData:
    obj_dict = obj_create.model_dump()
    users_data = UsersData(**obj_dict)
    session.add(users_data)
    session.commit()
    session.refresh(users_data)
    return users_data


def update(session: Session, obj: UsersData,
           obj_update: UsersDataUpdate) -> UsersData:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: UsersData) -> UsersData:
    session.delete(obj)
    session.commit()
    return obj
