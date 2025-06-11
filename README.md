# Cashflow Management System

Веб-приложение для управления движением денежных средств (ДДС).

## Возможности
- Учёт поступлений и списаний денежных средств
- Управление справочниками (статусы, типы, категории, подкатегории)
- Фильтрация и поиск записей
- Современный интерфейс на Bootstrap
- Валидация и бизнес-правила
- Docker + Nginx + Postgres

## Технологии
- Python, Django
- Postgres (Docker) или SQLite (по умолчанию)
- uv (современный менеджер зависимостей)
- Nginx (Docker)

## Быстрый старт (через Docker Compose)

1. Клонируйте репозиторий:
   ```
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. Создайте файл `.env` в корне проекта:
   ```
   POSTGRES_DB=cashflow
   POSTGRES_USER=cashflow
   POSTGRES_PASSWORD=cashflow
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=*
   DATABASE_URL=postgres://cashflow:cashflow@db:5432/cashflow
   ```
3. Соберите и запустите контейнеры:
   ```
   docker-compose up --build
   ```
4. Примените миграции (в новом терминале):
   ```
   docker-compose exec web python manage.py migrate
   ```
5. (Опционально) Создайте суперпользователя:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```
6. Откройте [http://localhost](http://localhost) в браузере.

---

   ```
   pip install uv
   ```
2. Установите зависимости:
   ```
   uv pip install --system
   ```
3. Примените миграции:
   ```
   python manage.py migrate
   ```
4. Запустите сервер:
   ```
   python manage.py runserver
   ```

---

## Структура проекта
- `directories/` — справочники
- `cashflow_records/` — записи ДДС
- `cashflow/` — настройки проекта
- `nginx/` — конфиг nginx для Docker

## Переменные окружения
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` — настройки базы данных
- `DJANGO_SECRET_KEY` — секретный ключ Django
- `DJANGO_DEBUG` — режим отладки (True/False)
- `DJANGO_ALLOWED_HOSTS` — допустимые хосты (например, `*` или `localhost`)
- `DATABASE_URL` — строка подключения к базе данных

---

## Скриншоты

