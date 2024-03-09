from sqlalchemy.orm import Session
from typing import List, Optional, Type

from server.src.entities.schema import Result
from server.src.entities.results.model import ResultCreate, ResultUpdate


def get_one(session: Session, obj_id: int) -> Optional[Result]:
    return session.query(Result).where(Result.id == obj_id).first()


def get_all(session: Session) -> List[Type[Result]]:
    return session.query(Result).all()


def create(session: Session, obj_create: ResultCreate) -> Result:
    obj_dict = obj_create.model_dump()
    result = Result(**obj_dict)
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


def update(session: Session, obj: Result,
           obj_update: ResultUpdate) -> Result:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Result) -> Result:
    session.delete(obj)
    session.commit()
    return obj
