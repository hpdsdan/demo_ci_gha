install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest --cov

test_ut:
	python -m unittest

lint:
	pylint *.py

format:
	black *.py

all:
	install lint test