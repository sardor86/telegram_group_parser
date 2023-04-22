from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from tgbot.keyboard import inline_menu


async def menu(message: Message) -> None:
    await message.reply('admin menu',
                        reply_markup=inline_menu())


def register_menu_handler(dp: Dispatcher):
    dp.register_message_handler(menu,
                                commands=['start'],
                                is_admin=True)
