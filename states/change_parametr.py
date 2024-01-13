from aiogram.dispatcher.filters.state import StatesGroup, State


class Change_States(StatesGroup):
    STATE_1 = State()
    CONFIRMATION = State()


class Change_States_cont_user(StatesGroup):
    STATE_1 = State()
    CONFIRMATION = State()
