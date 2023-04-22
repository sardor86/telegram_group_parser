from aiogram.dispatcher import Dispatcher
from .admin import AdminFilter


def register_all_filters(dp: Dispatcher) -> None:
    dp.filters_factory.bind(AdminFilter)
