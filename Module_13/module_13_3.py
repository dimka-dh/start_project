from aiogram import Bot, Dispatcher, executor, types


api = "ййй"

bot = Bot(token=api)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
