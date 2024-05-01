from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from app.models.tasks import Task
from app.schemas.tasks import TaskDTO

DTOSchema = TypeVar("DTOSchema", bound=BaseModel)
DBModel = TypeVar("DBModel", bound=DeclarativeBase)


class IRepo(ABC):
    @abstractmethod
    async def create(self) -> DTOSchema: ...

    @abstractmethod
    async def get_all(self) -> list[DTOSchema]: ...

    @abstractmethod
    async def get(self) -> DTOSchema: ...

    @abstractmethod
    async def update(self) -> list[DTOSchema]: ...

    @abstractmethod
    async def update_one(self) -> DTOSchema: ...

    @abstractmethod
    async def delete(self) -> None: ...


class ISQLRepo(IRepo, Generic[DTOSchema, DBModel]):
    @abstractmethod
    def __init__(self, session, schema: DTOSchema, model: DBModel) -> None: ...

    @abstractmethod
    async def create(self, values: dict) -> DTOSchema | None: ...

    @abstractmethod
    async def get_all(self, **kwargs) -> list[DTOSchema] | None: ...

    @abstractmethod
    async def get(self, pk: UUID | int) -> DTOSchema | None: ...

    @abstractmethod
    async def update(self, values: dict, filters: dict) -> list[DTOSchema] | None: ...

    @abstractmethod
    async def update_one(self, values: dict, pk: UUID | int) -> DTOSchema | None: ...

    @abstractmethod
    async def delete(self, filters: dict) -> None: ...


class ISQLTaskRepo(ISQLRepo[TaskDTO, Task]):

    @abstractmethod
    async def get_all_ordered_by_date(self, **kwargs) -> list[TaskDTO] | None: ...
