from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


async def start_menu():
    btn = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btn.add(
        KeyboardButton("🎁 Купить"),
        KeyboardButton("📱 Профиль"),
        KeyboardButton("ℹ️ FAQ"),
        KeyboardButton("📕 Поддержка"),
        KeyboardButton("▶️ Информация")
    )
    return btn