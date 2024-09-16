from sqlalchemy import select

from database import new_session, TaskTable
from schemas import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
