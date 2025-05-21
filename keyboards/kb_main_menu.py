from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


mkp_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мой профиль', callback_data='user:profile')],
        [InlineKeyboardButton(text='Тренировки', callback_data='user:trainings')],
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calc_cals')]
    ]
)