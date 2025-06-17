from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📄 Ariza yuborish")],
        [KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

# Ariza turlari menyusi
ariza_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💼 Ish joyiga ariza")],
        [KeyboardButton(text="🎓 Ta'lim muassasasiga ariza")],
        [KeyboardButton(text="🏥 Tibbiy xizmat uchun ariza")],
        [KeyboardButton(text="🏠 Uy-joy masalasi uchun ariza")]
    ],
    resize_keyboard=True
)

# Tasdiqlash uchun inline tugmalar
tasdiqlash_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash va yuborish", callback_data="tasdiq")],
        [InlineKeyboardButton(text="✏️ Tahrirlash", callback_data="edit")],
        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")]
    ]
)
