from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
async def inline():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("пробив по номеру", callback_data="btn1")
    btn2 = InlineKeyboardButton("ПВД", callback_data="btn2")
    btn3 = InlineKeyboardButton("ФНС", callback_data="btn3")
    btn4 = InlineKeyboardButton("ПФР", callback_data="btn4")
    btn5 = InlineKeyboardButton("МИНИ-ДОСЬЕ(АВТОВЫДАЧА)", callback_data="btn5")
    btn6 = InlineKeyboardButton("ВЕРЕФИКАТЦЫЯМ ГОТОВЫЕ КОШЕЛКИ", callback_data="btn6")
    btn7 = InlineKeyboardButton("МОБИЛНЫЕ ОПЕРАТОРЫ", callback_data="btn7")
    btn8 = InlineKeyboardButton("ФЛУД И РАССЫЛКА", callback_data="btn8")
    btn9 = InlineKeyboardButton("ПРОБИВ КИ ", callback_data="btn9")
    btn10 = InlineKeyboardButton("СЕРТИФИКАТ КОВИД", callback_data="btn10")
    btn11 = InlineKeyboardButton("✅ДОКУМЕНТЫ", callback_data="btn11")


    inline_keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11)
    return inline_keyboard


from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
async def inline_btn():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton(" 💵ПОПОЛНИТЬ ", callback_data="btn1")
    btn2 = InlineKeyboardButton("🛒МОИ ЗАКАЗЫ", callback_data="btn2")



    inline_keyboard.add(btn1,btn2,)
    return inline_keyboard