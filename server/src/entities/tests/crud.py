from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Test
from src.entities.tests.model import TestCreate, TestUpdate


def get_one(session: Session, obj_id: int) -> Optional[Test]:
    return session.query(Test).where(Test.id == obj_id).first()


def get_all(session: Session) -> List[Type[Test]]:
    return session.query(Test).all()


def create(session: Session, obj_create: TestCreate) -> Test:
    obj_dict = obj_create.model_dump()
    test = Test(**obj_dict)
    session.add(test)
    session.commit()
    session.refresh(test)
    return test


def update(session: Session, obj: Test,
           obj_update: TestUpdate) -> Test:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Test) -> Test:
    session.delete(obj)
    session.commit()
    return obj
