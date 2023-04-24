from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.states import DeleteWords
from models import Words


async def start_delete_word(callback: CallbackQuery) -> None:
    await DeleteWords.get_word.set()
    await callback.message.reply('Отправте ключево слово')


async def get_word(message: Message, state: FSMContext) -> None:
    if await Words().delete_word(message.text):
        await message.reply('ключвое слово удален')
    else:
        await message.reply('ключевое слово не существует в базе')
    await state.finish()


def register_delete_word_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_delete_word,
                                       lambda callback: callback.data == 'delete_words')

    dp.register_message_handler(get_word,
                                state=DeleteWords.get_word)
