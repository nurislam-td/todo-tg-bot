import punq

from app.interfaces.unit_of_work import IUnitOfWork
from app.repo.unit_of_work import UnitOfWork

container = punq.Container()
container.register(IUnitOfWork, UnitOfWork)
