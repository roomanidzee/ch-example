# ch-example
Пример по работе с ClickHouse для презентации по предмету

## Генерация тестовых данных
```
cd app
python3 -m virtualenv ch_env
source ch_env/bin/activate
pip install poetry
poetry install
python script.py
```

## Запуск сервера с данными
```
cd docker
docker-compose up -d
```

## Запуск клиента для выполнения запросов
```
docker run -it --rm --network=docker_default yandex/clickhouse-client:19.13 --host=ch-server
```

