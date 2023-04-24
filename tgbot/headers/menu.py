from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.keyboard import inline_menu


async def cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.reply('отменен')


async def menu(message: Message) -> None:
    await message.reply('admin menu',
                        reply_markup=inline_menu())


def register_menu_handler(dp: Dispatcher):
    dp.register_message_handler(menu,
                                commands=['start'],
                                state='*',
                                is_admin=True)
    dp.register_message_handler(cancel,
                                commands=['cancel'],
                                state='*')
