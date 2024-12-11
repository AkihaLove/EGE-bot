import asyncio
from aiogram import Bot, Dispatcher, types
import stress
from aiogram.filters import Command

bot = Bot(token="Your Token Here")
dp = Dispatcher()

@dp.message(Command('start'))  # Обработка команды /start
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в бот для подготовки к ЕГЭ по русскому языку! Список доступных команд вы можете увидеть написав /help")

@dp.message(Command('help'))  # Обработка команды /help
async def help_command(message: types.Message):
    await message.answer("Доступные команды: /help - команды, /start - Вернуться к приветствию, /train - запустить тренировку, /stop - закончить тренировку")

@dp.message(Command('stop'))  # Обработка команды /stop
async def stop_command(message: types.Message):
    await message.answer("Удачи! Если снова захотите запустить тренировку, введите /train. Чтобы увидеть список остальных команд введите /help")

@dp.message(Command('train'))  # Обработка команды /train
async def victorina_handler(message: types.Message):
    await send_random_quiz(message.from_user.id)

@dp.poll_answer()  # При ответе на вопрос, отправляет случайную викторину
async def answer(PollAnswer: types.PollAnswer):
    await send_random_quiz(PollAnswer.user.id)

async def send_random_quiz(user_id: int):  # Определяет функцию отправляющую викторину
    quiz = stress.get_random_quiz()  # Получает случайную викторину из модуля стресс
    
    await bot.send_poll(chat_id=user_id,
                        question=f'Поставь правильное ударение в слове {quiz.question.upper()}',  # Определяет формат викторины
                        options=quiz.options,
                        type='quiz',
                        correct_option_id=quiz.correct_number,
                        is_anonymous=False)

# Обработка входящих обновлений telegram
async def main():
    await dp.start_polling(bot)

# Если модуль является основным, то запускает бота
if __name__ == "__main__":
    asyncio.run(main())
