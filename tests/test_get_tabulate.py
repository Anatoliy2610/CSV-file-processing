import pytest
from tabulate import tabulate

from processing_CSV.builder import get_tabulate
from processing_CSV.utils import open_file


test_data = [
    ['name', 'brand', 'price', 'rating'],
    ['iphone 15 pro', 'apple', '999', '4.9'],
    ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ['redmi note 12', 'xiaomi', '199', '4.6'],
    ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]


test_filtering = [
    {'filtering': 'brand=apple', 'result': [['iphone 15 pro', 'apple', '999', '4.9']]},
    {'filtering': 'brand=samsung', 'result': [['galaxy s23 ultra', 'samsung', '1199', '4.8']]},
    {'filtering': 'brand=xiaomi', 'result': [['redmi note 12', 'xiaomi', '199', '4.6'], ['poco x5 pro', 'xiaomi', '299', '4.4']]},
    {'filtering': 'brand!=apple', 'result': [
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
        ]},
    {'filtering': 'brand!=samsung', 'result': [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]},
    {'filtering': 'brand!=xiaomi', 'result': [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8']
        ]},
]

test_aggregate = [
    {'aggregate': 'rating=min', 'result': [['4.4']], 'headers': ['min']},
    {'aggregate': 'rating=max', 'result': [['4.9']], 'headers': ['max']},
    {'aggregate': 'rating=avg', 'result': [['4.67']], 'headers': ['avg']},
    {'aggregate': 'price=min', 'result': [['199']], 'headers': ['min']},
    {'aggregate': 'price=max', 'result': [['1199']], 'headers': ['max']},
    {'aggregate': 'price=avg', 'result': [['674']], 'headers': ['avg']},
]


def test_get_tabulate():
    file_path = 'tests/fixtures/file1.csv'
    error_file_path = 'file_path_not_found.csv'

    assert open_file(file_path) == test_data

    assert get_tabulate(file_path=file_path) == tabulate(tabular_data=test_data[1:], headers=test_data[0], tablefmt="psql")
    assert get_tabulate(file_path=error_file_path) == tabulate(tabular_data=[['Путь до файла указан неверно']], headers=['Ошибка'], tablefmt="psql")

    for test_filter in test_filtering:
        assert get_tabulate(
            file_path=file_path,
            filtering=test_filter.get('filtering')
            ) == tabulate(tabular_data=test_filter.get('result'), headers=test_data[0], tablefmt="psql")
    assert get_tabulate(
            file_path=file_path,
            filtering='col_not_found=apple'
            ) == tabulate(tabular_data=[['Поле фильтрации указано неверно']], headers=['Ошибка'], tablefmt="psql")
    assert get_tabulate(
            file_path=file_path,
            filtering='brand=brand_not_found'
            ) == tabulate(tabular_data=[[]], headers=test_data[0], tablefmt="psql")
    assert get_tabulate(
            file_path=file_path,
            filtering='brand<apple'
            ) == tabulate(tabular_data=[['Символ (условие) в фильтрации указан неверно']], headers=['Ошибка'], tablefmt="psql")
    
    for test_agg in test_aggregate:
        assert get_tabulate(
            file_path=file_path,
            aggregate=test_agg.get('aggregate')
            ) == tabulate(tabular_data=test_agg.get('result'), headers=test_agg.get('headers'), tablefmt="psql")
    assert get_tabulate(
        file_path=file_path,
        aggregate='col_not_found=avg'
        ) == tabulate(tabular_data=[['Поле агрегации указано неверно']], headers=['Ошибка'], tablefmt="psql")
    assert get_tabulate(
        file_path=file_path,
        aggregate='rating~avg'
        ) == tabulate(tabular_data=[['Символ (условие) агрегации указан неверно']], headers=['Ошибка'], tablefmt="psql")
    assert get_tabulate(
        file_path=file_path,
        aggregate='rating=avg123'
        ) == tabulate(tabular_data=[['Режим агрегации указан неверно']], headers=['Ошибка'], tablefmt="psql")

