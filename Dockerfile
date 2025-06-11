FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

COPY . .

RUN uv pip install --system .


RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "cashflow.wsgi:application", "--bind", "0.0.0.0:8000"]