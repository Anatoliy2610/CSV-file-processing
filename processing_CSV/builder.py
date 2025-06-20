from tabulate import tabulate

from processing_CSV.data_processor import MethodFile, MethodFilter, MethodAggregate

class BuilderData:
    def __init__(self, methods: dict):
        self.methods = methods

    def get_builder_data(self):
        data = MethodFile().get_data(file_path=self.methods.get('file_path'))
        data_filter = MethodFilter().get_data(data=data, filter_method=self.methods.get('filtering'))
        data_aggregate = MethodAggregate().get_data(data=data_filter, aggregate_method=self.methods.get('aggregate'))
        return data_aggregate

def get_tabulate(**methods) -> str:
    try:
        result = BuilderData(methods).get_builder_data()
        return tabulate(
            tabular_data=result[1:],
            headers=result[0],
            tablefmt="psql"
        )
    except ValueError as e:
        return tabulate([[e]], headers=['Ошибка'], tablefmt="psql")
    except FileNotFoundError:
        return tabulate([['Путь до файла указан неверно']], headers=['Ошибка'], tablefmt="psql")

