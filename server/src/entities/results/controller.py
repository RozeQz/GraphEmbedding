from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.results import crud
from src.entities.results.model import ResultCreate, ResultUpdate

from configs.database import get_session


router = APIRouter(tags=["Results"], prefix="/planared/results")


@router.post("/", description="Создать результат")
async def create_user_group(
    user_group: ResultCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user_group)


@router.get("/{user_id}/",
            description="Получить список всех результатов пользователя")
async def get_user_results(user_id: int,
                           session: Session = Depends(get_session)):
    user_results = crud.get_user_results(session, user_id)

    if not user_results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user_id=} not found",
        )

    return user_results


@router.get("/{test_id}/",
            description="Получить список всех результатов теста")
async def get_test_results(test_id: int,
                           session: Session = Depends(get_session)):
    test_results = crud.get_test_results(session, test_id)

    if not test_results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test with {test_id=} not found",
        )

    return test_results


@router.get("/", description="Получить все результаты")
async def get_results(session: Session = Depends(get_session)):
    return crud.get_all(session)


@router.delete("/{result_id}/",
               description="Удалить результат")
async def delete_result(
    result_id: int,
    session: Session = Depends(get_session),
):
    result = crud.get_one(session, result_id)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Result with {result_id=} not found",
        )

    return crud.delete(session, result)
