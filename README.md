# Тестовые задания Sila Sveta

Репозиторий содержит два тестовых задания для компании Sila Sveta:
1. Сервис сокращения ссылок
2. Сервис загрузки изображений

## Структура репозитория

```
sila-sveta-test/
├── urlshortener/          # Сервис сокращения ссылок
│   ├── manage.py
│   ├── requirements.txt
│   ├── shortener/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   └── templates/
│       └── shortener/
│           ├── base.html
│           ├── create.html
│           ├── list.html
│           ├── success.html
│           └── not_found.html
│
└── imageupload/           # Сервис загрузки изображений
    ├── manage.py
    ├── requirements.txt
    ├── media/
    ├── imageupload/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── image_service/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── urls.py
        ├── views.py
        └── templates/
            ├── base.html
            ├── upload.html
            ├── image_detail.html
            └── image_list.html
```

# 1. Сервис сокращения ссылок

## Описание
Веб-сервис для создания коротких ссылок из длинных URL-адресов.

### Основной функционал:
- Создание коротких ссылок из длинных URL
- Просмотр списка всех созданных ссылок
- Автоматическое перенаправление при переходе по короткой ссылке
- Адаптивный дизайн для мобильных устройств

### Особенности реализации:
- Генерация уникальных коротких идентификаторов
- Обработка длинных URL (до 2000 символов)
- Защита от дубликатов коротких ссылок
- Обработка ошибок при несуществующих ссылках

### Технологии:
- Python 3.12
- Django
- SQLite
- Bootstrap 5.3.2

# 2. Сервис загрузки изображений

## Описание
Веб-сервис для загрузки и хранения изображений с возможностью получения постоянной ссылки.

### Основной функционал:
- Загрузка изображений через веб-форму
- Загрузка изображений через API
- Галерея всех загруженных изображений
- Постоянные ссылки на загруженные изображения
- Пагинация в галерее изображений

### API Endpoints:
- POST `/api/upload/`
  - Content-Type: multipart/form-data
  - Параметры: title (string), image (file)

### Технологии:
- Python 3.8+
- Django
- Django REST Framework
- SQLite3
- Bootstrap 5

## Установка и запуск проектов

### Общие шаги для обоих проектов:

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/sila-sveta-test-repo.git
cd sila-sveta-test-repo
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate  # для Windows
```

### Для запуска сервиса сокращения ссылок:

1. Перейдите в директорию проекта:
```bash
cd urlshortener
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции и запустите сервер:
```bash
python manage.py migrate
python manage.py runserver 8000
```

Сервис будет доступен по адресу: http://localhost:8000

### Для запуска сервиса загрузки изображений:

1. Перейдите в директорию проекта:
```bash
cd imageupload
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции и запустите сервер:
```bash
python manage.py migrate
python manage.py runserver 8000
```

Сервис будет доступен по адресу: http://localhost:8000

## Дополнительная информация

Оба проекта разработаны в качестве тестовых заданий для компании Sila Sveta.