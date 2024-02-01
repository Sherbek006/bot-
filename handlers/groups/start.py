from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from filters import IsGroup
import logging

@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"Asalom alaykum yaxshi bola bo'l, {message.chat.title}!")


@dp.message_handler(IsGroup(),text ="salom")
async def bott(message: types.Message):
    logging.info(message)
    await message.answer(f"valeykum salom, {message.from_user.full_name}!")



@dp.message_handler(IsGroup(),text ="makama")
@dp.message_handler(IsGroup(),text ="qanday")
async def boft(message: types.Message):
    logging.info(message)
    await message.answer(f"zo'r yaxshi raxmat xudoga shukur o'zizchi brodar, {message.from_user.full_name}!")