PYTHON ?= python3

.PHONY: test run health clean

test:
	$(PYTHON) -m unittest discover -s tests

run:
	$(PYTHON) -m src.main

health:
	./scripts/healthcheck.sh

clean:
	./scripts/cleanup.sh