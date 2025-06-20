from processing_CSV.cli import common_parser
from processing_CSV.builder import get_tabulate


def main():
    args = common_parser()
    print(get_tabulate(filtering=args.where, aggregate=args.aggregate, file_path=args.file, order_by=args.order_by))


if __name__ == "__main__":
    main()
