from app.interfaces.unit_of_work import IUnitOfWork
from app.schemas.tasks import TaskCreate, TaskDTO


async def add_task(uow: IUnitOfWork, task_in: TaskCreate):
    async with uow:
        await uow.task.create(values=task_in.model_dump())
        await uow.commit()


async def get_tasks(uow: IUnitOfWork) -> list[TaskDTO]:
    async with uow:
        tasks = await uow.task.get_all_ordered_by_date()
        return tasks
