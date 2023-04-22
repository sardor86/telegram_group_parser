from aiogram.dispatcher import Dispatcher

from tgbot.headers.menu import register_menu_handler

from tgbot.headers.group.add_group import register_add_group_handler
from tgbot.headers.group.delete_group import register_delete_group_handler
from tgbot.headers.group.get_all_group import register_get_all_group

from tgbot.headers.words.add_words import register_add_word_handler
from tgbot.headers.words.delete_word import register_delete_word_handler
from tgbot.headers.words.get_all_words import register_get_all_words


def register_all_handlers(dp: Dispatcher):
    register_menu_handler(dp)

    register_add_group_handler(dp)
    register_delete_group_handler(dp)
    register_get_all_group(dp)

    register_add_word_handler(dp)
    register_delete_word_handler(dp)
    register_get_all_words(dp)
