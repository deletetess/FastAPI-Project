from pydantic import BaseModel, ConfigDict


class TasksSchema(BaseModel):
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class TaskIDSchema(TasksSchema):
    id: int

class StatusTasks(BaseModel):
    ok: bool = True
    task_id: int