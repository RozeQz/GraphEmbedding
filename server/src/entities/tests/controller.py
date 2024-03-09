from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.tests import crud
from server.src.entities.tests.model import TestCreate, TestUpdate

from server.configs.database import get_session


router = APIRouter(tags=["Tests"], prefix="/planared/tests")


@router.post("/", description="Создать тест")
async def create_test(
    test: TestCreate,
    session: Session = Depends(get_session)
):
    return crud.create(session, test)


@router.get("/{test_id}/",
            description="Получить тест по идентификатору")
async def get_test(test_id: int,
                   session: Session = Depends(get_session)):
    test = crud.get_one(session, test_id)

    if not test:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test with {test_id=} not found",
        )

    return test


@router.get("/", description="Получить все тесты")
async def get_tests(session: Session = Depends(get_session)):
    return crud.get_all(session)


@router.delete("/{test_id}/", description="Удалить тест")
async def delete_test(
    test_id: int,
    session: Session = Depends(get_session),
):
    test = crud.get_one(session, test_id)
    if not test:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test with {test_id=} not found",
        )

    return crud.delete(session, test)


@router.put("/{test_id}/", description="Редактировать тест")
async def update_test(
    test_id: int,
    test_update: TestUpdate,
    session: Session = Depends(get_session),
):
    test = crud.get_one(session, test_id)

    if not test:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test with {test_id=} not found",
        )

    return crud.update(session, test, test_update)
