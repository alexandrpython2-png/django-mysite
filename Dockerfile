FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip "poetry==2.5.1"
# Контейнер и так изолирован, поэтому отдельное виртуальное окружение Poetry не создаёт:
# зависимости ставятся прямо в Python образа
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main --no-interaction --no-ansi

COPY mysite .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
