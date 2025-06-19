from tabulate import tabulate

from processing_CSV.utils import open_file, get_symbol_and_value
from processing_CSV.data_processor import get_filter_data, get_aggreagte_data


def builder_result(data: list, filtering: str = None, aggregate: str = None) -> list:
    if filtering:
        values = get_symbol_and_value(filtering)
        filter_data = get_filter_data(
            data_file=data,
            symbol=values['symbol'],
            name_col=values['col_name'],
            data=values['data']
            )
        data = [data[0]] + filter_data
    if aggregate:
        values = get_symbol_and_value(aggregate)
        aggregate_data = get_aggreagte_data(data_file=data, agg=values['data'], name_col=values['col_name'])
        return [[values['data']], aggregate_data]
    return data


def get_tabulate(file_path: str, filtering: str = None, aggregate: str = None) -> str:
    data = open_file(file_path=file_path)
    result = builder_result(data=data, filtering=filtering, aggregate=aggregate)
    return tabulate(
        result[1:],
        headers=result[0],
        tablefmt="psql"
    )
