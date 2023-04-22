from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.states import AddGroup
from models import Groups


async def start_add_group(callback: CallbackQuery) -> None:
    await AddGroup.get_group.set()
    await callback.message.edit_text('Отправте сылку на группу')


async def get_group_link(message: Message, state: FSMContext) -> None:
    if await Groups().add_group(message.text):
        await message.reply('Группа добавлена')
    else:
        await message.reply('Группа существует в базе')
    await state.finish()


def register_add_group_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_add_group,
                                       lambda callback: callback.data == 'add_group')

    dp.register_message_handler(get_group_link,
                                state=AddGroup.get_group)
