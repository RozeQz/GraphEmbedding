from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Users_Topic
from src.entities.users_topics.model import (
    UsersTopicCreate, UsersTopicUpdate)


def get_one(session: Session, obj_id: int) -> Optional[Users_Topic]:
    return session.query(Users_Topic).where(Users_Topic.id == obj_id).first()


def get_all(session: Session) -> List[Type[Users_Topic]]:
    return session.query(Users_Topic).all()


def get_user_topics(session: Session, user_id: int) -> List[Type[Users_Topic]]:
    '''
    Получить все прочитанные темы пользователя по user_id.
    '''
    return session.query(Users_Topic).where(Users_Topic.user_id == user_id).all()


def get_topic_users(session: Session,
                    topic_id: int) -> List[Type[Users_Topic]]:
    '''
    Получить всех пользователей, которые прочитали тему topic_id.
    '''
    return session.query(Users_Topic).where(Users_Topic.topic_id == topic_id).all()


def create(session: Session, obj_create: UsersTopicCreate) -> Users_Topic:
    obj_dict = obj_create.model_dump()
    user_topic = Users_Topic(**obj_dict)
    session.add(user_topic)
    session.commit()
    session.refresh(user_topic)
    return user_topic


def update(session: Session, obj: Users_Topic,
           obj_update: UsersTopicUpdate) -> Users_Topic:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Users_Topic) -> Users_Topic:
    session.delete(obj)
    session.commit()
    return obj
