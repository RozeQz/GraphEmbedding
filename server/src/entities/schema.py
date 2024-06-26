'''
Схема базы данных.
'''

from datetime import datetime
import enum

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
    declared_attr
)

from sqlalchemy import (
    text,
    ForeignKey,
    Column
)

from sqlalchemy.dialects.postgresql import JSONB


class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(autoincrement=True,
                                    unique=True,
                                    nullable=False,
                                    primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow
    )


class UsersData(Base):
    __tablename__ = "Users_data"

    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    midname: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)


class Role(enum.Enum):
    student = "student"
    teacher = "teacher"


class User(Base):
    __tablename__ = "Users"

    login: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role:  Mapped[Role] = mapped_column(nullable=False)
    user_data_id: Mapped[int] = mapped_column(
        ForeignKey("Users_data.id", ondelete="CASCADE"),
        nullable=False
    )


class Group(Base):
    __tablename__ = "Groups"

    name: Mapped[str] = mapped_column(nullable=False)


class Users_Group(Base):
    __tablename__ = "Users_Groups"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey("Groups.id"),
        nullable=False
    )


class Task(Base):
    __tablename__ = "Tasks"

    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[int] = mapped_column(nullable=False)
    options: Mapped[str] = mapped_column(nullable=False)


class Users_Task(Base):
    __tablename__ = "Users_Tasks"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("Tasks.id"),
        nullable=False
    )


class Test(Base):
    __tablename__ = "Tests"

    name: Mapped[str] = mapped_column(nullable=True)


class Tasks_Test(Base):
    __tablename__ = "Tasks_Tests"

    test_id: Mapped[int] = mapped_column(
        ForeignKey("Tests.id"),
        nullable=False
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("Tasks.id"),
        nullable=False
    )


class Result(Base):
    __tablename__ = "Results"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )
    test_id: Mapped[int] = mapped_column(
        ForeignKey("Tests.id"),
        nullable=False
    )
    points: Mapped[float] = mapped_column(nullable=False)
    answers = Column(JSONB, nullable=True)
    time_spent:  Mapped[int] = mapped_column(nullable=True)


class Topic(Base):
    __tablename__ = "Topics"

    title: Mapped[str] = mapped_column(nullable=False)
    file_name: Mapped[str] = mapped_column(nullable=True)


class Users_Topic(Base):
    __tablename__ = "Users_Topics"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )
    topic_id: Mapped[int] = mapped_column(
        ForeignKey("Topics.id"),
        nullable=False
    )
