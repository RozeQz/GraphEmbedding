from sqlalchemy.orm import Session
from typing import List, Optional, Type

from src.entities.schema import Topic
from src.entities.topics.model import TopicCreate, TopicUpdate


def get_one(session: Session, obj_id: int) -> Optional[Topic]:
    return session.query(Topic).where(Topic.id == obj_id).first()


def get_all(session: Session) -> List[Type[Topic]]:
    return session.query(Topic).all()


def create(session: Session, obj_create: TopicCreate) -> Topic:
    obj_dict = obj_create.model_dump()
    topic = Topic(**obj_dict)
    session.add(topic)
    session.commit()
    session.refresh(topic)
    return topic


def update(session: Session, obj: Topic,
           obj_update: TopicUpdate) -> Topic:
    for name, value in obj_update.model_dump().items():
        setattr(obj, name, value)
    session.commit()
    session.refresh(obj)
    return obj


def delete(session: Session, obj: Topic) -> Topic:
    session.delete(obj)
    session.commit()
    return obj
