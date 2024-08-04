from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from data.database import *
from states.movie import movie_state
from keyboards.inline.main_keyboards import add_button, save_data, start_001

# Echo bot
@dp.callback_query_handler(lambda query: query.data == "$add_movie")
async def bot_echo(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    await query.message.answer("Menga kinoni yuboring")
    await movie_state.movie_id.set()

@dp.message_handler(content_types=["video"], state=movie_state.movie_id)
async def get_movie_id(message: types.Message, state: FSMContext):
    movie_id = message.video.file_id
    await state.update_data(movie_id=movie_id)
    await message.answer_video(movie_id)
    await message.answer(f"Menga kino nomini yuboring!")
    await movie_state.title.set()

@dp.message_handler(state=movie_state.title)
async def get_title(messge: types.Message, state: FSMContext):
    title = messge.text
    await state.update_data(title=title)
    await messge.reply(f"Kino haqida ozgana malumot qoldiring (yili, nima haqida...)")
    await movie_state.description.set()

@dp.message_handler(state=movie_state.description)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    data = await state.get_data()
    movie_id = data.get('movie_id')
    title = data.get('title')
    await message.answer_video(movie_id, caption=f"{title}\n\n{description}")
    await message.answer(f"Kino va uning malumotlarini saqlashni hoxlaysizmi❓", reply_markup=save_data)

#   Callback Query

@dp.callback_query_handler(lambda query: query.data == "$cancel", state="*")
async def cancel_query(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    await state.reset_state(with_data=True)
    await query.message.answer(f'Kino malumotlari salanmadi')
    await query.message.answer(f"Kino qo'shishni hoxlaysizmi", reply_markup=start_001)

@dp.callback_query_handler(lambda query: query.data == "$save", state="*")
async def cancel_query(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    data = await state.get_data()
    movie_id = data.get('movie_id')
    random_id = movie_id[-15:]
    title = data.get('title')
    description = data.get('description') 
    add_movie(movie_id, random_id, title, description)

    await query.message.answer(f"Tabriklayman😊 \nSizning kinoingiz muvaffaqiyatli saqlandi❕\n\nKinoni IDsi ``{random_id}``\n\nIltimos buni saqlab qoying❕")
    await query.message.answer(f"Yana kino qo'shishni hoxlaysizmi❓", reply_markup=start_001)