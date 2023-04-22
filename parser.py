import asyncio
from pyrogram import Client

from parser.headers import register_all_handler
from config import load_parser_config, path

config = load_parser_config(str(path / '.env'))

app = Client("my_account", config.parser.api_id, config.parser.api_hash)


async def run_parser():
    async def main():
        async with app:
            register_all_handler(app)

    app.run(main())


if __name__ == '__main__':
    asyncio.run(run_parser())

