import logging
from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton
from aiogram import Bot ,Dispatcher ,executor,types
from btn import start_menu
from inline_btn import inline , inline_btn

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "6041736832:AAHDF7tFI-vGcWPWRWdgPrGcVRr6Cx9oV44"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    a = await start_menu()
    await message.answer("""
🔸 Бот готов к использованию.
🔸 Если не появились вспомогательные кнопки
▶️ Введите /start
    """, reply_markup=a)


@dp.message_handler(text=["🎁 Купить"]) 
async def kupit_bot(message:types.Message) :
    b = await inline()
    await message.answer("🎁 Купить", reply_markup=b)

@dp.message_handler(text=["📱 Профиль"]) 
async def profil_bot(message:types.Message) :
    c = await inline_btn()
    await message.answer("""
    📱 Профиль
 📱 Ваш профиль:
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔑 Мой ID: 5370726024
👤 Логин: @abdulloh01s
🕜 Регистрация: 20/05/2023 09:55:32
➖➖➖➖➖➖➖➖➖➖➖➖➖
💳 Баланс: 0.0 р
👥Вы пригласили: 0 человек
🔗Ссылка для приглашения: https://t.me/Probiv2bot?start=5370726024
    """, reply_markup=c)  


@dp.message_handler(text=["ℹ️ FAQ"]) 
async def kupit_bot(message:types.Message) :
    await message.answer("""
    ℹ️ FAQ
    Данный бот, поможет вам найти кого угодно.
Наши плюсы:
➕Удобное использование
➕Автоматическая оплата
➕Вашим заказом занимаются профессионалы
➕Прямая связь с саппортом
➕Выдача заказа в сроки

Помощь/предложить свои услуги - @kaban_service
    """)
@dp.message_handler(text=["📕 Поддержка"]) 
async def kupit_bot(message:types.Message) :
    await message.answer("""
📕 Писать сюда ➡️ @kaban_service
    """)
@dp.message_handler(text=["▶️ Информация"]) 
async def kupit_bot(message:types.Message) :
    await message.answer("""
Работаем быстро и качественно ✅

Помощь/предложить свои услуги - @kaban_service
    """)

if __name__ == "__main__":
    executor.start_polling(dp)