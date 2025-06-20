from abc import ABC, abstractmethod
import csv

class Methods(ABC):
    @abstractmethod
    def get_data(self, data: list, filter_method: str) -> list:
        pass

    def get_symbol_and_value(self, data: str) -> dict:
        symbols = ('>=', '<=', '!=', '=', '>', '<')
        for symbol in symbols:
            split_text = data.split(symbol)
            if len(split_text) > 1:
                return {
                    'symbol': symbol,
                    'col_name': split_text[0].lower().strip(),
                    'data': split_text[1].lower().strip()
                }
        return {}

class MethodFile(Methods):
    def open_file(self, file_path: str) -> list:
        result = []
        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                result.append(row)
        return result

    def get_data(self, file_path: str) -> list:
        if not file_path:
            raise ValueError('Файл не указан')
        data = self.open_file(file_path)
        return data


class MethodFilter(Methods):
    def get_filter_for_brand(self, data_file: list, brand: str, symbol: str) -> list:
        if symbol == '=':
            return [product for product in data_file[1:] if brand == product[1]]
        if symbol == '!=':
            return [product for product in data_file[1:] if brand != product[1]]
        raise ValueError('Символ (условие) в фильтрации указан неверно')

    def get_filter_numeric_data(self, data_file: list, data: float, symbol: str, name_col: str) -> list:
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

    def get_filter_data(self, data_file: list, symbol: str, name_col: str, data: str) -> list:
        if symbol not in ('>', '<', '>=', '<=', '!=', '='):
            raise ValueError('Символ (условие) в фильтрации указан неверно')
        if name_col not in ('price', 'rating', 'brand'):
            raise ValueError('Поле фильтрации указано неверно')
        if name_col == 'brand':
            return self.get_filter_for_brand(data_file=data_file, brand=data, symbol=symbol)
        return self.get_filter_numeric_data(data_file=data_file, data=float(data), symbol=symbol, name_col=name_col)
    
    def get_data(self, data: list, filter_method: str) -> list:
        if filter_method:
            values = self.get_symbol_and_value(filter_method)
            filter_data = self.get_filter_data(
                data_file=data,
                symbol=values.get('symbol'),
                name_col=values.get('col_name'),
                data=values.get('data')
                )     
            data = [data[0]] + filter_data
        return data


class MethodAggregate(Methods):
    def get_aggreagte_data(self, data_file: list, agg: str, name_col: str, symbol: str) -> list:
        if symbol != '=':
            raise ValueError('Символ (условие) агрегации указан неверно')
        if name_col not in ('price', 'rating'):
            raise ValueError('Поле агрегации указано неверно')
        if agg not in ('min', 'max', 'avg'):
            raise ValueError('Режим агрегации указан неверно')
        for index, col in enumerate(data_file[0]):
            if col.strip() == name_col:
                if agg == 'avg':
                    return [round(sum([float(product[index]) for product in data_file[1:]]) / len(data_file[1:]), 2)]
                if agg == 'min':
                    return [min([float(product[index]) for product in data_file[1:]])]
                if agg == 'max':
                    return [max([float(product[index]) for product in data_file[1:]])]

    def get_data(self, data: list, aggregate_method: str) -> list:
        if aggregate_method:
            values = self.get_symbol_and_value(aggregate_method)
            aggregate_data = self.get_aggreagte_data(
                data_file=data,
                agg=values.get('data'),
                name_col=values.get('col_name'),
                symbol=values.get('symbol'))
            return [[values.get('data')], aggregate_data]
        return data

