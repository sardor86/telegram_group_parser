from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.states import AddWords
from models import Words


async def start_add_word(callback: CallbackQuery) -> None:
    await AddWords.get_word.set()
    await callback.message.reply('Отпарвте ключевое слово')


async def get_word(message: Message, state: FSMContext) -> None:
    if await Words().add_word(message.text):
        await message.reply('Слово добавлено')
    else:
        await message.reply('Слово сущесвует')
    await state.finish()


def register_add_word_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_add_word,
                                       lambda callback: callback.data == 'add_words')

    dp.register_message_handler(get_word,
                                state=AddWords.get_word)
