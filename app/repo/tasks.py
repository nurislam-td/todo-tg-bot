from typing import override

from sqlalchemy import select

from app.models.tasks import Task
from app.repo.base import SQLAlchemyRepo
from app.schemas.tasks import TaskDTO


class TaskRepo(SQLAlchemyRepo[TaskDTO, Task]):
    @override
    async def get_all_ordered_by_date(self) -> list[TaskDTO]:
        query = select(self._model.__table__).order_by(
            self._model.__table__.c.created_at.desc()
        )
        return await self.fetch_all(query)
