from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from database import create_tables
from routers import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables(to_delete=True)
    yield
    print("Выключение")
app = FastAPI(lifespan=lifespan)

app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app")
