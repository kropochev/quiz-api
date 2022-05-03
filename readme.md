# quiz-api

## Установка
Клонировать этот репозиторий. `git clone https://github.com/kropochev/quiz-api.git`

## Запуск с помощью Docker-Compose
1. Проверить, что `Docker` работает локально.
2. Создать образ `docker-compose build`.
3. Запустить `docker-compose up`.

## Пример запроса
```
curl -X 'POST' \
  'http://0.0.0.0:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 3
}'
```

## Пример ответа
```
{
  "id": 7737,
  "question": "God's sending him up Sinai & Nebo made quite a mountain climber out of this sheepherder",
  "answer": "Moses",
  "created_at": "2014-02-11T22:51:18.019000"
}
```