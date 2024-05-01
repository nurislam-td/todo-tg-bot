from typing import cast

from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils import markdown

from app.di_container import container
from app.handlers.keyboards import (
    ButtonText,
    CallbackButtonData,
    get_inline_keyboard,
    get_main_keyboard,
)
from app.interfaces.unit_of_work import IUnitOfWork
from app.schemas.tasks import TaskCreate, TaskDTO
from app.services.tasks import add_task, get_tasks

router = Router(name="tasks")


class AddState(StatesGroup):
    title = State()
    description = State()


@router.message(F.text == ButtonText.ADD)
@router.message(Command("add"))
async def handle_add(message: types.Message, state: FSMContext):
    await state.set_state(AddState.title)
    await message.answer(
        "Введите заголовок задачи:", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(AddState.title)
async def add_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(AddState.description)
    await message.answer("Введите описание задачи:")


@router.message(AddState.description)
async def add_descr(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    uow = cast(IUnitOfWork, container.resolve(IUnitOfWork))
    task_in = TaskCreate(title=data["title"], description=data["description"])
    await add_task(uow, task_in)
    await state.clear()
    await message.answer(
        text=f'Круто, задача "{task_in.title}" была добавлена.\n'
        "Желаете посмотреть свои задачи?",
        reply_markup=get_inline_keyboard(),
    )


@router.message(F.text == ButtonText.TSK)
@router.message(Command("tsk"))
async def handle_tsk(message: types.Message):
    uow = cast(IUnitOfWork, container.resolve(IUnitOfWork))
    tasks = await get_tasks(uow)
    await output_tasks(message=message, tasks=tasks)


@router.callback_query(F.data == CallbackButtonData.TSK)
async def handle_callback_tsk(callback_query: types.CallbackQuery):
    await callback_query.answer()
    uow = cast(IUnitOfWork, container.resolve(IUnitOfWork))
    tasks = await get_tasks(uow)
    await output_tasks(message=callback_query.message, tasks=tasks)


async def output_tasks(message: types.Message, tasks: list[TaskDTO]):
    for task in tasks:
        await message.answer(
            f"📍 <b>Задача: {task.title}</b>\n\n<b>📜 Описание:</b>\n{task.description}\n\n",
            parse_mode=ParseMode.HTML,
            reply_markup=get_main_keyboard(),
        )
