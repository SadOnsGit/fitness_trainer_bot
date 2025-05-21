from aiogram import Router
from aiogram import types
from aiogram.filters import Command

from keyboards.kb_main import mkp_main


router_start = Router()


@router_start.message(Command('start'))
async def start_message(msg: types.Message):
    await msg.answer(
        'Тут мотивационный текст или аффирмация...'
        '\nГлавное меню бота',
        reply_markup=mkp_main,
    )
