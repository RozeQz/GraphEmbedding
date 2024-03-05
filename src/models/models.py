from datetime import datetime
from typing import Any, Dict, Optional

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from sqlalchemy import (
    MetaData,
    text,
    JSON,
    TIMESTAMP,
    ForeignKey
)


class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(autoincrement=True,
                                    primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow
    )


class Users_data(Base):
    __tablename__ = "Users_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    midname: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(nullable=False)


class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    user_data_id: Mapped[int] = mapped_column(
        ForeignKey("Users_data.id", ondelete="CASCADE"),
        nullable=False
    )


class Group(Base):
    __tablename__ = "Groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class Users_Group(Base):
    __tablename__ = "Users_Groups"

    id: Mapped[int] = mapped_column(primary_key=True)
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

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[int] = mapped_column(nullable=False)
    options: Mapped[str] = mapped_column(nullable=False)


class Test(Base):
    __tablename__ = "Tests"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class Tasks_Test(Base):
    __tablename__ = "Tasks_Tests"

    id: Mapped[int] = mapped_column(primary_key=True)
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

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )
    test_id: Mapped[int] = mapped_column(
        ForeignKey("Tests.id"),
        nullable=False
    )
    porint: Mapped[float] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column()
