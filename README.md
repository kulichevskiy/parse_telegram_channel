# Скрипт скачивает сообщения из публичного телеграм-канала

## Установка

1. Клонируйте этот репозиторий: `git@github.com:kulichevskiy/parse_telegram_channel.git`
2. Перейдите в папку проекта: `cd parse_telegram_channel`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Установите зависимости: `pip install -r requirements.txt`
5. Создайте файл `.env` и добавьте туда ваш `api_key` и `api_hash`

Пример .env:
```
api_key=123456
api_hash=abc123
```

Чтобы узнать, где взять `api_key` и `api_hash`, читайте документацию от библиотеки Telethon: https://docs.telethon.dev/en/stable/basic/signing-in.html