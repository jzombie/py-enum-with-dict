.PHONY: build publish

build:
	python setup.py sdist bdist_wheel

publish-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish:
	twine upload dist/*
