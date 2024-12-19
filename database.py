from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///database.db", echo=True
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class BaseModel(DeclarativeBase):
    pass

class TasksModel(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]

async def create_tables(to_delete: bool = True):
    async with engine.begin() as conn:
        if to_delete:
            await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)