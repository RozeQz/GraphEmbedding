from sqlalchemy import text

from configs.database import session_factory

with session_factory() as session:
    res = session.execute(text("SELECT VERSION();"))
    print(f"{res.first()=}")
