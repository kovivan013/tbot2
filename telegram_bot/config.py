import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
storage = MemoryStorage()
bot = Bot(token=os.getenv("TOKEN_API"))
dp = Dispatcher(bot=bot,
                storage=storage)