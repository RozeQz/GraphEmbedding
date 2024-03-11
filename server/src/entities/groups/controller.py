from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.groups import crud
from src.entities.groups.model import GroupCreate, GroupUpdate

from configs.database import get_session


router = APIRouter(tags=["Groups"], prefix="/planared/groups")


@router.post("/", description="Создать группу")
async def create_group(
    group: GroupCreate,
    session: Session = Depends(get_session)
):
    return crud.create(session, group)


@router.get("/{group_id}/",
            description="Получить группу по идентификатору")
async def get_group(group_id: int,
                    session: Session = Depends(get_session)):
    group = crud.get_one(session, group_id)

    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Group with {group_id=} not found",
        )

    return group


@router.get("/", description="Получить все группы")
async def get_groups(session: Session = Depends(get_session)):
    return crud.get_all(session)


@router.delete("/{group_id}/", description="Удалить группу")
async def delete_group(
    group_id: int,
    session: Session = Depends(get_session),
):
    group = crud.get_one(session, group_id)
    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Group with {group_id=} not found",
        )

    return crud.delete(session, group)


@router.put("/{group_id}/", description="Редактировать группу")
async def update_group(
    group_id: int,
    group_update: GroupUpdate,
    session: Session = Depends(get_session),
):
    group = crud.get_one(session, group_id)

    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Group with {group_id=} not found",
        )

    return crud.update(session, group, group_update)
