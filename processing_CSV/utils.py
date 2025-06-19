import csv


def open_file(file_path: str) -> list:
    result = []
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            result.append(row)
    return result


def get_symbol_and_value(data: str) -> dict:
    symbols = ('>', '<', '>=', '<=', '=', '!=')
    for symbol in symbols:
        split_text = data.split(symbol)
        if len(split_text) > 1:
            return {
                'symbol': symbol,
                'col_name': split_text[0].lower().strip(),
                'data': split_text[1].lower().strip()
            }
