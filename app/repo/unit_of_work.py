from app.database import async_session_maker
from app.interfaces.unit_of_work import IUnitOfWork
from app.models.tasks import Task
from app.repo.tasks import TaskRepo
from app.schemas.tasks import TaskDTO


class UnitOfWork(IUnitOfWork):
    def __init__(self, session_factory=async_session_maker):
        self.session_factory = session_factory

    def __call__(self):
        return self

    async def __aenter__(self):
        self.session = self.session_factory()
        self.task = TaskRepo(
            session=self.session,
            schema=TaskDTO,
            model=Task,
        )

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
