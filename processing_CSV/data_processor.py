def get_filter_for_brand(data_file: list, brand: str, symbol: str) -> list:
    if symbol == '=':
        return [product for product in data_file[1:] if brand == product[1]]
    return [product for product in data_file[1:] if brand != product[1]]


def get_filter_numeric_data(data_file: list, data: float, symbol: str, name_col: str) -> list:
    for index, col in enumerate(data_file[0]):
        if col.strip() == name_col:
            comparison = {
                '>': lambda x: x > data,
                '<': lambda x: x < data,
                '>=': lambda x: x >= data,
                '<=': lambda x: x <= data,
                '=': lambda x: x == data,
                '!=': lambda x: x != data
            }
            return [product for product in data_file[1:] if comparison[symbol](float(product[index]))]
    return ['Данные отсутствуют']


def get_filter_data(data_file: list, symbol: str, name_col: str, data: str) -> list:
    if symbol not in ('>', '<', '>=', '<=', '=', '!='):
        return ['Символ в фильтрации указан неверно']
    if name_col not in ('price', 'rating', 'brand'):
        return ['Поле фильтрации указано неверно']
    if name_col == 'brand':
        return get_filter_for_brand(data_file=data_file, brand=data, symbol=symbol)
    return get_filter_numeric_data(data_file=data_file, data=float(data), symbol=symbol, name_col=name_col)


def get_aggreagte_data(data_file: list, agg: str, name_col: str) -> list:
    if name_col not in ('price', 'rating'):
        return ['Поле агрегации указано неверно']
    if agg not in ('min', 'max', 'avg'):
        return ['Режим агрегации указан неверно']
    for index, col in enumerate(data_file[0]):
        if col.strip() == name_col:
            if agg == 'avg':
                return [round(sum([float(product[index]) for product in data_file[1:]]) / len(data_file[1:]), 2)]
            if agg == 'min':
                return [min([float(product[index]) for product in data_file[1:]])]
            if agg == 'max':
                return [max([float(product[index]) for product in data_file[1:]])]
            return ['Данные отсутствуют']
