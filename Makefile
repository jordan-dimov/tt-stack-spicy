lint:
	flake8 .
	mypy --ignore-missing .

unit_test:
	pytest

test: lint unit_test
