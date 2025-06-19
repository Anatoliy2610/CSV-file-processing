from processing_CSV.cli import common_parser
from processing_CSV.builder import get_tabulate


def main():
    args = common_parser()
    print(get_tabulate(args.file, args.where, args.aggregate))


if __name__ == "__main__":
    main()
