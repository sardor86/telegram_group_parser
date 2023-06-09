from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery

from models import Words


async def get_all_words(callback: CallbackQuery) -> None:
    message = ''
    for word in await Words().get_all_words():
        message += word.words + '\n'

    if message == '':
        message = 'нету'

    await callback.message.reply(message)


def register_get_all_words(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(get_all_words,
                                       lambda callback: callback.data == 'get_all_words')
