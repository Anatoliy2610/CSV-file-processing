from processing_CSV.builder import builder_result
from processing_CSV.utils import open_file


def test_builder_result():
    data = open_file('tests/fixtures/file1.csv')
    assert builder_result(data=data) == [
        ['name', 'brand', 'price', 'rating'],
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['poco x5 pro', 'xiaomi', '299', '4.4']
        ]
    assert builder_result(data=data, filtering='rating>4.7') == [
        ['name', 'brand', 'price', 'rating'],
        ['iphone 15 pro', 'apple', '999', '4.9'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8']
        ]
    assert builder_result(data=data, filtering='brand=apple') == [
        ['name', 'brand', 'price', 'rating'],
        ['iphone 15 pro', 'apple', '999', '4.9']
        ]
    assert builder_result(data=data, aggregate='rating=avg') == [['avg'], [4.67]]
    assert builder_result(data=data, filtering='brand=xiaomi', aggregate='rating=min') == [['min'], [4.4]]
