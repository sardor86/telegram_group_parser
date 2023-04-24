from dataclasses import dataclass
from environs import Env
from gino import Gino
from pathlib import Path

path = Path(__file__).parent

gino_db = Gino()


@dataclass
class DataBase:
    host: str
    port: int

    user: str
    password: str

    name: str


@dataclass
class TGBot:
    token: str
    admin: int


@dataclass
class Parser:
    api_id: int
    api_hash: str


@dataclass
class TgConfig:
    db: DataBase
    tgbot: TGBot


@dataclass
class ParserConfig:
    db: DataBase
    parser: Parser


async def set_gino(data_base: DataBase) -> None:
    await gino_db.set_bind(f'postgresql://{data_base.user}:'
                           f'{data_base.password}@'
                           f'{data_base.host}:5432/'
                           f'{data_base.name}')


def load_tg_config(env_path: str) -> TgConfig:
    env = Env()
    env.read_env(env_path)

    return TgConfig(
                    db=DataBase(
                                host=env.str('DB_HOST'),
                                port=env.int('DB_PORT'),

                                user=env.str('DB_USER'),
                                password=env.str('DB_PASSWORD'),

                                name=env.str('DB_NAME')
                                ),

                    tgbot=TGBot(
                                token=env.str('BOT_TOKEN'),
                                admin=env.int('ADMIN_ID')
                                ))


def load_parser_config(env_path: str) -> ParserConfig:
    env = Env()
    env.read_env(env_path)

    return ParserConfig(
                    db=DataBase(
                                host=env.str('DB_HOST'),
                                port=env.int('DB_PORT'),

                                user=env.str('DB_USER'),
                                password=env.str('DB_PASSWORD'),

                                name=env.str('DB_NAME')
                                ),

                    parser=Parser(
                                api_id=env.int('API_ID'),
                                api_hash=env.str('API_HASH')
                                ))