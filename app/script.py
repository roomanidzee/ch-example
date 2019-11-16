import time
import random
from enum import IntEnum
from datetime import datetime

import lya
from clickhouse_driver import Client

config = lya.AttrDict.from_yaml('config.yml')
ch_config = config['clickhouse']


class MatchTypeEnum(IntEnum):
    """Перечисление для хранения типов матча"""
    friendly = 1
    uefa = 2
    fifa = 3


def generate_data():
    """Метод для генерации тестовых данных ClickHouse"""

    input_data = []
    limit = 1_000_000

    print('Генерируем данные')

    for _ in range(limit):

        random_value = random.randint(1, int(time.time()))
        time_obj = datetime.fromtimestamp(random_value)

        input_data.append({
            'match_date': time_obj.date(),
            'record_time': time_obj,
            'home_country': f'Country #{random.randint(1, limit)}',
            'guest_country': f'Country #{random.randint(1, limit)}',
            'home_score': random.randrange(0, 20),
            'guest_score': random.randrange(0, 20),
            'match_type': random.choice(
                [MatchTypeEnum.friendly, MatchTypeEnum.uefa, MatchTypeEnum.fifa]
            ),
            'match_city': f'City #{random.randint(1, limit)}',
            'match_country': f'Country #{random.randint(1, limit)}'
        })

    settings = {'send_logs_level': 'debug'}
    client = Client(**ch_config)

    print('Начинаем вставлять данные..')

    query = '''
    INSERT INTO test_db.football_table 
    (match_date, record_time, home_country, guest_country, home_score, guest_score, math_type, match_city, match_country)
    VALUES
    '''

    client.execute_with_progress(query, input_data, types_check=True, settings=settings)


if __name__ == '__main__':
    generate_data()
