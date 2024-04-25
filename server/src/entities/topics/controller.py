from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.topics import crud
from src.entities.topics.model import TopicCreate, TopicUpdate

from configs.database import get_session


router = APIRouter(tags=["Topics"], prefix="/planared/topics")


@router.post("/", description="Создать тему")
async def create_topic(
    topic: TopicCreate,
    session: Session = Depends(get_session)
):
    return crud.create(session, topic)


@router.get("/{topic_id}/",
            description="Получить тему по идентификатору")
async def get_topic(topic_id: int,
                    session: Session = Depends(get_session)):
    topic = crud.get_one(session, topic_id)

    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Topic with {topic_id=} not found",
        )

    return topic


@router.get("/", description="Получить все темы")
async def get_topics(session: Session = Depends(get_session)):
    return crud.get_all(session)


@router.delete("/{topic_id}/", description="Удалить тему")
async def delete_group(
    topic_id: int,
    session: Session = Depends(get_session),
):
    topic = crud.get_one(session, topic_id)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Topic with {topic_id=} not found",
        )

    return crud.delete(session, topic)


@router.put("/{topic_id}/", description="Редактировать тему")
async def update_group(
    topic_id: int,
    topic_update: TopicUpdate,
    session: Session = Depends(get_session),
):
    topic = crud.get_one(session, topic_id)

    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Topic with {topic_id=} not found",
        )

    return crud.update(session, topic, topic_update)
