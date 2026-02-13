.PHONY: install run test lint

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest -q

lint:
	python -m compileall app
