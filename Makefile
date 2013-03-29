REPO=django/django

all: commits.json run

commits.json: 
	python ./fetch.py $(REPO) commits.json

clean:
	rm -f commits.json

run:
	python -m SimpleHTTPServer 8000

.PHONY: clean