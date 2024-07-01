# Places_Remember.

Данное приложение развернуто на сервисе pythonanywhere. Ознакомиться можно тут:
    https://picnichek.pythonanywhere.com/

### Локальный запуск
* Клонировать репозиторий в локальную папку:
    ```bash
    git clone https://github.com/Picnichek/Places_Remember.git
    cd mysite
    ```
* Создать виртуальное окружение и установить зависимости:
    windows
    ```bash
    python -m venv venv
    sourse venv/Scripts/activate
    pip install -r requirements.txt
    ```
    linux
    ```bash
    python3 -m venv venv
    Sourse venv/bin/activate
    pip install -r requirements.txt
    ```

* Создать базу данных PostgreSQL
    переименовать файл ".env.template" в ".env" и заполнить ".env" в соответствии с вашими данными в корне проекта:
    ```bash
    SECRET_KEY=20061996
    YANDEX_MAPS_API_KEY=somekey # ключ 
    SOCIAL_AUTH_VK_OAUTH2_KEY =12345
    SOCIAL_AUTH_VK_OAUTH2_SECRET=somesecret
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres # имя вашей БД
    POSTGRES_USER=postgres # пользователь
    POSTGRES_PASSWORD=postgres # пароль
    DB_HOST=db
    DB_PORT=5432
    ```
* Cоздание администратора и миграций, а также их применение:
    ```bash
    cd places_remember_project
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
* Запускаем сервер:
    ```bash
    python manage.py runserver
    ```
* Поднимаем контейнеры
    ```bash
    docker compose up -d --build
    ```
* Выполняем миграции:

    ```bash
    docker compose exec web python places_remember_project/manage.py makemigrations
    ```
    ```bash
    docker compose exec web python places_remember_project/manage.py migrate
    ```
* При завершении работы останавливаем контейнеры:

    ```bash
    docker compose down -v
    ```