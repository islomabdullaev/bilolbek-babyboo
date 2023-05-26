from  aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menuMain = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="BabyBoo Salfetka", callback_data="BabyBoo Salfetka"),
        ],
        [
            InlineKeyboardButton(text="ℹ️BabyBoo UltraSoft", callback_data="ℹ️BabyBoo UltraSoft")
        ],
        [
            InlineKeyboardButton(text="ℹ️BabyBoo Comfort", callback_data="ℹ️BabyBoo Comfort")
        ],
        # [
        #     InlineKeyboardButton(text="☎️Aloqaga chiqish", callback_data="☎️Aloqaga chiqish")
        # ],
        [
            InlineKeyboardButton(text="⌛️Obuna | bo'lish", url="https://t.me/babyboopampers")
        ],
    ],
)
menuPcs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="120talik", callback_data="120talik"),
        ],
        [
            InlineKeyboardButton(text="120talik k",callback_data="120talik k")
        ],
        [
            InlineKeyboardButton(text="72talik", callback_data="72talik")
        ],
        [
            InlineKeyboardButton(text="72talik s",callback_data="72talik s")
        ],
        [
            InlineKeyboardButton(text="↩️Back", callback_data="back2"),
        ],
    ],
)
salfetka_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️Back", callback_data="salfetkalar_back")
        ]
    ],
)

comfort_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️Back", callback_data="comfort_back")
        ]
    ],
)
menuComfort = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣lik razmer: 40ta ichida 1 dona p. 💰1375 so'm",callback_data="1️⃣lik razmer: 40ta ichida 1 dona p. 💰1375 so'm")
        ],
        [
            InlineKeyboardButton(text="2️⃣lik razmer: 38ta ichida 1 dona p. 💰1447 so'm ",callback_data="2️⃣lik razmer: 38ta ichida 1 dona p. 💰1447 so'm")
        ],
        [
            InlineKeyboardButton(text="3️⃣lik razmer: 32ta ichida 1 dona p. 💰1718 so'm ",callback_data="3️⃣lik razmer: 32ta ichida 1 dona p. 💰1718 so'm")
        ],
        [
            InlineKeyboardButton(text="4️⃣lik razmer: 28ta ichida 1 dona p. 💰1964 so'm ",callback_data="4️⃣lik razmer: 28ta ichida 1 dona p. 💰1964 so'm")
        ],
        [
            InlineKeyboardButton(text="5️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm",callback_data="5️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm")
        ],
        [
            InlineKeyboardButton(text="6️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm",callback_data="6️⃣lik razmer: 24ta ichida 1 dona p. 💰2291 so'm")
        ],
        [
            InlineKeyboardButton(text="↩️Back",callback_data="comfort_orqaga")
        ],
    ],
)
Ultraback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️Back", callback_data="babyboo_ultraback")
        ]
    ],
)
menuTil = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿UZB",callback_data="🇺🇿UZB"),
            InlineKeyboardButton(text="🇷🇺RUS",callback_data="🇷🇺RUS")
        ],
    ],
)
menuUltra = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣lik razmer: 52ta ichida 1 dona p. 💰1346 so'm",callback_data="1️⃣lik razmer: 52ta ichida 1 dona p. 💰1346 so'm")
        ],
        [
            InlineKeyboardButton(text="2️⃣lik razmer: 50ta ichida 1 dona p. 💰1400 so'm",callback_data="2️⃣lik razmer: 50ta ichida 1 dona p. 💰1400 so'm")
        ],
        [
            InlineKeyboardButton(text="3️⃣lik razmer: 42ta ichida 1 dona p. 💰1666 so'm",callback_data="3️⃣lik razmer: 42ta ichida 1 dona p. 💰1666 so'm")
        ],
        [
            InlineKeyboardButton(text="4️⃣lik razmer: 36ta ichida 1 dona p. 💰1944 so'm",callback_data="4️⃣lik razmer: 36ta ichida 1 dona p. 💰1944 so'm")
        ],
        [
            InlineKeyboardButton(text="5️⃣lik razmer: 32ta ichida 1 dona p. 💰2187 so'm",callback_data="5️⃣lik razmer: 32ta ichida 1 dona p. 💰2187 so'm")
        ],
        [
            InlineKeyboardButton(text="6️⃣lik razmer: 26ta ichida 1 dona p. 💰2692 so'm",callback_data="6️⃣lik razmer: 26ta ichida 1 dona p. 💰2692 so'm")
        ],
        [
            InlineKeyboardButton(text="↩️Back",callback_data="ultra_back")
        ],
    ]
)
back2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️Back", callback_data="back2")
        ]
    ],
)