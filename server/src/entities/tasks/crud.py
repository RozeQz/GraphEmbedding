from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Task
from src.entities.tasks.model import TaskCreate, TaskUpdate


def get_one(session: Session, obj_id: int) -> Optional[Task]:
    return session.query(Task).where(Task.id == obj_id).first()


def get_all(session: Session) -> List[Type[Task]]:
    return session.query(Task).all()


def create(session: Session, obj_create: TaskCreate) -> Task:
    obj_dict = obj_create.model_dump()
    task = Task(**obj_dict)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update(session: Session, obj: Task,
           obj_update: TaskUpdate) -> Task:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Task) -> Task:
    session.delete(obj)
    session.commit()
    return obj
