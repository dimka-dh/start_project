import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "qqq"

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"), KeyboardButton("Купить"))

buying_menu = InlineKeyboardMarkup(row_width=4)
buying_menu.add(
    InlineKeyboardButton("Product1", callback_data="product_buying"),
    InlineKeyboardButton("Product2", callback_data="product_buying"),
    InlineKeyboardButton("Product3", callback_data="product_buying"),
    InlineKeyboardButton("Product4", callback_data="product_buying"),
)

inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories")
button_formulas = InlineKeyboardButton("Формулы расчёта", callback_data="formulas")
inline_keyboard.add(button_calories, button_formulas)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.username}! Я помогу рассчитать вашу норму калорий. Нажмите 'Рассчитать', чтобы начать, или 'Информация', чтобы узнать больше.",
        reply_markup=keyboard
    )


@dp.message_handler(filters.Text(equals="Рассчитать", ignore_case=True))
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(filters.Text(equals="formulas"))
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора для мужчин:\n"
        "10 × вес (кг) + 6.25 × рост (см) − 5 × возраст (лет) + 5\n\n"
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "10 × вес (кг) + 6.25 × рост (см) − 5 × возраст (лет) − 161"
    )
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(filters.Text(equals="calories"))
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data["age"]
    growth = data["growth"]
    weight = data["weight"]

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"{message.from_user.username}, Ваша норма калорий: {calories:.2f} ккал в день.")
    await state.finish()


@dp.message_handler(filters.Text(equals="Информация", ignore_case=True))
async def info(message: types.Message):
    await message.answer(
        "Я бот, который помогает рассчитать вашу норму калорий. Нажмите 'Рассчитать', чтобы начать расчет."
    )


@dp.message_handler(filters.Text(equals="Купить", ignore_case=True))
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer_photo(
            photo=f"https://nhatrangshop.ru/wa-data/public/shop/products/85/34/3485/images/3202/Zvezdochka---lyubaya-gramovka.970.jpeg?text=Product{i}",
            caption=f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100} RUB"
        )
    await message.answer("Выберите продукт для покупки:", reply_markup=buying_menu)


@dp.callback_query_handler(filters.Text(equals="product_buying"))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
