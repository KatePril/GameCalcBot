from aiogram import types
from loader import dp
from expressions import give_question

correct = 0
incorrect = 0
expression_result = 0

@dp.message_handler(commands='next')
async def send_expression(message: types.Message):
    global expression_result
    expression, markup = give_question()
    expression_result = eval(expression)
    await message.answer(f'What is the result of {expression}?\n/next\n/stop_game', reply_markup=markup)
    
@dp.message_handler(commands='stop_game')
async def end_game(message: types.Message):
    global expression_result, correct, incorrect
    await message.reply(f"You have {correct} correct answers and {incorrect} incorrect answers\nType '/next' to start again")
    if correct > incorrect:
        await message.answer_sticker('CAACAgIAAxkBAAMLZC7jGd-wBGvbaMqukB67kHn5SpUAAikAA8GcYAzwS6kev9jffC8E')
    else:
        await message.answer_sticker('CAACAgIAAxkBAAMNZC7jG8HXwEiAvfu_udNWSBIqzzgAAi0AA8GcYAzjNPIncv-QZS8E')
    correct = 0
    incorrect = 0

@dp.callback_query_handler(text_contains='correct_') 
async def plus(call: types.CallbackQuery):
    global correct
    correct = correct + 1
    await call.message.answer('Correct\n/next\n/stop_game')
    
@dp.callback_query_handler(text_contains='wrong_') 
async def minus(call: types.CallbackQuery):
    global incorrect, correct, expression_result
    incorrect = incorrect + 1
    if incorrect >= 5:
        await call.message.answer("You reached the maximum number of incorrect answers (5 answers)\nYou have {correct} correct answers and {incorrect} incorrect answers\nType '/next' to start again")
        await call.message.answer_sticker('CAACAgIAAxkBAAMPZC7jHZO_BuBNm6EHZZY7epUqAqoAAiUAA8GcYAyxmxTZKx6K1i8E')
        correct = 0
        incorrect = 0
    else:
        await call.message.answer(f'Incorrect, correct result is {expression_result}\n/next\n/stop_game')