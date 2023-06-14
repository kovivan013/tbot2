from typing import Union
from toolz import partition
from dataclasses import dataclass
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)

def default_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=2
    )

def default_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        row_width=2
    )

@dataclass(frozen=True)
class ControlsMenu:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(text="« Назад",
                                 callback_data="back_control_callback"),
            InlineKeyboardButton(text="Вперёд »",
                                 callback_data="forward_control_callback")
        )

        return keyboard
@dataclass(frozen=True)
class StartMenu:

    marks: str = "📊 Моя успеваемость"

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(text=cls.marks)
        )

        return keyboard

@dataclass(frozen=True)
class StatsMenu:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = InlineKeyboardMarkup(row_width=5)

        marks_list: list = [11, 12, 10, 9, 9, 8, 12, 7, 9, 5, 8, 5, 8, 11, 5, 7, 11, 8, 5, 11, 8, 11, 10, 7, 11]
        value: int = 1
        index: int = 0
        get_v_index: int = 5
        page: int = get_v_index / 5

        for i in range(0, len(marks_list)):
            marks_list.insert(index, value)
            value += 1
            index += 2

        tpl = list(partition(2, marks_list))
        marks_list.clear()
        [marks_list.append(list(i)) for i in tpl]
        marks_dict = dict(marks_list)

        keyboard.add(
            InlineKeyboardButton(text=marks_dict[get_v_index - 4], callback_data="null"),
            InlineKeyboardButton(text=marks_dict[get_v_index - 3], callback_data="null"),
            InlineKeyboardButton(text=marks_dict[get_v_index - 2], callback_data="null"),
            InlineKeyboardButton(text=marks_dict[get_v_index - 1], callback_data="null"),
            InlineKeyboardButton(text=marks_dict[get_v_index], callback_data="null"),
        )

        if page == 1:
            keyboard.add(
                InlineKeyboardButton(text="Вперёд »",
                                     callback_data="forward_control_callback")
            )
        elif page == 5:
            keyboard.add(
                InlineKeyboardButton(text="« Назад",
                                     callback_data="back_control_callback")
            )
        else:
            keyboard.add(
                InlineKeyboardButton(text="« Назад",
                                     callback_data="back_control_callback"),
                InlineKeyboardButton(text="Вперёд »",
                                     callback_data="forward_control_callback")
            )

        return keyboard
