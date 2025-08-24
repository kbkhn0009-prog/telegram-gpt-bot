FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем минимальный HTTP-сервер
RUN pip install gunicorn

COPY . .

# Команда запуска: Telegram-бот + HTTP-заглушка
CMD ["sh", "-c", "gunicorn bot.fake_server:app --bind 0.0.0.0:8080 & python bot/main.py"]
