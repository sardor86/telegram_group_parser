from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client

from models import Groups, Words, Users


async def get_all_message_group(client, message) -> None:
    if not message.text == '!get_all_message!':
        return

    for chat in await Groups().get_all_group():
        chat = await client.get_chat(chat.group_link)
        if str(chat.type) == 'ChatType.CHANNEL':
            chat_id = chat.linked_chat.id
        else:
            chat_id = chat.id

        for word in await Words().get_all_words():
            async for history_message in client.search_messages(chat_id, query=word.words, limit=5000):
                try:
                    await Users().add_user(history_message.from_user.id, history_message.from_user.username, chat.username)
                except AttributeError:
                    pass

    await message.reply('Парсинг старых сообщений закончен')


def register_get_all_message_group_handler(app: Client) -> None:
    app.add_handler(MessageHandler(get_all_message_group, filters.me))
