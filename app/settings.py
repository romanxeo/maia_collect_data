import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_HOST = os.getenv('APP_HOST')
    APP_PORT = int(os.getenv('APP_PORT'))

    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')

    DB_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

    PASSWORD = os.getenv('PASSWORD')


settings = Settings()
