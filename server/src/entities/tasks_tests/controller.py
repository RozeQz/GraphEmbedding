from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.tasks_tests import crud
from src.entities.tasks_tests.model import TasksTestCreate, TasksTestUpdate

from configs.database import get_session


router = APIRouter(tags=["TasksTests"], prefix="/planared/tasks_tests")


@router.post("/", description="Создать связь задание-тест")
async def create_task_test(
    task_test: TasksTestCreate, session: Session = Depends(get_session)
):
    return crud.create(session, task_test)


@router.get("/{test_id}/",
            description="Получить список заданий теста")
async def get_test_tasks(test_id: int, session: Session = Depends(get_session)):
    test_tasks = crud.get_test_tasks(session, test_id)

    if not test_tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Test with {test_id=} not found",
        )

    return test_tasks


@router.get("/", description="Получить все связи задание-тест")
async def get_tasks_tests(session: Session = Depends(get_session)):
    return crud.get_all(session)
