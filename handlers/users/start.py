from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from data.config import ADMINS
from data.database import add_user, get_user
from keyboards.inline.main_keyboards import start_001


@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
  user_id = message.from_user.id
  name = message.from_user.full_name
  username = f"@{message.from_user.username}"
  user = get_user(user_id)
  if user_id == ADMINS:
    await message.reply(f'Salom Admin ✋\n\nKino qoshishni hoxlaysizmi❓', reply_markup=start_001)
  else:
    if user:
      await message.reply(f'Assalomu alaykum {message.chat.first_name} \nBotimizga qaytib kelganingizdan hursandmiz.\nIltimos kino IDsini yuboring.')

    else:
      add_user(user_id, name, username)
      await message.reply(f'Assalomu alaykum {message.chat.first_name} \nFull & Quality Movies botga hush kelibsiz.\nIltimos kino IDsini yuboring.')
