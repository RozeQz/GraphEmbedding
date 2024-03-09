from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from server.src.entities.groups import crud
from server.src.entities.groups.model import GroupCreate, GroupUpdate

from server.configs.database import get_session


router = APIRouter(tags=["Groups"], prefix="/planared/groups")

###
