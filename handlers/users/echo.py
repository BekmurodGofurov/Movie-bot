from aiogram import types
from loader import dp, bot
from data.database import get_movie
from keyboards.inline.main_keyboards import join

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    id = message.text
    data = get_movie(id)
    channel_id="@tarjima_kinolaruz_1"
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    is_member = chat_member.status=='member' or chat_member.status=='administrator' or chat_member.status=='creator'

    if data:
        if is_member:
            movie_id = data[0]
            title = data[2]
            desciption = data[3]
            await message.answer_video(movie_id, caption=f"{title}\n{desciption}")
        else:
          await message.reply(f"Uzr siz bizning kanalimzga obuna bo'lmagansiz. Biznig kanlga obuna bo'lsangiz yanigi ID lar berib boriladi va siz bu botda to'liq foydalanish huquqiga ega bo'lasiz.", reply_markup=join)      
    else:    
        await message.answer("Siz yuborgan ID orqali hech nima topa olmadik iltimos qyata tekshiring!")

@dp.callback_query_handler(lambda query: query.data == "$check")
async def cancel_query(query: types.CallbackQuery): 
    await query.message.delete()  
    user_id = query.message.from_user.id
    channel_id="@tarjima_kinolaruz_1"

    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    is_member = chat_member.status=='member' or chat_member.status=='administrator' or chat_member.status=='creator'
    if is_member:
        await query.message.answer(f"Bizning kanlga obuna bo'lganingizda judayam hursandmiz😊\nBotga kino ID ingizni yuboring!")

    else:
        await query.message.reply(f"Uzr siz bizning kanalimzga obuna bo'lmagansiz. Biznig kanlga obuna bo'lsangiz yanigi ID lar berib boriladi va siz bu botda to'liq foydalanish huquqiga ega bo'lasiz.", reply_markup=join)      
