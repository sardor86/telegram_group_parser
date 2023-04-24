from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client

from models import Groups, Words, Users


async def check_channels(client, message) -> None:
    chat = await client.get_chat(message.chat.id)
    if chat.username is None:
        return

    if await Groups().check_in_db(chat.username):
        for word in message.text.split(' '):
            if await Words().check_in_db(word):
                if await Users().add_user(chat.id, chat.username, chat.username):
                    await client.send_message('me',
                                              f'{message.from_user.id}  |  '
                                              f'{message.from_user.username}  |  '
                                              f'{chat.username}'
                                              f'{message.date}')


def register_check_channels_handler(app: Client) -> None:
    app.add_handler(MessageHandler(check_channels, filters.channel))
