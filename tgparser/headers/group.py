from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client

from models import Groups, Words, Users


async def check_group(client, message) -> None:

    chat = await client.get_chat(message.chat.id)
    if chat.username is None:
        return

    if await Groups().check_in_db(chat.username):
        for word in message.text.split(' '):
            if await Words().check_in_db(word):
                await Users().add_user(message.from_user.id, message.from_user.username, chat.username)


def register_check_group_handler(app: Client) -> None:
    app.add_handler(MessageHandler(check_group, filters.group))
