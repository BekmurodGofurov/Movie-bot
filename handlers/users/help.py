from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
  await message.answer("Ushbu botimizda siz bizning tanlimizda berilayotkan kino IDlari yordamida kinoni tomosha qilishingiz mukin.\n\n/start - Botni qayta ishga tushirish\n\n/help - Yordam olish")
