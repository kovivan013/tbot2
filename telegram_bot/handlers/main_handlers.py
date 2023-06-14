from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from tbot2.telegram_bot.config import bot, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from tbot2.telegram_bot.keyboards.keyboards import StartMenu, StatsMenu
from tbot2. telegram_bot.states.states import MainStates

async def start(message: Message) -> None:

    await message.answer(text=f"*Главное меню:*",
                         reply_markup=StartMenu.keyboard(),
                         parse_mode="Markdown")

async def my_stats(message: Message, state: FSMContext) -> None:

    await MainStates.my_stats.set()
    await message.answer(text=f"*📊 Ваша успеваемость:*",
                         reply_markup=StatsMenu.keyboard(),
                         parse_mode="Markdown")

async def stats_control(callback: CallbackQuery, state: FSMContext) -> None:

    if "back" in callback.data:
        await callback.message.edit_reply_markup(reply_markup=StatsMenu.keyboard())
    else:
        pass

def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start, commands=["start"], state=None
    )
    dp.register_message_handler(
        my_stats, Text(equals=StartMenu.marks), state=None
    )
    dp.register_callback_query_handler(
        stats_control, Text(equals="back_control_callback"), state=MainStates.my_stats
    )
    dp.register_callback_query_handler(
        stats_control, Text(equals="forward_control_callback"), state=MainStates.my_stats
    )