from aiogram.dispatcher.filters.state import State, StatesGroup

class movie_state(StatesGroup):
  movie_id = State()
  title = State()
  description = State()