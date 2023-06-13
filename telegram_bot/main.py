from config import bot, dp
from aiogram import executor
from handlers.main_handlers import register_main_handlers
from handlers.debug_handlers import register_debug_handlers

register_main_handlers(dp)
register_debug_handlers(dp)

async def on_startup(_) -> None:
    print("Connecting...\nBot started!")

async def on_shutdown(_) -> None:
    print("Bot shutdown!")

def start_bot() -> None:
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)

if __name__ == "__main__":
    start_bot()