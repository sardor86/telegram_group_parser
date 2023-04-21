from dataclasses import dataclass
from environs import Env
from gino import Gino

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
class Config:
    db: DataBase
    tgbot: TGBot
    parser: Parser


async def set_gino(data_base: DataBase) -> None:
    await gino_db.set_bind(f'postgresql://{data_base.user}:'
                           f'{data_base.password}@'
                           f'{data_base.host}:5432/'
                           f'{data_base.name}')


async def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)

    config = Config(
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
                                ),

                    parser=Parser(
                                  api_id=env.int('API_ID'),
                                  api_hash=env.str('API_HASH'),
                                 )
                    )

    await set_gino(config.db)
    return config
