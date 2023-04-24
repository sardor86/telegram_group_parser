from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.storage import FSMContext

from tgbot.states import AddGroup
from models import Groups


async def start_add_group(callback: CallbackQuery) -> None:
    await AddGroup.get_group.set()
    await callback.message.reply('Отправте сылку на группу/канал')
    await callback.bot.send_message(callback.from_user.id, 'Группа должна быть публичной')


async def get_group_link(message: Message, state: FSMContext) -> None:
    if '@' in message.text:
        group_link = message.text.split('@')[1:]
    else:
        group_link = message.text.split('/')[-1]
    if await Groups().add_group(group_link):
        await message.reply('Группа/Канал добавлена')
    else:
        await message.reply('Группа/Канал существует в базе')
    await state.finish()


def register_add_group_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_add_group,
                                       lambda callback: callback.data == 'add_group')

    dp.register_message_handler(get_group_link,
                                state=AddGroup.get_group)
