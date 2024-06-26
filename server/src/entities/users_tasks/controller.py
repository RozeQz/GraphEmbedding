from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.users_tasks import crud
from src.entities.users_tasks.model import UsersTaskCreate

from configs.database import get_session


router = APIRouter(tags=["UsersTasks"], prefix="/planared/users_tasks")


@router.post("/", description="Создать связь пользователь-задание")
async def create_user_task(
    user_task: UsersTaskCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user_task)


@router.get("/",
            description="Получить все связи пользователь-задание \
                         c учетом query параметров")
async def get_users_tasks(user_id: int = None,
                          task_id: int = None,
                          session: Session = Depends(get_session)):
    if user_id is not None:
        user_tasks = crud.get_user_tasks(session, user_id)
        if not user_tasks:
            return []
        return user_tasks
    if task_id is not None:
        task_users = crud.get_task_users(session, task_id)
        if not task_users:
            return []
        return task_users
    return crud.get_all(session)


@router.delete("/{user_task_id}/",
               description="Удалить связь пользователь-группа")
async def delete_user_task(
    user_task_id: int,
    session: Session = Depends(get_session),
):
    user_task = crud.get_one(session, user_task_id)

    if not user_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Link User-Task with {user_task_id=} not found",
        )

    return crud.delete(session, user_task)
