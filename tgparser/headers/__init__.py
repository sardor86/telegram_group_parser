from pyrogram import Client

from .group import register_check_group_handler
from .get_all_message import register_get_all_message_group_handler


def register_all_handler(app: Client) -> None:
    register_check_group_handler(app)
    register_get_all_message_group_handler(app)
