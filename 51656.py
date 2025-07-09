import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InputMediaPhoto
from aiogram import F
from aiogram.utils import run_polling

API_TOKEN = '7487741804:AAGVcjzCqrKJuXgWT_eEvA7d5EHzdJevclA'  # Замените на ваш токен

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Команда /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Используйте команду /portfolio для просмотра моего портфолио.")


# Команда /portfolio
@dp.message(Command("portfolio"))
async def send_portfolio(message: types.Message):
    # Список путей к изображениям (скриншотам)
    images = [
        'C:/python/телеграмм бот графф дизигн/1.jpg',
        'C:/python/телеграмм бот графф дизигн/2.jpg',
        'C:/python/телеграмм бот графф дизигн/3.jpg'
    ]

    # Отправка изображений в виде карусели
    media = [InputMediaPhoto(open(image, 'rb')) for image in images]

    await message.answer_media_group(media)


# Запуск бота
if __name__ == '__main__':
    run_polling(dp)