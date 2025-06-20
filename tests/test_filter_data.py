from processing_CSV.data_processor import get_filter_data
from processing_CSV.utils import open_file


def test_get_filter_data():
    data = open_file('tests/fixtures/file1.csv')
    assert get_filter_data(data_file=data, symbol='=', name_col='brand', data='apple') == [['iphone 15 pro', 'apple', '999', '4.9']]
    assert get_filter_data(data_file=data, symbol='=', name_col='brand', data='samsung') == [['galaxy s23 ultra', 'samsung', '1199', '4.8']]
    assert get_filter_data(data_file=data, symbol='=', name_col='brand', data='xiaomi') == [
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
        ]
    assert get_filter_data(data_file=data, symbol='!=', name_col='brand', data='samsung') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
        ]
    assert get_filter_data(data_file=data, symbol='!=', name_col='brand', data='xiaomi') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ]
    assert get_filter_data(data_file=data, symbol='=', name_col='brand', data='qwerty') == []
    assert get_filter_data(data_file=data, symbol='>', name_col='price', data='300') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ]
    assert get_filter_data(data_file=data, symbol='<', name_col='price', data='300') == [
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]
    assert get_filter_data(data_file=data, symbol='>=', name_col='price', data='999') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ]
    assert get_filter_data(data_file=data, symbol='<=', name_col='price', data='299') == [
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]
    assert get_filter_data(data_file=data, symbol='=', name_col='price', data='300') == []
    assert get_filter_data(data_file=data, symbol='=', name_col='price', data='199') == [['redmi note 12', 'xiaomi', '199', '4.6']]
    assert get_filter_data(data_file=data, symbol='!=', name_col='price', data='299') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ['redmi note 12', 'xiaomi', '199', '4.6']
    ]

    assert get_filter_data(data_file=data, symbol='>', name_col='rating', data='4.7') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ]
    assert get_filter_data(data_file=data, symbol='<', name_col='rating', data='4.7') == [
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]
    assert get_filter_data(data_file=data, symbol='>=', name_col='rating', data='4.8') == [
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ]
    assert get_filter_data(data_file=data, symbol='<=', name_col='rating', data='4.6') == [
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]
    assert get_filter_data(data_file=data, symbol='=', name_col='rating', data='4.9') == [['iphone 15 pro', 'apple', '999', '4.9']]
    assert get_filter_data(data_file=data, symbol='!=', name_col='rating', data='4.9') == [
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]

