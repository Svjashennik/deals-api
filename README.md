# deals-api

# Установка

## Загрузка
```bash
git clone https://github.com/Svjashennik/deals-api.git
cd deals-api
touch .env.dev
```

## В .env.dev
```txt
DEBUG=0
SECRET_KEY='django-insecure--qr=ua3*hxzd&xbs-bxayc8nwq@&=$%4&7#ru_#@ka$odrq+tk'
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1 [::1] 
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
```

## Создание билда
```bash
docker-compose build
```

## Запуск
```bash
docker-compose up -d
```

# Документация

## Csv Response

### Загрузка данных deals.csv

POST запрос на ```/api/deals/csv/```

В тело запроса прикрепленный файл с ключем 'file'

Файл успешно загружен в базу:
201 Created
```json
{
    "status": "success"
}
```

Файл неправильного формата:
400 Bad Request
```json
[
    "wrong file format"
]
```

Пустые данные в файле:
400 Bad Request
```json
{
    "customer": [
        "This field is required."
    ],
    "item": [
        "This field is required."
    ],
    "total": [
        "This field is required."
    ],
    "quantity": [
        "This field is required."
    ],
    "date": [
        "This field is required."
    ]
}
```

### Топ покупателей

GET запрос на ```api/deals/top/```

Вернет список из 5 клиентов потративших наибольшую сумму за весь период

200 OK

```json
[
    {
        "spent_money": 451731,
        "name": "resplendent",
        "gems": [
            "Рубин",
            "Танзанит",
            "Сапфир"
        ]
    },
    {
        "spent_money": 217794,
        "name": "bellwether",
        "gems": [
            "Петерсит",
            "Сапфир"
        ]
    },
    {
        "spent_money": 120419,
        "name": "uvulaperfly117",
        "gems": [
            "Петерсит",
            "Танзанит"
        ]
    },
    {
        "spent_money": 108957,
        "name": "braggadocio",
        "gems": [
            "Изумруд"
        ]
    },
    {
        "spent_money": 100132,
        "name": "turophile",
        "gems": [
            "Рубин",
            "Изумруд"
        ]
    }
]
```