import uvicorn

from fastapi import FastAPI

from configs.database import session_factory, engine
from src.entities.schema import Base

from src.entities.users.controller import router as router_users
from src.entities.users_data.controller import router as router_users_data
from src.entities.groups.controller import router as router_groups
from src.entities.users_groups.controller import router as router_users_groups
from src.entities.results.controller import router as router_results
from src.entities.tasks.controller import router as router_tasks
from src.entities.tests.controller import router as router_tests
from src.entities.tasks_tests.controller import router as router_tasks_tests

Base.metadata.create_all(engine)

app = FastAPI(title="PlanarEd API", version="1.0.0")

app.include_router(router=router_users)
app.include_router(router=router_users_data)
app.include_router(router=router_groups)
app.include_router(router=router_users_groups)
app.include_router(router=router_results)
app.include_router(router=router_tasks)
app.include_router(router=router_tests)
app.include_router(router=router_tasks_tests)

origins = [
    "http://localhost:3000",
]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
