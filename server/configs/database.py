from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs.settings import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

session_factory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_session():
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
