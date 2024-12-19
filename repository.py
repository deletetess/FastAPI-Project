from sqlalchemy import select

from database import new_session, TasksModel
from schemas import TasksSchema, TaskIDSchema


class TaskRepository:
    @classmethod
    async def create_task(cls, data: TasksSchema) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TasksModel(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all_tasks(cls) -> list[TaskIDSchema]:
        async with new_session() as session:
            select_tasks = select(TasksModel)
            result = await session.execute(select_tasks)
            tasks_ = result.scalars().fetchall()
            tasks = [TaskIDSchema.model_validate(task_model) for task_model in tasks_]
            return tasks