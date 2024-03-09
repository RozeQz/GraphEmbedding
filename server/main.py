import uvicorn

from fastapi import FastAPI

from configs.database import session_factory, engine
from server.src.entities.schema import Base
from src.entities.users.controller import router


Base.metadata.create_all(engine)

app = FastAPI(title="PlanarEd API", version="1.0.0")

app.include_router(router=router)

origins = [
    "http://localhost:3000",
]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
