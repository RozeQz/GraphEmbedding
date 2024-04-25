from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.entities.users_topics import crud
from src.entities.users_topics.model import UsersTopicCreate

from configs.database import get_session


router = APIRouter(tags=["UsersTopics"], prefix="/planared/users_topics")


@router.post("/", description="Создать связь пользователь-тема")
async def create_user_topic(
    user_group: UsersTopicCreate, session: Session = Depends(get_session)
):
    return crud.create(session, user_group)


@router.get("/",
            description="Получить все связи пользователь-тема \
                         c учетом query параметров")
async def get_users_topics(user_id: int = None,
                           topic_id: int = None,
                           session: Session = Depends(get_session)):
    if user_id is not None:
        user_topics = crud.get_user_topics(session, user_id)
        if not user_topics:
            return []
        return user_topics
    if topic_id is not None:
        topic_users = crud.get_topic_users(session, topic_id)
        if not topic_users:
            return []
        return topic_users
    return crud.get_all(session)


@router.delete("/{user_topic_id}/",
               description="Удалить связь пользователь-тема")
async def delete_user_topic(
    user_topic_id: int,
    session: Session = Depends(get_session),
):
    user_topic = crud.get_one(session, user_topic_id)

    if not user_topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Link User-Topic with {user_topic_id=} not found",
        )

    return crud.delete(session, user_topic)
