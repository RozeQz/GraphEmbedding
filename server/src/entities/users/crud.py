from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import User
from src.entities.users.model import UserCreate, UserUpdate


def get_one(session: Session, obj_id: int) -> Optional[User]:
    return session.query(User).where(User.id == obj_id).first()


def get_all(session: Session) -> List[Type[User]]:
    return session.query(User).all()


def get_users_by_role(session: Session, role: str) -> List[Type[User]]:
    return session.query(User).where(User.role == role).all()


def create(session: Session, obj_create: UserCreate) -> User:
    obj_dict = obj_create.model_dump()
    user = User(**obj_dict)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update(session: Session, obj: User,
           obj_update: UserUpdate) -> User:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: User) -> User:
    session.delete(obj)
    session.commit()
    return obj
