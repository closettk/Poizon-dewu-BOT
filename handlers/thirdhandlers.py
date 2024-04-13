#здесь мы считаем кол-во активных юзеров, а также изменяем курс юаня
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3 as sq
from db import update_yuan_rate

#creator = ВАШ TELEGRAM ID
router = Router()

@router.message((F.from_user.id == creator) & F.text == '/countusers')
async def count_users(message: types.Message):
    # Подключаемся к базе данных
    conn = sq.connect('handlers/tg.db')  # замените на путь к вашей базе данных
    cursor = conn.cursor()

    # Выполняем запрос для подсчета пользователей
    cursor.execute("SELECT COUNT(*) FROM profiles")  # замените на имя вашей таблицы
    count = cursor.fetchone()[0]

    # Отправляем количество пользователей пользователю, который запросил команду
    await message.answer(f"Всего пользователей: {count}")
    conn.close()

class NewYan(StatesGroup):
    wait = State()

@router.message((F.from_user.id == creator) & F.text =='/rate')
async def yuancheck(message: types.Message, state: FSMContext):
    await message.answer('Напиши курс юаня')
    await state.set_state(NewYan.wait)

@router.message(NewYan.wait)
async def chee(message: types.Message, state: FSMContext):
    try:
        yan = float(message.text)
        await update_yuan_rate(yan)  # Обновляем курс в базе данных
        await message.answer(f"Обновленное значение курса юаня: {yan}")
    except ValueError:
        await message.answer("Сообщение не содержит корректный курс юаня.")
        return
    await state.clear()