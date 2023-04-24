from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from config import load_tg_config, path, set_gino
from tgbot.filters import register_all_filters
from tgbot.headers import register_all_handlers
from models import create_all_db


async def main():
    config = load_tg_config(str(path / '.env'))
    await set_gino(config.db)
    await create_all_db()

    storage = MemoryStorage()
    bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_filters(dp)

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')

