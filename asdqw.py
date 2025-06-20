from tabulate import tabulate


test_headers = ['name', 'brand', 'price', 'rating']
test_data = [
    ['iphone 15 pro', 'apple', '999', '4.9'],
    ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
    ['redmi note 12', 'xiaomi', '199', '4.6'],
    ['poco x5 pro', 'xiaomi', '299', '4.4']
    ]
# print(tabulate(tabular_data=test_data, headers=test_headers, tablefmt="psql"))



def func(*args, **kwargs):
    print(f'args - {args}, \nkwargs - {kwargs}')

# print(func(*test_data, name=123, pape=456))
