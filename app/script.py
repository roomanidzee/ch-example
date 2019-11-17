import time
import random
import csv

from enum import IntEnum
from datetime import datetime


class MatchTypeEnum(IntEnum):
    """Перечисление для хранения типов матча"""
    friendly = 1
    uefa = 2
    fifa = 3


def generate_data():
    """Метод для генерации тестовых данных ClickHouse"""

    limit = 1_000_000

    print('Генерируем данные')

    with open('../docker/clickhouse/data.csv', 'w') as csv_file:

        data_writer = csv.writer(csv_file, delimiter=',')
        columns = [
            'match_date',
            'record_time',
            'home_country',
            'guest_country',
            'home_score',
            'guest_score',
            'match_type',
            'match_city',
            'match_country'
        ]
        data_writer.writerow(columns)

        for _ in range(limit):
            random_value = random.randint(1, int(time.time()))
            time_obj = datetime.fromtimestamp(random_value)

            data_writer.writerow([
                time_obj.date().strftime("%Y-%m-%d"),
                time_obj.strftime("%Y-%m-%d %H:%M:%S"),
                f'Country #{random.randint(1, limit)}',
                f'Country #{random.randint(1, limit)}',
                random.randrange(0, 20),
                random.randrange(0, 20),
                random.choice(
                    [
                        MatchTypeEnum.friendly.name,
                        MatchTypeEnum.uefa.name,
                        MatchTypeEnum.fifa.name
                    ]
                ),
                f'City #{random.randint(1, limit)}',
                f'Country #{random.randint(1, limit)}'
            ])

    print('CSV сгенерирован')


if __name__ == '__main__':
    generate_data()
