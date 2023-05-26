from aiogram import types, Bot, executor, Dispatcher
from data import TOKEN
from buttons import menuMain, menuPcs, salfetka_back, menuUltra, Ultraback, menuComfort, comfort_back
from aiogram.types import CallbackQuery, Message, MediaGroup, UserProfilePhotos
from messages import (
    start_description,oltilik,
    photo,reklama1,reklama2,
    photo120,birlik,ikilik, 
    uchlik,torlik,beshlik, oltilik_comfort, beshlik_comfort, torlik_comfort, uchlik_comfort, ikilik_comfort, 
   birlik_comfort, kok, video3)
from aiogram import types

bot = Bot(TOKEN) 
dp = Dispatcher(bot)


ADMIN_IDs = [877492698, 5804415330]

@dp.message_handler(content_types=["photo"])
async def photo_file_id(message: types.Message):
    await message.answer(message.photo[2].file_id)

async def send_admin_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

@dp.message_handler(commands=["start", "help"])
async def start(message:types.Message):
    user = message.from_user
    print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBotimizga yangi odam kirdi\n\nFoydalanuvchi ismi: {user.first_name}\nUsername: @{user.username} \nId raqami: {user.id}\nTelegram tili: {user.language_code} tili')
    allbum = MediaGroup()
    allbum.attach_video(reklama1, caption="video 1")
    allbum.attach_video(reklama2, caption="video 2")
    await message.answer_media_group(media=allbum)
    for chat_id in ADMIN_IDs:
        await send_admin_message(
            chat_id=chat_id,
            text=f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBotimizga yangi odam kirdi\n\nFoydalanuvchi ismi: {user.first_name}\nUsername: @{user.username} \nId raqami: {user.id}\nTelegram tili: {user.language_code} tili")
    await message.answer(text=start_description, reply_markup=menuMain, disable_notification=True)
    

@dp.callback_query_handler(text="↩️Back")
async def delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_description,reply_markup=menuComfort)
@dp.callback_query_handler(text="comfort_back")
async def delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_description,reply_markup=menuComfort)
@dp.callback_query_handler(text="comfort_orqaga")
async def delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_description,reply_markup=menuMain)
@dp.callback_query_handler(text="Ko'k rangi")
async def delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=kok,reply_markup=menuMain)
@dp.callback_query_handler(text="salfetkalar_back")
async def delete_message(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Salfetkalarimiz👇",reply_markup=menuPcs)
# Ultra
@dp.callback_query_handler(text="ℹ️BabyBoo UltraSoft")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("ℹ️BabyBoo UltraSoft",reply_markup=menuUltra)

@dp.callback_query_handler(text="1️⃣lik razmer: 52ta ichida 1 dona p. 💰1346 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=birlik,reply_markup=Ultraback)
@dp.callback_query_handler(text="2️⃣lik razmer: 50ta ichida 1 dona p. 💰1400 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=ikilik,reply_markup=Ultraback)
@dp.callback_query_handler(text="3️⃣lik razmer: 42ta ichida 1 dona p. 💰1666 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=uchlik,reply_markup=Ultraback)
@dp.callback_query_handler(text="4️⃣lik razmer: 36ta ichida 1 dona p. 💰1944 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=torlik,reply_markup=Ultraback)
@dp.callback_query_handler(text="5️⃣lik razmer: 32ta ichida 1 dona p. 💰2187 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=beshlik,reply_markup=Ultraback)
@dp.callback_query_handler(text="6️⃣lik razmer: 26ta ichida 1 dona p. 💰2692 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=oltilik,reply_markup=Ultraback)
@dp.callback_query_handler(text="back2")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_description,reply_markup=menuMain)

@dp.callback_query_handler(text="babyboo_ultraback")
async def ultra_back(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("ℹ️BabyBoo UltraSoft",reply_markup=menuUltra)
@dp.callback_query_handler(text="ultra_back")
async def ultra_back(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=start_description,reply_markup=menuMain)
# Comfort
@dp.callback_query_handler(text="ℹ️BabyBoo Comfort")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("ℹ️BabyBoo Comfort",reply_markup=menuComfort)
@dp.callback_query_handler(text="1️⃣lik razmer: 40ta ichida 1 dona p. 💰1375 so'm")
async def birlik_comfor(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=birlik_comfort,reply_markup=comfort_back)
@dp.callback_query_handler(text="2️⃣lik razmer: 38ta ichida 1 dona p. 💰1447 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=ikilik_comfort,reply_markup=comfort_back)
@dp.callback_query_handler(text="3️⃣lik razmer: 32ta ichida 1 dona p. 💰1718 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=uchlik_comfort,reply_markup=comfort_back)
@dp.callback_query_handler(text="4️⃣lik razmer: 28ta ichida 1 dona p. 💰1964 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=torlik_comfort,reply_markup=comfort_back)
@dp.callback_query_handler(text="5️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=beshlik_comfort,reply_markup=comfort_back)
@dp.callback_query_handler(text="6️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=oltilik_comfort,reply_markup=comfort_back)

@dp.callback_query_handler(text="BabyBoo Salfetka")
async def contact(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Salfetkalarimiz👇",reply_markup=menuPcs)
@dp.callback_query_handler(text="120talik")
async def som12(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=photo120, reply_markup=salfetka_back)
@dp.callback_query_handler(text="120talik k")
async def som12(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=kok, reply_markup=salfetka_back)
@dp.callback_query_handler(text="72talik s")
async def som12(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=video3, reply_markup=salfetka_back)
@dp.callback_query_handler(text="72talik")
async def som8(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(photo=photo,reply_markup=salfetka_back)
@dp.message_handler(content_types=[types.ContentType.STICKER,types.ContentType.ANIMATION,types.ContentType.VIDEO_NOTE,types.ContentType.DOCUMENT])
async def delete_sticker(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("🫵Men sizni tushunmayapman!")




@dp.message_handler()
async def handle_message(message: Message):
    message_text = message.text
    user_id = message.from_user.id

    
    file_path = f'{user_id}.txt'
    with open(file_path, 'a') as write:
        write.write(f'{message_text}\n')

if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)