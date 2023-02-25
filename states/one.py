from aiogram.dispatcher.filters.state import StatesGroup, State


class Type(StatesGroup):
    type1 = State()
    type2 = State()
    type3 = State()
    type4 = State()
    type5 = State()
    type6 = State()
    type7 = State()
    type8 = State()

class Panel(StatesGroup):
    stat = State()
    reklama = State()
    majburiy = State()