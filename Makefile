load:
	python src/etl/loader.py

test:
	pytest

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf logs/*
	