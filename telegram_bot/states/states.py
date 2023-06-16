from aiogram.dispatcher.filters.state import State, StatesGroup

class MainStates(StatesGroup):
    classes_menu_state = State()
    personal_menu_state = State()
    settings_menu_state = State()
