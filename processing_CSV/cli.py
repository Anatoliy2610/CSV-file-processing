import argparse


def common_parser():
    parser = argparse.ArgumentParser(
        description="Скрипт обработки CSV файла"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="чтение файла",
    )
    parser.add_argument(
        "-w",
        "--where",
        help="условия фильтрации",
    )
    parser.add_argument(
        "-agg",
        "--aggregate",
        help="условия агрегации",
    )
    return parser.parse_args()
