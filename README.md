![Build Status](https://github.com/Syzhet/syzhet_fastapi/actions/workflows/syzhetfastapi.yml/badge.svg)

# syzhet_fastapi

## REST API - для оформления заказов от пользователей.

Исходный функционал:
- Добавление пользователей и заказов в базу данных.
- Получение пользователей и заказов из базы данных.
- Обновление и удаление пользователей и заказов из базы данных
- Валидация передаваемых значений.
- Документация по API.
- Запуск проекта в docker-контейнерах (FastAPI, postgres, nginx, certbot).
- Автоматическое тестирование и push на Docker Hub при загрузке кода на GitHub.
- Автоматический деплой на удаленный сервер.


## Стек технологий 

<div>
  <a href="https://www.python.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://nginx.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/nginx/nginx-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://www.postgresql.org/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>
  <a href ="https://www.docker.com/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  </a>
  <a href="https://github.com/">
    <img src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  </a>
</div>

Версии ПО:

- python: 3.10.4;
- fastapi: 0.85.1;
- uvicorn: 0.19.0;
- Docker: 20.10.18;
- docker-compose: 1.26.0.
- alembic: 1.8.1
- pydantic: 1.10.2
- asyncpg: 0.27.0


# Установка проекта локально
Склонировать репозиторий на локальную машину:
```sh
git clone https://github.com/Syzhet/syzhet_fastapi.git
```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```

Подготовить для работы базу данных

Подготовить для работы файл .env (необходимые переменные окружение можно найти в файле config.py)

Запусите приложение командой:
```sh
uvicorn backend.main:app --reload
```

# Запуск проекта в Docker-контейнерах
Установите Docker и docker-compose
```sh
sudo apt install docker.io 
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Cоздайте файл .env в директории с файлом docker-compose.yaml:
Параметры запуска описаны в файлах docker-compose.yaml.

Запустите docker-compose:
```sh
sudo docker-compose up -d
```

После сборки появляется 4 контейнера:

| Контайнер | Описание |
| ------ | ------ |
| api | контейнер с запущенным приложением FastAPI|
| db | контейнер с базой данных postgres|
| nginx | контейнер с запущенным web-сервером nginx|
| certbot | (опционально) контейнер необходим на удаленном сервере для получения ssl-сертификата (при локальном запуске и отладке можно убрать работу с данным контейнером из docker-compose.yaml)|


## Автор проекта

- [Ионов А.В.](https://github.com/Syzhet) - Python разработчик.