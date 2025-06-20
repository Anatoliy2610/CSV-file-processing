import pytest
from processing_CSV.builder import get_tabulate


@pytest.mark.parametrize(
    "file_path, filtering, aggregate, order_by, result_file_path",
    [
        ("tests/fixtures/file1.csv", "", "", "", "tests/fixtures/results/result1.txt"),
        (
            "tests/fixtures/file1.csv",
            "brand=xiaomi",
            "",
            "",
            "tests/fixtures/results/filter/result1.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "brand=samsung",
            "",
            "",
            "tests/fixtures/results/filter/result2.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "brand!=apple",
            "",
            "",
            "tests/fixtures/results/filter/result3.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "",
            "rating=desc",
            "tests/fixtures/results/order_by/result1.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "",
            "price=asc",
            "tests/fixtures/results/order_by/result2.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "price=min",
            "",
            "tests/fixtures/results/aggregate/result1.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "rating=max",
            "",
            "tests/fixtures/results/aggregate/result2.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "price=avg",
            "",
            "tests/fixtures/results/aggregate/result3.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "rating=avg",
            "",
            "tests/fixtures/results/aggregate/result4.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "brand=xiaomi",
            "",
            "rating=desc",
            "tests/fixtures/results/result2.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "brand=xiaomi",
            "",
            "price=asc",
            "tests/fixtures/results/result2.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "brand>xiaomi",
            "",
            "",
            "tests/fixtures/results/errors/result1.txt",
        ),
        ("", "", "rating=avg", "", "tests/fixtures/results/errors/result2.txt"),
        (
            "tests/fixtures/file1.csv",
            "",
            "rating=qwerty",
            "",
            "tests/fixtures/results/errors/result3.txt",
        ),
        (
            "tests/fixtures/file1.csv",
            "",
            "",
            "123=asc",
            "tests/fixtures/results/errors/result4.txt",
        ),
    ],
)
def test_get_tabulate(file_path, filtering, aggregate, order_by, result_file_path):
    with open(result_file_path, "r") as file:
        exp_result = file.read()
    assert (
        get_tabulate(
            file_path=file_path,
            filtering=filtering,
            aggregate=aggregate,
            order_by=order_by,
        )
        == exp_result
    )
