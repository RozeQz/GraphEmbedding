from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Tasks_Test
from src.entities.tasks_tests.model import (
    TasksTestCreate, TasksTestUpdate)


def get_one(session: Session, obj_id: int) -> Optional[Tasks_Test]:
    return session.query(Tasks_Test).where(Tasks_Test.id == obj_id).first()


def get_all(session: Session) -> List[Type[Tasks_Test]]:
    return session.query(Tasks_Test).all()


def get_test_tasks(session: Session, test_id: int) -> List[Type[Tasks_Test]]:
    '''
    Получить все задания теста по test_id.
    '''
    return session.query(Tasks_Test).where(Tasks_Test.test_id == test_id).all()


def create(session: Session, obj_create: TasksTestCreate) -> Tasks_Test:
    obj_dict = obj_create.model_dump()
    task_test = Tasks_Test(**obj_dict)
    session.add(task_test)
    session.commit()
    session.refresh(task_test)
    return task_test


def update(session: Session, obj: Tasks_Test,
           obj_update: TasksTestUpdate) -> Tasks_Test:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Tasks_Test) -> Tasks_Test:
    session.delete(obj)
    session.commit()
    return obj
