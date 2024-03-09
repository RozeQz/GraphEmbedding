from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.users import crud
from server.src.entities.users.model import UserCreate, UserUpdate

from server.configs.database import get_session


router = APIRouter(tags=["Users"], prefix="/planared/users")


@router.post("/", description="Создать пользователя")
async def create_user(
    user: UserCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user)


@router.get("/{user_id}/",
            description="Получить пользователя по идентификатору")
async def get_user(user_id: int, session: Session = Depends(get_session)):
    user = crud.get_one(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user_id=} not found",
        )

    return user


@router.get("/", description="Получить всех пользователей")
async def get_users(session: Session = Depends(get_session)):
    return crud.get_all(session)


@router.delete("/{user_id}/", description="Удалить пользователя")
async def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = crud.get_one(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user_id=} not found",
        )

    return crud.delete(session, user)


@router.put("/{user_id}/", description="Редактировать пользователя")
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session),
):
    user = crud.get_one(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user_id=} not found",
        )

    return crud.update(session, user, user_update)
