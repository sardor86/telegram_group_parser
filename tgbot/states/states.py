from aiogram.dispatcher.filters.state import StatesGroup, State


class AddGroup(StatesGroup):
    get_group = State()


class DeleteGroup(StatesGroup):
    get_group = State()
