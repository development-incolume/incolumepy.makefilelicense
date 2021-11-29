.DEFAULT_GOAL := help

setup:
	@poetry env use 3.9

install: setup
	@poetry add incolumepy.makefilelicense

license-gnu-agpl-v3:
	@echo GNU Affero General Public License v3.0
	@license-agpl

license-gnu-gpl-v3:
	@echo GNU General Public License v3.0
	@license-gpl

license-gnu-lgpl-v3:
	@echo GNU Lesser General Public License v3.0
	@license-lgpl

license-mozilla-v2:
	@echo Mozilla Public License 2.0
	@license-mpl

license-apache-v2:
	@echo Apache License 2.0
	@license-apache

license-mit:
	@echo MIT License
	@license-mit

license-boost-v1:
	@echo Boost Software License 1.0
	@license-bsl

license-cc0:
	@echo Creative Commons Legal Code
	@license-cc0

unlicense:
	@echo The Unlicense
	@unlicense

.PHONY: help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test:
	@pytest  tests/ -vv --cov=incolumepy.makefilelicense --cov-report='html'

clean:
	@echo -n "Cleanning environment .."
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*.log' -exec rm -f {} \;
	@find ./ -name ".cache" -exec rm -fr {} \;
	@find ./ -name "*.egg-info" -exec rm -rf {} \;
	@find ./ -name "*.coverage" -exec rm -rf {} \;
	@rm -rf ".pytest_cache"
	@rm -rf docs/_build
	@echo " Ok."

clean-all: clean
	@echo -n "Deep cleanning .."
	@rm -rf dist
	@rm -rf build
	@rm -rf htmlcov
	@rm -rf .tox
	@#fuser -k 8000/tcp &> /dev/null
	@echo " Ok."

format: clean
	@poetry run black incolumepy/ tests/

tox:
	@tox
