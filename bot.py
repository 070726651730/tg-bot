from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "7608931409:AAF4n2uL12D_dHQ2hK-igATfAayz-5L14_s"  # Вставь свой токен из BotFather
ADMIN_ID = 1258418262 # Вставь свой Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def forward_message(message: types.Message):
    user = message.from_user
    text = f"{message.text}\n\n👤 *Отправитель:* {user.full_name} (@{user.username})"
    await bot.send_message(ADMIN_ID, text, parse_mode="Markdown")

if name == "main":
    executor.start_polling(dp, skip_updates=True)
