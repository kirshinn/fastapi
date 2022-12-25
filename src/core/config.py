from starlette.config import Config

config = Config(".env")

DATABASE_URL = "postgresql://" \
               + config("POSTGRES_USER", cast=str, default="") + ":" \
               + config("POSTGRES_PASSWORD", cast=str, default="") + "@" \
               + config("POSTGRES_HOST", cast=str, default="") + "/" \
               + config("POSTGRES_DB", cast=str, default="")
