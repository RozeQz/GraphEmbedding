from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.users_groups import crud
from src.entities.users_groups.model import UsersGroupCreate

from configs.database import get_session


router = APIRouter(tags=["UsersGroups"], prefix="/planared/users_groups")


@router.post("/", description="Создать связь пользователь-группа")
async def create_user_group(
    user_group: UsersGroupCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user_group)


@router.get("/",
            description="Получить все связи пользователь-группа \
                         c учетом query параметров")
async def get_users_groups(user_id: int = None,
                           group_id: int = None,
                           session: Session = Depends(get_session)):
    if user_id is not None:
        user_groups = crud.get_user_groups(session, user_id)
        if not user_groups:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with {user_id=} not found",
            )
        return user_groups
    if group_id is not None:
        group_users = crud.get_group_users(session, group_id)
        if not group_users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Group with {group_id=} not found",
            )
        return group_users
    return crud.get_all(session)


@router.delete("/{user_group_id}/",
               description="Удалить связь пользователь-группа")
async def delete_user_group(
    user_group_id: int,
    session: Session = Depends(get_session),
):
    user_group = crud.get_one(session, user_group_id)

    if not user_group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Link User-Group with {user_group_id=} not found",
        )

    return crud.delete(session, user_group)
