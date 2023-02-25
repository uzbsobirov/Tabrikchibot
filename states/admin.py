from aiogram.dispatcher.filters.state import State, StatesGroup

# For `Xabar yuborish`
class SendMessage(StatesGroup):
    message = State()

# <----------Majburiy obuna---------->
class AddSponsor(StatesGroup):
    username = State()

class DeleteSponsor(StatesGroup):
    username = State()