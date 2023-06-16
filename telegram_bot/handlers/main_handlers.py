from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from tbot2.telegram_bot.config import bot, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.storage import FSMContext
from tbot2.telegram_bot.keyboards.keyboards import StartMenu, StatsMenu, ClassesMenu, PersonalMenu, SettingsMenu
from tbot2.telegram_bot.states.states import MainStates
from tbot2.telegram_bot.decorators.decorators import private_message
from tbot2.telegram_bot.handlers.debug_handlers import debug_handler


async def main_menu(message: Message) -> None:

    await message.answer(text=f"*Главное меню:*",
                         reply_markup=StartMenu.keyboard(),
                         parse_mode="Markdown")


async def classes_menu(message: Message, state: FSMContext) -> None:

    await MainStates.classes_menu_state.set()
    await message.answer(text=f"*У Вас пока нет классов...*",
                         reply_markup=ClassesMenu.keyboard(),
                         parse_mode="Markdown")


async def personal_menu(message: Message, state: FSMContext) -> None:

    await MainStates.personal_menu_state.set()
    await message.answer(text=f"*Здесь пока ничего нет...*",
                         reply_markup=PersonalMenu.keyboard(),
                         parse_mode="Markdown")


async def settings_menu(message: Message, state: FSMContext) -> None:

    await MainStates.settings_menu_state.set()
    await message.answer(text=f"*Здесь пока ничего нет...*",
                         reply_markup=SettingsMenu.keyboard(),
                         parse_mode="Markdown")


async def stats_control(callback: CallbackQuery, state: FSMContext) -> None:

    if callback.data == "back_control_callback":
        StatsMenu.get_v_index -= 5
        await callback.message.edit_reply_markup(reply_markup=StatsMenu.keyboard())
    elif callback.data == "forward_control_callback":
        StatsMenu.get_v_index += 5
        await callback.message.edit_reply_markup(reply_markup=StatsMenu.keyboard())
    elif callback.data == "close_control_callback":
        await debug_handler(message=callback.message, state=state)


async def null_callback(callback: CallbackQuery) -> None:
    await callback.answer(text=f"тест")


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(
        main_menu, commands=["start"], state=None
    )
    dp.register_message_handler(
        classes_menu, Text(equals=StartMenu.student), state=None
    )
    dp.register_message_handler(
        personal_menu, Text(equals=StartMenu.personal), state=None
    )
    dp.register_message_handler(
        settings_menu, Text(equals=StartMenu.settings), state=None
    )
    dp.register_callback_query_handler(
        stats_control, Text(equals="back_control_callback"), state=MainStates.classes_menu_state
    )
    dp.register_callback_query_handler(
        stats_control, Text(equals="forward_control_callback"), state=MainStates.classes_menu_state
    )
    dp.register_callback_query_handler(
        stats_control, Text(equals="close_control_callback"), state=MainStates.classes_menu_state
    )
    dp.register_callback_query_handler(
        null_callback, Text(equals='null'),state=["*"]
    )

# await MainStates.classes_menu_state.set()
#     StatsMenu.get_v_index = 5
#     async with state.proxy() as data:
#         data["global_callback_message"] = await message.answer(text=f"*📊 Ваша успеваемость:*",
#                                                                reply_markup=StatsMenu.keyboard(),
#                                                                parse_mode="Markdown")
