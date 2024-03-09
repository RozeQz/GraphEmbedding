from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.results import crud
from server.src.entities.results.model import ResultCreate, ResultUpdate

from server.configs.database import get_session


router = APIRouter(tags=["Results"], prefix="/planared/results")

###
