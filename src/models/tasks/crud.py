from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.models.models import Task
from src.models.tasks.schemas import TaskCreate, TaskUpdate


def get_task(session: Session, task_id: int) -> Optional[Task]:
    return session.query(Task).where(Task.id == task_id).first()


def get_tasks(session: Session) -> List[Type[Task]]:
    return session.query(Task).all()


def create_tasks(session: Session, task_in: TaskCreate) -> Task:
    task_in_dict = task_in.model_dump()
    task = Task(**task_in_dict)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_user(session: Session, task: Task,
                task_update: TaskUpdate) -> Task:
    for name, value in task_update.model_dump().items():
        setattr(task, name, value)
    session.commit()
    session.refresh(task)
    return task


def delete_user(session: Session, task: Task) -> Task:
    session.delete(task)
    session.commit()
    return task
