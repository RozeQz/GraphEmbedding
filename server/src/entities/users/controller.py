from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.users import crud
from src.entities.users.model import UserCreate, UserUpdate

from configs.database import get_session


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


@router.get("/", description="Получить всех пользователей \
                              с учетом query параметров")
async def get_users(role: str = None,
                    session: Session = Depends(get_session)):
    if role is not None:
        users = crud.get_users_by_role(session, role)
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Users with {role=} not found",
            )
        return users
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
