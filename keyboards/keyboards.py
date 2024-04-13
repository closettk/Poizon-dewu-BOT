#поменяйте клавиатуру под себя и уберите духи, их вроде некоторые карго не доставляют
#возможно долго тыкать сначала на тип товара и затем только на конкретный товар. Так что можно просто оставить одежду и убрать остальные кнопки ведь на них почти не тыкают
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def gk_start() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='💵 Рассчитать стоимость', callback_data='s_money')],
        [InlineKeyboardButton(text='🔍 Отзывы', callback_data='s_fb')],
        [InlineKeyboardButton(text='📲 Перейти к заказу/Задать вопрос', callback_data='s_zakaz')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def choosewhat() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='🧥 Одежда', callback_data='clothes')],
        [InlineKeyboardButton(text='📱 Техника', callback_data='techno')],
        [InlineKeyboardButton(text='💍 Аксессуары/Духи', callback_data='perfume')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def clothes() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='💂‍♂️ Головной убор', callback_data='c_hat')],
        [InlineKeyboardButton(text='🧥 Куртка', callback_data='c_jacket')],
        [InlineKeyboardButton(text='👕 Футболка', callback_data='c_shirt')],
        [InlineKeyboardButton(text='👖 Джинсы', callback_data='c_jeans')],
        [InlineKeyboardButton(text='👟 Обувь', callback_data='c_sneakers')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def techno() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='📱 Телефон', callback_data='t_phone')],
        [InlineKeyboardButton(text='💻 Ноутбук', callback_data='t_laptop')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def gk_main() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='💵 Рассчитать стоимость', callback_data='s_money')],
        [InlineKeyboardButton(text='📲 Перейти к заказу', callback_data='s_zakaz')],
        [InlineKeyboardButton(text='👈 Главное меню', callback_data='main')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def wata() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='💵 Рассчитать стоимость', callback_data='s_money')],
        [InlineKeyboardButton(text='👈 Главное меню', callback_data='main')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def yesorno() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='✅ Да', callback_data='yes'),
         InlineKeyboardButton(text='❌ Нет', callback_data='no')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def secondyesorno() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='✅ Да', callback_data='secondyes'),
         InlineKeyboardButton(text='❌ Нет', callback_data='secondno')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb