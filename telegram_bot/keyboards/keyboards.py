from typing import Union
from math import ceil
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
        row_width=1
    )

@dataclass(frozen=True)
class StartMenu:

    student: str = "👨‍🎓 Мои классы"
    personal: str = "👨‍🏫 Личный кабинет"
    settings: str = "⚙️ Настройки"

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(text=cls.student),
            KeyboardButton(text=cls.personal),
            KeyboardButton(text=cls.settings)
        )

        return keyboard

class ClassesMenu:

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = default_inline_keyboard()

        keyboard.add(
            InlineKeyboardButton(text="✚ Добавить класс",
                                 callback_data="classesmenu_add_class_callback"),
            InlineKeyboardButton(text="🔗 Воспользоваться ссылкой-приглашением",
                                 callback_data="classesmenu_link_callback")
        )

        return keyboard

class PersonalMenu:

    coming_soon: str = "🔥 Скоро..."

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(text=cls.coming_soon)
        )

        return keyboard


class SettingsMenu:
    coming_soon: str = "🔥 Скоро..."

    @classmethod
    def keyboard(cls) -> Union[ReplyKeyboardMarkup]:
        keyboard = default_keyboard()

        keyboard.add(
            KeyboardButton(text=cls.coming_soon)
        )

        return keyboard

@dataclass(frozen=True)
class StatsMenu:

    keyboard_width: int = 5
    get_v_index: int = keyboard_width

    @classmethod
    def keyboard(cls) -> Union[InlineKeyboardMarkup]:
        keyboard = InlineKeyboardMarkup(row_width=cls.keyboard_width)

        page: int = cls.get_v_index / cls.keyboard_width
        marks_list: list = [11,8,10,9,7,9]
        page_rem: int = ceil(len(marks_list) / cls.keyboard_width)
        marks_dict: dict = dict.fromkeys(range(1, len(marks_list)+1), None)

        for i, v in marks_dict.items():
            marks_dict[i] = marks_list[i - 1]

        try:
            keyboard.add(
                InlineKeyboardButton(text=marks_dict[cls.get_v_index - 4], callback_data="null"),
                InlineKeyboardButton(text=marks_dict[cls.get_v_index - 3], callback_data="null"),
                InlineKeyboardButton(text=marks_dict[cls.get_v_index - 2], callback_data="null"),
                InlineKeyboardButton(text=marks_dict[cls.get_v_index - 1], callback_data="null"),
                InlineKeyboardButton(text=marks_dict[cls.get_v_index], callback_data="null")
            )
        except KeyError:
            try:
                keyboard.add(
                    InlineKeyboardButton(text=marks_dict[cls.get_v_index - 4], callback_data="null"),
                    InlineKeyboardButton(text=marks_dict[cls.get_v_index - 3], callback_data="null"),
                    InlineKeyboardButton(text=marks_dict[cls.get_v_index - 2], callback_data="null"),
                    InlineKeyboardButton(text=marks_dict[cls.get_v_index - 1], callback_data="null")
                )
            except KeyError:
                try:
                    keyboard.add(
                        InlineKeyboardButton(text=marks_dict[cls.get_v_index - 4], callback_data="null"),
                        InlineKeyboardButton(text=marks_dict[cls.get_v_index - 3], callback_data="null"),
                        InlineKeyboardButton(text=marks_dict[cls.get_v_index - 2], callback_data="null")
                    )
                except KeyError:
                    try:
                        keyboard.add(
                            InlineKeyboardButton(text=marks_dict[cls.get_v_index - 4], callback_data="null"),
                            InlineKeyboardButton(text=marks_dict[cls.get_v_index - 3], callback_data="null")
                        )
                    except KeyError:
                        try:
                            keyboard.add(
                                InlineKeyboardButton(text=marks_dict[cls.get_v_index - 4], callback_data="null")
                            )
                        except:
                            pass

        if page == 1 and page_rem == 1:
            keyboard.add(
                InlineKeyboardButton(text=f"Закрыть ✖",
                                     callback_data="close_control_callback")
            )
        else:
            if page == 1:
                keyboard.add(
                    InlineKeyboardButton(text=f"Закрыть ✖",
                                         callback_data="close_control_callback"),
                    InlineKeyboardButton(text="Вперёд ▶",
                                         callback_data="forward_control_callback")
                )
            elif page == page_rem:
                keyboard.add(
                    InlineKeyboardButton(text="◀ Назад",
                                         callback_data="back_control_callback"),
                    InlineKeyboardButton(text=f"Закрыть ✖",
                                         callback_data="close_control_callback")
                )
            else:
                keyboard.add(
                    InlineKeyboardButton(text="◀ Назад",
                                         callback_data="back_control_callback"),
                    InlineKeyboardButton(text=f"Закрыть ✖",
                                         callback_data="close_control_callback"),
                    InlineKeyboardButton(text="Вперёд ▶",
                                         callback_data="forward_control_callback")
                )

        return keyboard
