from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.users_data import crud
from src.entities.users_data.model import (
    UsersDataCreate, UsersDataUpdate)

from configs.database import get_session


router = APIRouter(tags=["UsersData"], prefix="/planared/users_data")


@router.post("/", description="Создать данные пользователя")
async def create_user_data(
    user: UsersDataCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user)


@router.get("/{user_id}/",
            description="Получить данные пользователя по идентификатору")
async def get_user_data(user_id: int, session: Session = Depends(get_session)):
    user = crud.get_one(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Users data with {user_id=} not found",
        )

    return user


@router.get("/", description="Получить данные всех пользователей \
                              с учетом query параметров")
async def get_users_data(email: str = None,
                         session: Session = Depends(get_session)):
    if email is not None:
        user = crud.get_by_email(session, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Users data with {email=} not found",
            )
        return user
    return crud.get_all(session)


@router.put("/{user_id}/", description="Редактировать данные пользователя")
async def update_user_data(
    user_id: int,
    user_update: UsersDataUpdate,
    session: Session = Depends(get_session),
):
    user = crud.get_one(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Users data with {user_id=} not found",
        )

    return crud.update(session, user, user_update)
