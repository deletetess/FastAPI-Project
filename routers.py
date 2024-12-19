from fastapi import APIRouter, Depends
from schemas import TasksSchema, StatusTasks
from typing import Annotated

from repository import TaskRepository

task_router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)

@task_router.get("/", name="Получение задач")
async def get_tasks() -> list[TasksSchema]:
    all_tasks = await TaskRepository.get_all_tasks()
    return all_tasks

@task_router.post("/", name="Добавление задачи")
async def add_task(task: Annotated[TasksSchema, Depends()]) -> StatusTasks:
    add_task = await TaskRepository.create_task(task)
    return StatusTasks(ok=True, task_id=add_task)