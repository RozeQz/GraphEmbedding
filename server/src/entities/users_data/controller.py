from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.users_data import crud
from server.src.entities.users_data.model import (
    UsersDataCreate, UsersDataUpdate)

from server.configs.database import get_session


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
            detail=f"User's data with {user_id=} not found",
        )

    return user


@router.get("/", description="Получить данных всех пользователей")
async def get_users_data(session: Session = Depends(get_session)):
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
            detail=f"User's data with {user_id=} not found",
        )

    return crud.update(session, user, user_update)
