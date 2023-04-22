from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client


async def check_group(client, message):
    print(message)


def register_check_group_handler(app: Client) -> None:
    app.add_handler(MessageHandler(check_group, filters.group_filter))
