from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class ButtonText:
    ADD = "Добавить задачу"
    TSK = "Посмотреть задачи"


class CallbackButtonData:
    ADD = "add_cb_data"
    TSK = "tsk_cb_data"


def get_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=ButtonText.ADD)
    builder.button(text=ButtonText.TSK)
    return builder.as_markup(resize_keyboard=True)


def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=ButtonText.TSK, callback_data=CallbackButtonData.TSK)
    return builder.as_markup()
