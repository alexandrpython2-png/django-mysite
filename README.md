# mysite

Учебный Django-проект курса Skillbox «Python Django»: магазин (`shopapp`), блог (`blogapp`),
профили пользователей (`myauth`), REST API на Django REST framework.

## Зависимости

Зависимости описаны в `pyproject.toml` и зафиксированы в `poetry.lock` (Poetry 2).

```bash
poetry install --no-root
```

## Запуск через Docker Compose

```bash
cp .env.template .env      # и задайте свой DJANGO_SECRET_KEY и адрес сервера
docker compose up -d --build
```

Приложение будет доступно на 80-м порту: `http://<адрес сервера>/shop/`.

- `restart: always` — Docker сам перезапустит приложение, если оно упадёт или сервер перезагрузится.
- В образе Poetry ставит зависимости без отдельного виртуального окружения
  (`poetry config virtualenvs.create false` в `Dockerfile`).
- База SQLite (`mysite/database`) и загруженные файлы (`mysite/uploads`) хранятся на сервере
  в папках, подключённых как volume, и не пропадают при пересборке образа.
- `DJANGO_DEBUG=1` нужен, чтобы Django сам раздавал статику (по условию учебного задания).

Создать администратора:

```bash
docker compose exec app python manage.py createsuperuser
```
