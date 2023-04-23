import asyncio

from pyrogram import Client

from config import load_parser_config, path, set_gino
from tgparser.headers import register_all_handler

config = load_parser_config(str(path / '.env'))


async def set_db():
    await set_gino(config.db)


def main() -> None:
    client = Client(name='telegram_group_parses', api_id=config.parser.api_id, api_hash=config.parser.api_hash)

    register_all_handler(client)

    client.run()


def start_parser():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(set_db())
    loop.run_until_complete(asyncio.wait([task1]))
    main()


if __name__ == '__main__':
    start_parser()
