from aiogram.dispatcher.filters.state import StatesGroup, State

class start_s(StatesGroup):
    start = State()

class States(StatesGroup):
    big_state = State()
    sec_state = State()
    vid_state = State()
class Test_state(StatesGroup):
    name = State()
    test = State()
    javob = State()
class Admin(StatesGroup):
    kutish = State()
    elon = State()