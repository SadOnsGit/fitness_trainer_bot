from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mkp_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мой профиль', callback_data='user:profile')],
        [InlineKeyboardButton(text='Мои тренировки', callback_data='user:trainings')],
        [InlineKeyboardButton(text='💪 Рассчитать норму калорий', callback_data='calc_cals')]
    ]
)