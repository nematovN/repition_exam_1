from aiogram import Router, F, types
from keyboards import main_menu

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer(
        "🎉 Assalomu alaykum, 👾 !\n\n"
        "🚀 Men ariza qabul qiluvchi botman.\n"
        "👇 Quyidagi tugmalardan birini tanlang:",
        reply_markup=main_menu
    )

@router.message(F.text == "ℹ️ Ma'lumot")
async def info_handler(message: types.Message):
    await message.answer(
        "📋 BOT HAQIDA MA'LUMOT\n\n"
        "📌 Bu bot nima qiladi?\n"
        "• Ariza yuborish\n"
        "• Tez javob olish\n"
        "• 24/7 xizmat\n\n"
        "🆘 Yordam: @admin_username"
    )

@router.message(F.text == "📞 Aloqa")
async def contact_handler(message: types.Message):
    await message.answer(
        "📞 BIZ BILAN BOG‘LANING\n"
        "• Telegram: @admin_username\n"
        "• Telefon: +998 90 123 45 67\n"
        "📧 Email: admin@example.com\n"
        "📍 Manzil: Toshkent shahar"
    )
