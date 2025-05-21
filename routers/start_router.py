from aiogram import Router
from aiogram import types
from aiogram.filters import Command

from keyboards.kb_main_menu import mkp_start

router_start = Router()

@router_start.message(Command('start'))
async def start_message(msg: types.Message):
    await msg.answer(
        'Тут мотивационный текст или аффирмация...'
        'Главное меню бота',
        reply_markup=mkp_start
    )