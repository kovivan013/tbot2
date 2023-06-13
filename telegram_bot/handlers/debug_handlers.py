from tbot2.telegram_bot.config import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

async def debug_handler(message: Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    await message.answer(text=f"*Перед вами главное меню:*",
                         reply_markup=None,
                         parse_mode="Markdown")

def register_debug_handlers(dp: Dispatcher):
    dp.register_message_handler(
        debug_handler, state=['*']
    )