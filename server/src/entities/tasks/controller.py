from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.tasks import crud
from src.entities.tasks.model import TaskCreate, TaskUpdate

from configs.database import get_session


router = APIRouter(tags=["Tasks"], prefix="/planared/tasks")


@router.post("/", description="Создать задание")
async def create_test(
    task: TaskCreate,
    session: Session = Depends(get_session)
):
    return crud.create(session, task)


@router.get("/{task_id}/",
            description="Получить задание по идентификатору")
async def get_task(task_id: int,
                   session: Session = Depends(get_session)):
    task = crud.get_one(session, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with {task_id=} not found",
        )

    return task


@router.get("/", description="Получить все задания с учетом query параметров")
async def get_tasks(task_type: int = None,
                    session: Session = Depends(get_session)):
    if task_type is not None:
        return crud.get_by_type(session, task_type)
    return crud.get_all(session)


@router.delete("/{task_id}/", description="Удалить задание")
async def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
):
    task = crud.get_one(session, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with {task_id=} not found",
        )

    return crud.delete(session, task)


@router.put("/{task_id}/", description="Редактировать задание")
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    session: Session = Depends(get_session),
):
    task = crud.get_one(session, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with {task_id=} not found",
        )

    return crud.update(session, task, task_update)
