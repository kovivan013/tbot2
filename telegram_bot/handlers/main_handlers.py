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
    StatsMenu.get_v_index = 5
    async with state.proxy() as data:
        data["global_callback_message"] = await message.answer(text=f"*📊 Ваша успеваемость:*",
                                                               reply_markup=StatsMenu.keyboard(),
                                                               parse_mode="Markdown")

async def stats_control(callback: CallbackQuery, state: FSMContext) -> None:

    if callback.data == "back_control_callback":
        StatsMenu.get_v_index -= 5
        await callback.message.edit_reply_markup(reply_markup=StatsMenu.keyboard())
    elif callback.data == "forward_control_callback":
        StatsMenu.get_v_index += 5
        await callback.message.edit_reply_markup(reply_markup=StatsMenu.keyboard())
    elif callback.data == "close_control_callback":
        await state.finish()
        del_msg = await callback.message.delete()
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"*Перед вами главное меню:*",
                               parse_mode="Markdown",
                               reply_markup=StartMenu.keyboard())

async def null_callback(callback: CallbackQuery) -> None:
    await callback.answer(text=f"тест")

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
    dp.register_callback_query_handler(
        stats_control, Text(equals="close_control_callback"), state=MainStates.my_stats
    )
    dp.register_callback_query_handler(
        null_callback, Text(equals='null'),state=["*"]
    )
