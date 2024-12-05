from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, add_user, is_included, get_all_users

api = "qqq"

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


# Добавление данных в таблицу через запуск файла crud_functions
initiate_db()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard.add(
    KeyboardButton("Рассчитать"),
    KeyboardButton("Информация"),
    KeyboardButton("Купить"),
    KeyboardButton("Регистрация"),
    KeyboardButton("Список пользователей"),
    KeyboardButton("Список продуктов")
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


@dp.message_handler(filters.Text(equals="Регистрация", ignore_case=True))
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return
    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    data = await state.get_data()

    add_user(data["username"], data["email"], data["age"])
    await message.answer(f"Регистрация завершена! Пользователь {data['username']} успешно зарегистрирован.")
    await state.finish()


@dp.message_handler(filters.Text(equals="Список пользователей", ignore_case=True))
async def list_users(message: types.Message):
    users = get_all_users()
    if not users:
        await message.answer("Список пользователей пуст.")
    else:
        user_list = "\n\n".join(
            f"ID: {user[0]}\nИмя: {user[1]}\nEmail: {user[2]}\nВозраст: {user[3]}\nБаланс: {user[4]} RUB"
            for user in users
        )
        await message.answer(f"Список пользователей:\n\n{user_list}")


@dp.message_handler(filters.Text(equals="Список продуктов", ignore_case=True))
async def list_products(message: types.Message):
    products = get_all_products()
    if not products:
        await message.answer("Список продуктов пуст.")
    else:
        product_list = "\n\n".join(
            f"ID: {product[0]}\nНазвание: {product[1]}\nОписание: {product[2]}\nЦена: {product[3]} RUB"
            for product in products
        )
        await message.answer(f"Список продуктов:\n\n{product_list}")


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
    products = get_all_products()
    inline_menu = InlineKeyboardMarkup(row_width=1)

    for product in products:
        await message.answer_photo(
            photo=f"https://nhatrangshop.ru/wa-data/public/shop/products/85/34/3485/images/3202/Zvezdochka---lyubaya-gramовка.970.jpeg?text={product[1]}",
            caption=f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} RUB"
        )
        inline_menu.add(
            InlineKeyboardButton(product[1], callback_data=f"product_buying_{product[0]}")
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_menu)


@dp.callback_query_handler(lambda call: call.data.startswith("product_buying_"))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(f"Вы успешно приобрели выбранный продукт.")
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
