from tbot2.telegram_bot.config import Dispatcher
from aiogram.types import Message
from tbot2.telegram_bot.keyboards.keyboards import StartMenu
from aiogram.dispatcher.storage import FSMContext

async def debug_handler(message: Message, state: FSMContext) -> None:

    async with state.proxy() as data:
        try:
            await data["global_callback_message"].delete()
        except:
            pass

    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    await message.answer(text=f"*Перед вами главное меню:*",
                         reply_markup=StartMenu.keyboard(),
                         parse_mode="Markdown")

def register_debug_handlers(dp: Dispatcher):
    dp.register_message_handler(
        debug_handler, state=['*']
    )