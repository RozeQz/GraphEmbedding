from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Result
from src.entities.results.model import ResultCreate, ResultUpdate


def get_one(session: Session, obj_id: int) -> Optional[Result]:
    return session.query(Result).where(Result.id == obj_id).first()


def get_all(session: Session) -> List[Type[Result]]:
    return session.query(Result).all()


def get_user_results(session: Session, user_id: int) -> List[Type[Result]]:
    '''
    Получить все результаты пользователя по user_id.
    '''
    return session.query(Result).where(Result.user_id == user_id).all()


def get_test_results(session: Session, test_id: int) -> List[Type[Result]]:
    '''
    Получить все результаты теста по test_id.
    '''
    return session.query(Result).where(Result.test_id == test_id).all()


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
