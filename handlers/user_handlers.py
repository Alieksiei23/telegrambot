
from database.database import conn, data_base
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message, FSInputFile
from keyboards.replykeyboard import start_keyboard
from keyboards.interkeyboard import (about_me_keyboard, inline_princip, inline_portfolio,
                                     calculate_hard, calculate_period, amount_marks, choice_menu, logo_key,
                                     poligraf_key, smm_key, merch_key, content_key)





router = Router()
portfolio = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg']

# старт
@router.message(CommandStart())
async def cmd_start(message: Message):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users(user_id, username, name, date) VALUES('{message.from_user.id}', '{message.from_user.username}', '{message.from_user.first_name}', 'NOW()')")
    conn.commit()
    if message.from_user.id not in data_base:
        data_base[message.from_user.id] = [0, 0]
    await message.answer(
        'Привет! Я - цифровой помощник Ксюши, графического дизайнера. Помогу:'
        '\n✨Узнать о моем подходе к дизайну'
        '\n💡Рассчитать стоимость вашего проекта'
        '\n📂Показать, как создаются крутые бренды',
        reply_markup=start_keyboard
    )


@router.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer(
        'Выберите интересующую категорию!',
        reply_markup=start_keyboard
    )

@router.callback_query(F.data=='about_me')
@router.message(F.text=='Обо мне!')
async def about_me(message: Message | CallbackQuery):
    if isinstance(message, Message):
        await message.answer(
        "<b>Я — Ксюша</b> 😊, графический дизайнер, который превращает идеи в визуальные решения. 🎨\n"
        "За <b>18 месяцев</b> опыта работы на крупном предприятии я научилась находить баланс ⚖️ "
        "между стандартами компании и творческими решениями. ✨\n\n"
        "<b>В моем портфолио:</b> брендинг 🏷️, печатная продукция 🖨️, наружная реклама 📢 и цифровые форматы 💻, "
        "выполненные с вниманием к деталям и пониманием контекста. 🔍",
        reply_markup=about_me_keyboard
        )
    else:
        await message.answer()
        await message.message.edit_text(
        "<b>Я — Ксюша</b> 😊, графический дизайнер, который превращает идеи в визуальные решения. 🎨\n"
        "За <b>18 месяцев</b> опыта работы на крупном предприятии я научилась находить баланс ⚖️ "
        "между стандартами компании и творческими решениями. ✨\n\n"
        "<b>В моем портфолио:</b> брендинг 🏷️, печатная продукция 🖨️, наружная реклама 📢 и цифровые форматы 💻, "
        "выполненные с вниманием к деталям и пониманием контекста. 🔍",
            reply_markup=about_me_keyboard
        )


@router.callback_query(F.data=='princ')
async def princ_func(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "В работе сочетаю креативность 🤯 с дисциплиной 🫡.\n"
    "Генерирую идеи 💡 и всегда помню о дедлайнах 😇.\n"
    "Инициативна, внимательна к деталям и открыта к диалогу 😉.\n"
    "В работе использую:\n"
    "<b><i>Adobe Illustrator</i></b>, <b><i>Adobe Photoshop</i></b>, <b><i>Figma</i></b>.",
        reply_markup=inline_princip
    )


@router.callback_query(F.data=='contacts')
async def contacts_func(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        ''
    )

@router.message(F.text == 'Портфолио')
async def send_portfolio(message: Message):
    data_base[message.from_user.id][0] = 0
    await message.answer_photo(photo=FSInputFile('1.jpg'), reply_markup=inline_portfolio)

@router.callback_query(F.data == 'next')
async def next_slide(callback: CallbackQuery):
    if data_base[callback.from_user.id][0] == len(portfolio)-1:
        await callback.answer()
        await callback.message.answer_photo(photo=FSInputFile(portfolio[data_base[callback.from_user.id][0]]),
                                            reply_markup=inline_portfolio)
    else:
        await callback.answer()
        data_base[callback.from_user.id][0] += 1
        await callback.message.answer_photo(photo=FSInputFile(portfolio[data_base[callback.from_user.id][0]]), reply_markup=inline_portfolio)
    await callback.message.delete()

@router.callback_query(F.data == 'back')
async def back_slide(callback: CallbackQuery):
    if data_base[callback.from_user.id][0] == 0:
        await callback.answer()
        await callback.message.answer_photo(photo=FSInputFile(portfolio[data_base[callback.from_user.id][0]]),
                                            reply_markup=inline_portfolio)
    else:
        await callback.answer()
        data_base[callback.from_user.id][0] -= 1
        await callback.message.answer_photo(photo=FSInputFile(portfolio[data_base[callback.from_user.id][0]]),
                                                  reply_markup=inline_portfolio)
    await callback.message.delete()

@router.message(F.text=='Расчитать стоимость')
async def calculate_cashe(message: Message):
    await message.answer(
        text='Укажи работу которую необходимо выполнить!',
        reply_markup=choice_menu
    )


@router.callback_query(F.data == 'cancel')
async def price1(callback: CallbackQuery):
    data_base[callback.from_user.id][1] = 0
    await callback.answer()
    await callback.message.delete()



@router.callback_query(F.data.in_(['logo', 'poligraf', 'smm', 'merch', 'content']))
async def price1(callback: CallbackQuery):
    await callback.answer()
    if callback.data=='logo':
        await callback.message.edit_text('Какой брендинг вам интересен?',reply_markup=logo_key)
    elif callback.data=='poligraf':
        await callback.message.edit_text('Выберите нужную полиграфию!',reply_markup=poligraf_key)
    elif callback.data=='smm':
        await callback.message.edit_text('Выберите тип рекламы!',reply_markup=smm_key)
    elif callback.data=='merch':
        await callback.message.edit_text('Какой мерч вы рассматриваете?',reply_markup=merch_key)
    elif callback.data=='content':
        await callback.message.edit_text('Выберите нужный контент!',reply_markup=content_key)


@router.callback_query(F.data.in_(['logo1', 'logo2']))
async def price1(callback: CallbackQuery):
    if callback.data=='logo1':
        data_base[callback.from_user.id][1] = 70
    elif callback.data=='logo2':
        data_base[callback.from_user.id][1] = 100
    await callback.answer()
    await callback.message.edit_text(
        'Какой сложности работа?',
        reply_markup=calculate_hard
    )

@router.callback_query(F.data.in_(['poligraf1', 'poligraf2', 'poligraf3']))
async def price1(callback: CallbackQuery):
    if callback.data=='poligraf1':
        data_base[callback.from_user.id][1] = 50
    elif callback.data=='poligraf2':
        data_base[callback.from_user.id][1] = 70
    elif callback.data == 'poligraf3':
        data_base[callback.from_user.id][1] = 100
    await callback.answer()
    await callback.message.edit_text(
        'Какой сложности работа?',
        reply_markup=calculate_hard
    )

@router.callback_query(F.data.in_(['smm1', 'smm2', 'smm3', 'smm4', 'smm5']))
async def price1(callback: CallbackQuery):
    if callback.data=='smm1':
        data_base[callback.from_user.id][1] = 60
    elif callback.data=='smm2':
        data_base[callback.from_user.id][1] = 65
    elif callback.data == 'smm3':
        data_base[callback.from_user.id][1] = 70
    elif callback.data == 'smm4':
        data_base[callback.from_user.id][1] = 75
    elif callback.data == 'smm5':
        data_base[callback.from_user.id][1] = 80
    await callback.answer()
    await callback.message.edit_text(
        'Какой сложности работа?',
        reply_markup=calculate_hard
    )

@router.callback_query(F.data.in_(['merch1', 'merch2', 'merch3']))
async def price1(callback: CallbackQuery):
    if callback.data=='merch1':
        data_base[callback.from_user.id][1] = 100
    elif callback.data=='merch2':
        data_base[callback.from_user.id][1] = 150
    elif callback.data == 'merch3':
        data_base[callback.from_user.id][1] = 50
    await callback.answer()
    await callback.message.edit_text(
        'Какой сложности работа?',
        reply_markup=calculate_hard
    )

@router.callback_query(F.data.in_(['content1', 'content2', 'content3']))
async def price1(callback: CallbackQuery):
    if callback.data=='content1':
        data_base[callback.from_user.id][1] = 150
    elif callback.data=='content2':
        data_base[callback.from_user.id][1] = 100
    elif callback.data == 'content3':
        data_base[callback.from_user.id][1] = 70
    await callback.answer()
    await callback.message.edit_text(
        'Какой сложности работа?',
        reply_markup=calculate_hard
    )


@router.callback_query(F.data.in_(['easy', 'medium', 'hard']))
async def hard_skills(callback: CallbackQuery):
    if callback.data=='medium':
        data_base[callback.from_user.id][1] = data_base[callback.from_user.id][1] * 1.15
    elif callback.data=='hard':
        data_base[callback.from_user.id][1] = data_base[callback.from_user.id][1] * 1.5
    await callback.answer()
    await callback.message.edit_text(
        'Срочный ли у вас заказ?',
        reply_markup=calculate_period
    )

@router.callback_query(F.data.in_(['standart', 'fast']))
async def hard_skills(callback: CallbackQuery):
    if callback.data=='fast':
        data_base[callback.from_user.id][1] = data_base[callback.from_user.id][1] * 1.5
    await callback.answer()
    await callback.message.edit_text(
        'На какое количество правок вы рассчитываете?',
        reply_markup=amount_marks
    )

@router.callback_query(F.data.in_(['marks1', 'marks2', 'marks3']))
async def hard_skills(callback: CallbackQuery):
    if callback.data=='marks2':
        data_base[callback.from_user.id][1] = data_base[callback.from_user.id][1] * 1.15
    elif callback.data=='marks3':
        data_base[callback.from_user.id][1] = data_base[callback.from_user.id][1] * 1.5
    await callback.answer()
    await callback.message.edit_text(
        f'Примерная стоимость вашего заказа будет {data_base[callback.from_user.id][1]}р'
        '\nчтобы узнать итоговую стоимость пиши мне!',
    )
    data_base[callback.from_user.id][1] = 0
