import os
from dotenv import load_dotenv
from openai import OpenAI
from httpx import Client  # Импорт клиента для OpenAI

# Загружаем переменные из .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Создаём http-клиент без прокси (по умолчанию)
http_client = Client()  # ← Больше не передаём proxies

# Создаём OpenAI клиент
openai_client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=http_client
)
