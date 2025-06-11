FROM python:3.11-slim

WORKDIR /app

# Копируем весь проект
COPY . .

# Установка uv и зависимостей (в .venv)
RUN pip install uv && uv sync --frozen

# Сборка статики внутри .venv
RUN .venv/bin/python manage.py collectstatic --noinput

# Запуск gunicorn внутри .venv
CMD [".venv/bin/gunicorn", "cashflow.wsgi:application", "--bind", "0.0.0.0:8000"]
