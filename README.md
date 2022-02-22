## **Мини-сервис для парсинга access logs Apache  c сохранением в БД**

### Реализованы следующие задачи:
* Стандартная авторизация юзера по токену 
* Парсинг файла с логами access Apache с сохранением в БД
* API: вывод списка логов из БД в виде JSON 
* Фильтрация списка логов по: IP, конкретной дате и выборка по промежутку дат

### Инструменты разработки:

**Стек:**

* Django 3.2.11
* DRF 3.13.1
* PostgreSQL 14 (через сервис docker-compose)


Подгрузите все зависимости в проект, введите в терминале: "pip install -r requirements.txt" либо установите каждый пакет отдельно.

Для запуска сервисов необходимо установить **docker, docker-compose**

После запустите:
```
* docker-compose up -d (установка и запуск сервисов)
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser (можно без email`a)
```

Теперь вы можете начать взаимодействовать с сервисом.
* python manage.py runserver

Чтобы распарсить файл access logs Apache вручную и сохранить в БД, вам необходимо зайти в settings и установить:

MASK_REQUEST_LOGS - запрос логов (по дефолу установлен)
PATH_ACCESS_LOG - прописать путь до файла логов
FILENAME_LOGS - имя файла логов

После, в терминале проекта ввести:
```
python manage.py fill_db_logs
```
**Для работы парсинга файла access logs Apache через cron:**

For Linux:

1) Cоздайте файл sh:

например: 
```
touch run_parser_access_logs_in_bd.sh
```
2) там же в терминале введите:
```
chmod +x run_parser_access_logs_in_bd.sh
```
3) в файле run_parser_access_logs_in_bd.sh

Необходимо прописать и сохранить:
```
#!/bin/bash
source .../aggregator_available_logs/env/bin/activate (активировать оружение проекта)
cd .../aggregator_available_logs/ (путь до manage.py)
python manage.py fill_db_logs
```
.../ - путь от корня до проекта

4) После создаем задачу в crontab:
    
в терминале:
```
crontab -e
```
в файле crontab указываем следующие:
```
* * * * * .../run_parser_access_logs_in_bd.sh
```
.../ - путь от корня

Для заполнения звездочек (установка переодичности выполнения) рекомедую воспользовать https://crontab.guru/ 
### API points:

**1) Авторизация пользователя -**
**/api-token-auth/**
#### Поля для заполнения (POST-запрос) - Body
* username
* password

**получаем Token для дальнейшего прохождения по проекту.**


**2) Вывод списка логов -** **/api/logs/**
#### Поля для заполнения (GET-запрос)
в Params (фильтрация)
* ip_address (по IP)
* date_add (по дате создания логов)
* date_range_after и date_range_before (для выборки по промежутку дат)

формат ввода дат: 2021-12-31


#### в качестве тестирования прошу использовать приложение postman, либо сайт https://www.postman.com/
