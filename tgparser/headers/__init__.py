from pyrogram import Client

from .group import register_check_group_handler
from .channels import register_check_channels_handler
from .get_all_message import register_get_all_message_group_handler


def register_all_handler(client: Client) -> None:
    register_check_group_handler(client)
    register_check_channels_handler(client)
    register_get_all_message_group_handler(client)
