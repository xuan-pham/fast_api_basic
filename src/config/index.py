
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")


config = Config()
