from aiogram import types
from loader import dp

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm CalcBot another calculation game!\nType '/next' to get the first expression")
    
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)