from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.models.models import User
from src.models.users.schemas import UserCreate, UserUpdate


def get_user(session: Session, user_id: int) -> Optional[User]:
    return session.query(User).where(User.id == user_id).first()


def get_users(session: Session) -> List[Type[User]]:
    return session.query(User).all()


def create_user(session: Session, user_in: UserCreate) -> User:
    user_in_dict = user_in.model_dump()
    # user_in_dict["password"] = auth.hash_password(user_in_dict["password"]).decode()
    user = User(**user_in_dict)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user(session: Session, user: User,
                user_update: UserUpdate) -> User:
    for name, value in user_update.model_dump().items():
        setattr(user, name, value)
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, user: User) -> User:
    session.delete(user)
    session.commit()
    return user
