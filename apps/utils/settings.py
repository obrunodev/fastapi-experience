from decouple import config

APP_VERSION = config("APP_VERSION", default="0.1.0")
DATABASE_URL = config("DATABASE_URL", default="sqlite+aiosqlite:///./test.db")
