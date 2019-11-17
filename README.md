# ch-example
Пример по работе с ClickHouse

## Генерация тестовых данных
```
cd app
python3 script.py
```

## Запуск сервера с данными
```
cd docker
docker-compose up -d
```

## Запуск клиента для выполнения запросов
```
cat clickhouse/data.csv | docker run -i --rm --network=docker_default yandex/clickhouse-client:19.13 --host=ch-server --query="INSERT INTO test_db.football_table FORMAT CSVWithNames"
docker run -it --rm --network=docker_default yandex/clickhouse-client:19.13 --host=ch-server
```

