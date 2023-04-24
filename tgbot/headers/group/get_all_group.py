from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery

from models import Groups


async def get_all_group(callback: CallbackQuery) -> None:
    message = ''
    for group in await Groups().get_all_group():
        message += group.group_link + '\n'

    if message == '':
        message = 'нету'

    await callback.message.reply(message)


def register_get_all_group(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(get_all_group,
                                       lambda callback: callback.data == 'get_all_group')
