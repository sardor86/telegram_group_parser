from aiogram.dispatcher import Dispatcher

from tgbot.headers.menu import register_menu_handler

from tgbot.headers.group.add_group import register_add_group_handler
from tgbot.headers.group.delete_group import register_delete_group_handler
from tgbot.headers.group.get_all_group import register_get_all_group


def register_all_handlers(dp: Dispatcher):
    register_menu_handler(dp)

    register_add_group_handler(dp)
    register_delete_group_handler(dp)
    register_get_all_group(dp)
