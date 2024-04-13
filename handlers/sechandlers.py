#здесь есть /cancel для отмены любого действия, а также можно сделать рекламный пост
#после отправки поста бот сам почистит недоступных юзеров, после чего вы можете проверить кол-во активных с помощью /countusers
from aiogram import types, Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keyboards import yesorno, secondyesorno
from aiogram.exceptions import TelegramForbiddenError, TelegramNotFound
from aiogram.methods import SendPhoto, SendMessage
import sqlite3 as sq

#creator = ВАШ TELEGRAM ID
token='ВАШ ТОКЕН'
bot = Bot(token=token)

router = Router()

class PostForm(StatesGroup):
    text = State()
    Photo = State()

@router.message((F.from_user.id == creator) & F.text == '/cancel')
async def cancelco(message: types.Message, state: FSMContext):
    await state.set_state(None)
    await message.answer('Все было отменено')

@router.message((F.from_user.id == creator) & F.text == '/addpost')
async def add_post_start(message: types.Message, state: FSMContext):
    await message.answer("Отправьте фото для поста.")
    await state.set_state(PostForm.Photo)

@router.message(PostForm.Photo)
async def process_post_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    user_data = await state.get_data()
    photo_file_id = user_data['photo']
    await message.answer_photo(photo=photo_file_id, reply_markup=yesorno())

@router.callback_query(F.data=='no')
async def nophoto(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Все было прервано')
    await state.set_state(None)

@router.callback_query(F.data=='yes')
async def yesphoto(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Теперь текст')
    await state.set_state(PostForm.text)

@router.message(PostForm.text)
async def addtext(message: types.Message, state: FSMContext):
    await state.update_data(texto=message.text)
    user_data = await state.get_data()
    TEXT = user_data['texto']
    photo_file_id = user_data['photo']
    await message.answer_photo(photo=photo_file_id,caption=TEXT,reply_markup=secondyesorno())


@router.callback_query(F.data=='secondno')
async def noall(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Все было прервано')
    await state.set_state(None)

@router.callback_query(F.data=='secondyes')
async def yesall(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    photo_file_id = user_data['photo']
    TEXT = user_data['texto']

    # Подключаемся к базе данных и получаем список всех user_id
    conn = sq.connect('handlers/tg.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM profiles")
    users = cursor.fetchall()
    
    # Отправляем пост каждому пользователю из списка
    for user_id in users:
        send_photo_request = SendPhoto(chat_id=user_id[0], photo=photo_file_id, caption=TEXT)
        try:
            await bot(send_photo_request)
        except (TelegramForbiddenError, TelegramNotFound):
            # Удаление пользователя из базы данных
            cursor.execute("DELETE FROM profiles WHERE user_id = ?", (user_id[0],))
            conn.commit()
            send_messagef = SendMessage(chat_id=creator, text=f"Пользователь {user_id[0]} заблокировал бота и был удален из базы данных.")
            await bot(send_messagef)
        except Exception as e:
            send_messagef = SendMessage(chat_id=creator, text=f"Не удалось отправить сообщение пользователю {user_id[0]}: {e}")
            await bot(send_messagef)

    # Закрываем соединение с базой данных после выполнения всех операций
    conn.close()

    await callback.message.answer('Пост был отправлен всем пользователям')
    await state.set_state(None)
