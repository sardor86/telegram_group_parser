from pyrogram import Client

from .group import register_check_group_handler


def register_all_handler(app: Client) -> None:
    register_check_group_handler(app)
