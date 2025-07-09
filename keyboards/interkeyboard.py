from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

about_me_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Качества и Навыки', callback_data='princ')],
    [InlineKeyboardButton(text='Мой Instagram', url='https://www.instagram.com/ahsusk_/profilecard/')],
    [InlineKeyboardButton(text='Телеграмм для связи', url='https://t.me/ahsusk4')]

]
)

inline_princip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться', callback_data='about_me')]
]
)


inline_portfolio = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Предыдущая', callback_data='back'), InlineKeyboardButton(text='Следующая', callback_data='next')]
    ]
)


choice_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Брендинг', callback_data='logo')],
    [InlineKeyboardButton(text='Полиграфия', callback_data='poligraf')],
    [InlineKeyboardButton(text='Наружняя реклама', callback_data='smm')],
    [InlineKeyboardButton(text='Мерч', callback_data='merch')],
    [InlineKeyboardButton(text='Визуальный контент', callback_data='content')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
    ]
)

logo_key = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Создание логотипа', callback_data='logo1')],
    [InlineKeyboardButton(text='Фирменный стиль', callback_data='logo2')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]])
poligraf_key = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Брошюра/Буклет/Флаер/Листовка/Билет/Постер', callback_data='poligraf1')],
    [InlineKeyboardButton(text='Журнал/Упаковка/Наклейки', callback_data='poligraf2')],
    [InlineKeyboardButton(text='Этикетка/Обложка книги/Каталог', callback_data='poligraf3')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]])
smm_key = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Афиша', callback_data='smm1')],
    [InlineKeyboardButton(text='Баннер', callback_data='smm2')],
    [InlineKeyboardButton(text='Вывеска', callback_data='smm3')],
    [InlineKeyboardButton(text='Билборд', callback_data='smm4')],
    [InlineKeyboardButton(text='Рекламный щит', callback_data='smm5')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
    ]
)
merch_key = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Принт для футболки', callback_data='merch1')],
    [InlineKeyboardButton(text='Принт для сумки', callback_data='merch2')],
    [InlineKeyboardButton(text='Дизайн кружки', callback_data='merch3')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]])
content_key = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Стикеры/Иконки/Пиктограммы', callback_data='content1')],
    [InlineKeyboardButton(text='Инфографика/Презентация', callback_data='content2')],
    [InlineKeyboardButton(text='Сторитейлинг/пост/пост-карусель', callback_data='content3')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
    ]
)




# calculate_cache = InlineKeyboardMarkup(
#     inline_keyboard=[
#     [InlineKeyboardButton(text='Логотип', callback_data='price1')],
#     [InlineKeyboardButton(text='Фирменный стиль', callback_data='price2')],
#     [InlineKeyboardButton(text='Упаковка', callback_data='price3')],
#     [InlineKeyboardButton(text='Полиграфия (визитки, буклеты)', callback_data='price4')],
#     [InlineKeyboardButton(text='Соцсети (обложки, шаблоны)', callback_data='price5')]
#     ]
# )

calculate_hard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Простой (шаблонный дизайн)', callback_data='easy')],
    [InlineKeyboardButton(text='Средний (индивидуальный, но без уникальных иллюстраций)', callback_data='medium')],
    [InlineKeyboardButton(text='Сложный (полный брендинг с анимацией)', callback_data='hard')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]]
)

calculate_period = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Стандартные сроки (не влияет на цену)', callback_data='standart')],
    [InlineKeyboardButton(text='Ускоренный режим (+20–50% к стоимости)', callback_data='fast')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]]
)

amount_marks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1–2 правки (включено в стоимость)', callback_data='marks1')],
    [InlineKeyboardButton(text='3–5 правок (+10–20%)', callback_data='marks2')],
    [InlineKeyboardButton(text='Безлимитные правки (+30–50%)', callback_data='marks3')],
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]]
)