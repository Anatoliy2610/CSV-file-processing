install:
	pip install -r requirements.txt

test:
	pytest -v

check:
	ruff check

format:
	ruff format


run:
	python3 main.py --file tests/fixtures/file1.csv
	python3 main.py --file tests/fixtures/file1.csv --where "rating>4.7"
	python3 main.py --file tests/fixtures/file1.csv --where "brand=apple"
	python3 main.py --file tests/fixtures/file1.csv --aggregate "rating=avg"
	python3 main.py --file tests/fixtures/file1.csv --where "brand=xiaomi" --aggregate "rating=min"