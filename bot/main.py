import sys
import os
import asyncio

# Добавляем /app в sys.path, чтобы модуль bot находился в Docker
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.config import TELEGRAM_TOKEN, openai_client

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я GPT-бот, твой репетитор по математике. Задай мне вопрос!")

@dp.message()
async def gpt_handler(message: Message):
    try:
        completion = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Ты — репетитор по математике для 5 класса. Помогай просто и понятно."
                },
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        )
        reply = completion.choices[0].message.content
        await message.answer(reply)
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())