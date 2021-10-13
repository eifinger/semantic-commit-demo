.PHONY: clean coverage beta test lint typing
init:
	python -m pip install --upgrade pip flit
	flit install
	pre-commit install
coverage:
	py.test --verbose --cov-report term-missing --cov-report xml --cov=SemanticCommitDemo tests
build:
	flit build
clean:
	rm -rf dist/
publish:
	flit --repository pypi publish
beta:
	flit --repository testpypi publish
test:
	py.test tests
lint:
	flake8 SemanticCommitDemo
	pylint --rcfile=.pylintrc SemanticCommitDemo
	black --check SemanticCommitDemo
typing:
	mypy SemanticCommitDemo
all: test lint typing
