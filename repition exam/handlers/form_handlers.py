from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from forms import Form
from keyboards import ariza_menu, tasdiqlash_inline

router = Router()


@router.message(F.text == "📄 Ariza yuborish")
async def start_form(message: types.Message, state: FSMContext):
    await state.set_state(Form.ism)
    await message.answer(
        "📄 Ariza berish jarayonini boshlaymiz!\n\n"
        "👤 Iltimos, ismingizni kiriting:\n"
        "💡 Masalan: Abdulla"
    )


@router.message(Form.ism)
async def get_ism(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Form.familiya)
    await message.answer("👨‍👩‍👧‍👦 Familiyangizni kiriting:\n💡 Masalan: Karimov")


@router.message(Form.familiya)
async def get_familiya(message: types.Message, state: FSMContext):
    await state.update_data(familiya=message.text)
    await state.set_state(Form.yosh)
    await message.answer("🎂 Yoshingizni kiriting:\n💡 Faqat raqam kiriting (masalan: 25)")


@router.message(Form.yosh)
async def get_yosh(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("❌ Faqat raqam kiriting!")
    await state.update_data(yosh=message.text)
    await state.set_state(Form.telefon)
    await message.answer("📱 Telefon raqamingizni kiriting:\n💡 Masalan: +998901234567 yoki 901234567")


@router.message(Form.telefon)
async def get_telefon(message: types.Message, state: FSMContext):
    await state.update_data(telefon=message.text)
    await state.set_state(Form.manzil)
    await message.answer("🏠 Manzilingizni kiriting:\n💡 Masalan: Toshkent shahar, Chilonzor tumani, Bunyodkor ko‘chasi, 5-uy")


@router.message(Form.manzil)
async def get_manzil(message: types.Message, state: FSMContext):
    if len(message.text.strip()) < 10:
        return await message.answer("❌ Manzil juda qisqa! Iltimos, to‘liq yozing.")
    await state.update_data(manzil=message.text)
    await state.set_state(Form.turi)
    await message.answer("📋 Ariza turini tanlang:", reply_markup=ariza_menu)


@router.message(Form.turi)
async def get_turi(message: types.Message, state: FSMContext):
    await state.update_data(turi=message.text)
    await state.set_state(Form.matn)
    await message.answer(
        "✍️ Ariza matnini yozing:\n\n"
        "📝 Batafsil yozing, bu sizning asosiy murojaatingiz.\n"
        "💡 Qancha ko'p ma'lumot bersangiz, shuncha tez javob olasiz!\n\n"
        "⏰ Vaqtingizni band qilmaslik uchun, ariza matnini oldindan tayyorlab qo'ysangiz bo'ladi."
    )


@router.message(Form.matn)
async def get_matn(message: types.Message, state: FSMContext):
    await state.update_data(matn=message.text)
    data = await state.get_data()

    msg = (
        "📋 *SIZNING ARIZANGIZ:*\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 Ism: {data['ism']}\n"
        f"👨‍👩‍👧‍👦 Familiya: {data['familiya']}\n"
        f"🎂 Yosh: {data['yosh']}\n"
        f"📱 Telefon: {data['telefon']}\n"
        f"🏠 Manzil: {data['manzil']}\n"
        f"📋 Ariza turi: {data['turi']}\n\n"
        f"✍️ Ariza matni:\n{data['matn']}\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "❓ Ma'lumotlar to‘g‘rimi?"
    )

    await state.set_state(Form.tasdiq)
    await message.answer(msg, parse_mode="Markdown", reply_markup=tasdiqlash_inline)


@router.callback_query(F.data == "tasdiq")
async def confirm(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("✅ Arizangiz yuborildi! Rahmat.", parse_mode="Markdown")
    await state.clear()


@router.callback_query(F.data == "cancel")
async def cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("❌ Ariza bekor qilindi.")
    await state.clear()


@router.callback_query(F.data == "edit")
async def edit_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("✏️ Qaysi ma'lumotni tahrirlashni xohlaysiz? (hozircha bu bo‘lim soddalashtirilgan)")
