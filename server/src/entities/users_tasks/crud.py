from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Users_Task
from src.entities.users_tasks.model import (
    UsersTaskCreate, UsersTaskUpdate)


def get_one(session: Session, obj_id: int) -> Optional[Users_Task]:
    return session.query(Users_Task).where(Users_Task.id == obj_id).first()


def get_all(session: Session) -> List[Type[Users_Task]]:
    return session.query(Users_Task).all()


def get_user_tasks(session: Session, user_id: int) -> List[Type[Users_Task]]:
    '''
    Получить все прорешанные задания пользователя по user_id.
    '''
    return session.query(Users_Task).where(Users_Task.user_id == user_id).all()


def get_task_users(session: Session,
                   task_id: int) -> List[Type[Users_Task]]:
    '''
    Получить всех пользователей, которые прорешали задание task_id.
    '''
    return session.query(Users_Task).where(Users_Task.task_id == task_id).all()


def create(session: Session, obj_create: UsersTaskCreate) -> Users_Task:
    obj_dict = obj_create.model_dump()
    user_task = Users_Task(**obj_dict)
    session.add(user_task)
    session.commit()
    session.refresh(user_task)
    return user_task


def update(session: Session, obj: Users_Task,
           obj_update: UsersTaskUpdate) -> Users_Task:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Users_Task) -> Users_Task:
    session.delete(obj)
    session.commit()
    return obj
