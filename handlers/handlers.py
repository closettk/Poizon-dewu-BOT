#здесь происходит основная работа. Вроде все понятно, но если не понятно напишите помогу
#при первом написани /start бот высылает ссылку на ваш канал, а в следующий раз такого нет, чтобы не было спамма
from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.keyboards import gk_start, choosewhat, clothes, techno, gk_main, wata
from db import create_profile
from aiogram.types import FSInputFile
from handlers.calculator import calculator
import sqlite3 as sq

#creator = ВАШ TELEGRAM ID

storage = MemoryStorage()
router = Router()

async def get_yuan_rate():
    global db, cur
    db = sq.connect('handlers/tg.db')
    cur = db.cursor()
    cur.execute("SELECT rate FROM yuan_rate WHERE id = 1")
    rate = cur.fetchone()
    return rate[0] if rate else None

class SomeState(StatesGroup):
    wait1 = State()
    wait2 = State()
    wait3 = State()

@router.message(Command('start'))
async def start_co(message: types.Message):
    user_exists = await create_profile(user_id=message.from_user.id)
    if user_exists:
        await message.answer('Выберите действие:', reply_markup=gk_start())
    else:
        image = FSInputFile('PoizonNow.jpg')
        await message.answer_photo(photo=image,caption=f"Добро пожаловать, {message.from_user.first_name} \nНаш канал: @PoizonNow!")
        await message.answer('Выберите действие:', reply_markup=gk_start())

@router.callback_query(F.data=='s_money')
async def s_money(callback: types.CallbackQuery, state: FSMContext):
    image = FSInputFile('cena.jpg')
    await callback.message.answer_photo(
        image,
        caption='В юанях без пробелов и лишних символов напишите зачеркнутую цену(на нашем аккаунте нет скидок)')
    await state.set_state(SomeState.wait1)

@router.message(SomeState.wait1)
async def s_money2(message: types.Message, state: FSMContext):
    yan = await get_yuan_rate()
    if not yan:
        await message.answer("Курс юаня не установлен.")
        return
    try:
        if 1 <= int(message.text) <= 100000:
            money = float(message.text) * yan
            await state.update_data(money=money)
    except ValueError:
        await message.answer('Нужно написать цифры, только цифры')
        return
    await message.forward(chat_id=creator)
    await message.answer('Выберите тип товара:', reply_markup=choosewhat())
    await state.set_state(SomeState.wait2)

@router.callback_query(F.data=='clothes')
async def clothes_f(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Выберите ваш товар:', reply_markup=clothes())
    await state.set_state(SomeState.wait3)

@router.callback_query(F.data=='techno')
async def techno_f(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Выберите ваш товар:', reply_markup=techno())
    await state.set_state(SomeState.wait3)

@router.callback_query(F.data=='perfume')
async def perfume_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 3
    weight = 0.5
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='c_hat')
async def c_hat_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 3
    weight = 0.5
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='c_jacket')
async def c_jacket_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 1
    weight = 1.8
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='c_shirt')
async def c_shirt_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 2
    weight = 0.5
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='c_jeans')
async def c_jeans_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 2
    weight = 1
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='c_sneakers')
async def c_sneakers_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 1
    weight = 1.5
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='t_phone')
async def t_phone_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 3
    weight = 2
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)

@router.callback_query(F.data=='t_laptop')
async def t_laptop_f(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    yan = await get_yuan_rate()
    money = data.get('money')
    box = 1
    weight = 2.5
    text = await calculator(yan=yan, money=money, weight=weight, box=box)
    await callback.message.edit_text(text=text, reply_markup=gk_main())
    await state.set_state(None)
    fornext = round(money*1.005 + 1800 + weight*640)
    await state.update_data(fornext=fornext)

@router.callback_query(F.data=='s_fb')
async def otzivi(callback: types.CallbackQuery):
    await callback.message.edit_text('Отзывы: t.me/poizonnowfeedback', reply_markup=wata())

@router.callback_query(F.data=='s_zakaz')
async def zakazik(callback: types.CallbackQuery):
    await callback.message.edit_text('Заказать/Задать вопрос: @benetter',
                                     'Ответы на часто задаваемые вопросы: https://t.me/PoizonNow/4',
                                  reply_markup=wata())

@router.callback_query(F.data=='main')
async def etomain(callback: types.CallbackQuery):
    await callback.message.edit_text('Выберите действие:',reply_markup=gk_start())