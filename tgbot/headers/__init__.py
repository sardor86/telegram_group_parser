from aiogram.dispatcher import Dispatcher

from .menu import register_menu_handler


def register_all_handlers(dp: Dispatcher):
    register_menu_handler(dp)
