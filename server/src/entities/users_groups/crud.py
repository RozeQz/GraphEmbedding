from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Users_Group
from src.entities.users_groups.model import (
    UsersGroupCreate, UsersGroupUpdate)


def get_one(session: Session, obj_id: int) -> Optional[Users_Group]:
    return session.query(Users_Group).where(Users_Group.id == obj_id).first()


def get_all(session: Session) -> List[Type[Users_Group]]:
    return session.query(Users_Group).all()


def get_user_groups(session: Session, user_id: int) -> List[Type[Users_Group]]:
    '''
    Получить все группы пользователя по user_id.
    '''
    return session.query(Users_Group).where(Users_Group.user_id == user_id).all()


def get_group_users(session: Session,
                    group_id: int) -> List[Type[Users_Group]]:
    '''
    Получить всех пользователей группы по group_id.
    '''
    return session.query(Users_Group).where(Users_Group.group_id == group_id).all()


def create(session: Session, obj_create: UsersGroupCreate) -> Users_Group:
    obj_dict = obj_create.model_dump()
    user_group = Users_Group(**obj_dict)
    session.add(user_group)
    session.commit()
    session.refresh(user_group)
    return user_group


def update(session: Session, obj: Users_Group,
           obj_update: UsersGroupUpdate) -> Users_Group:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Users_Group) -> Users_Group:
    session.delete(obj)
    session.commit()
    return obj
