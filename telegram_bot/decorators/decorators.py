from aiogram.types import Message
from functools import wraps
from typing import Any

def private_message(func):

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        message: Message = args[0]
        if message.chat.type == "private":
            await func(*args, **kwargs)

    return wrapper