from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.tasks_tests import crud
from server.src.entities.tasks_tests.model import TasksTestCreate, TasksTestUpdate

from server.configs.database import get_session


router = APIRouter(tags=["TasksTests"], prefix="/planared/tasks_tests")

###
