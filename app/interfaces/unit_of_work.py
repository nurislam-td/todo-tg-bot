from abc import ABC, abstractmethod
from typing import Type

from app.interfaces.repo import ISQLTaskRepo


class IUnitOfWork(ABC):
    task: Type[ISQLTaskRepo]

    @abstractmethod
    async def __init__(self): ...

    @abstractmethod
    async def __call__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...
