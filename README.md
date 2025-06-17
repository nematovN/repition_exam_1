# 📋 Telegram Ariza Qabul Bot

Bu Telegram bot foydalanuvchilardan turli xil arizalarni qabul qilish, ularni shakllantirish va yakunda tasdiqlatish uchun yaratilgan. Bot foydalanuvchidan ism, familiya, yosh, telefon, manzil, ariza turi va ariza matnini bosqichma-bosqich so‘raydi va chiroyli ko‘rinishda arizani chiqaradi.

---

## ⚙️ Texnologiyalar

* Python 3.11+
* Aiogram 3.x (async/await bilan ishlaydi)
* FSM (Finite State Machine) yordamida shaklni to‘ldirish
* Inline va Reply tugmalar

---

## 📦 Loyihani ishga tushirish

### 1. Klonlash

```bash
git clone [https://github.com/your-username/ariza-bot.git](https://github.com/nematovN/repition_exam_1.git)
cd repition_exam
```

### 2. Virtual muhit yaratish

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

### 3. Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

Agar `requirements.txt` mavjud bo‘lmasa, quyidagilarni o‘rnating:

```bash
pip install aiogram==3.4.1
```

### 4. `main.py` faylini ishga tushirish

```bash
python main.py
```

---

## 🔑 Token sozlash

`main.py` faylida quyidagiga o‘zingizning bot tokeningizni yozing:

```python
TOKEN = "YOUR_BOT_TOKEN"
```

---

## 🧹 Loyihaning tarkibi

```
ariza-bot/
├── main.py                # Bot ishga tushiruvchi fayl
├── forms.py               # FSM holatlari
├── keyboards.py           # Tugma joylashuvlari
├── handlers/
│   ├── menu.py            # Start, Aloqa, Ma'lumot handlerlari
│   └── form_handlers.py   # Ariza to‘ldirish jarayoni bosqichlari
└── README.md              # Ushbu fayl
```

---

## 📋 Bot imkoniyatlari

* 📄 Ariza yuborish
* ℹ️ Bot haqida ma’lumot
* 📞 Administrator bilan aloqa
* ✍️ Ariza to‘ldirishni bosqichma-bosqich so‘rash
* ✅ Tasdiqlash yoki ❌ Bekor qilish

---

## 🔐 Qo‘shimcha imkoniyatlar (keyinchalik)

* 📥 Admin foydalanuvchiga arizani yuborish
* 📄 SQLite yoki PostgreSQL ga saqlash
* 📄 PDF yoki Excel formatga chiqarish

---

## 📬 Bog‘lanish

* Telegram: [@admin\_username](https://t.me/admin_username)
* Email: [admin@example.com](mailto:admin@example.com)

---

> Ushbu bot o‘quvchilar, talabalar, fuqarolar yoki ish beruvchilardan arizalarni qulay qabul qilish uchun mo‘ljallangan.
