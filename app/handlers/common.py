from aiogram import Router, types
from aiogram.filters import Command, CommandStart

from app.handlers.keyboards import get_main_keyboard

router = Router(name="common")


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.full_name}.\nЧто я могу сделать для тебя ?",
        reply_markup=get_main_keyboard(),
    )


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(
        """Вот что я умею:\n/add - добавить задачу в "список задач"\n/tsk - вывести "список задач" """
    )
