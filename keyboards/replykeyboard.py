from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text='Портфолио'), KeyboardButton(text='Обо мне!')],
        [KeyboardButton(text='Расчитать стоимость')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите инстересующую кнопку!'
)