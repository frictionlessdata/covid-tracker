.PHONY: all install data github


LEAD := $(shell head -n 1 LEAD.md)


all:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

install:
	pip install -r requirements.txt
	cp -n .env.example .env

data:
	python code/extract.py
	python code/transform.py
	python code/load.py

github:
	sed -i -E "s/@(\w*)/@$(LEAD)/" .github/issue_template.md
	sed -i -E "s/@(\w*)/@$(LEAD)/" .github/pull_request_template.md
