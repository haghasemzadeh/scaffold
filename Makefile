install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black src/*.py

lint:
	pylint --disable=R,C src/sum.py 

test:
	python3 -m unittest tests/test_sum.py -v

all: install lint test
