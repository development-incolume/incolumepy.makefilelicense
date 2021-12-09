.DEFAULT_GOAL := help

setup: ## setup environment python with poetry
setup:
	@poetry env use 3.10

install:  ## Install this package using poetry
install: setup
	@poetry add incolumepy.makefilelicense

license-gnu-agpl-v3: ## Generate LICENSE file with GNU Affero General Public License v3.0
	@echo GNU Affero General Public License v3.0
	@license-agpl

license-gnu-gpl-v3:  ## Generate LICENSE file with GNU General Public License v3.0
	@echo GNU General Public License v3.0
	@license-gpl

license-gnu-lgpl-v3:  ## Generate LICENSE file with GNU Lesser General Public License v3.0
	@echo GNU Lesser General Public License v3.0
	@license-lgpl

license-mozilla-v2:  ## Generate LICENSE file with Mozilla Public License 2.0
	@echo Mozilla Public License 2.0
	@license-mpl

license-apache-v2:  ## Generate LICENSE file with Apache License 2.0
	@echo Apache License 2.0
	@license-apache

license-mit:  ## Generate LICENSE file with MIT License
	@echo MIT License
	@license-mit

license-boost-v1:  ## Generate LICENSE file with Boost Software License 1.0
	@echo Boost Software License 1.0
	@license-bsl

license-cc0:  ## Generate LICENSE file with Creative Commons Legal Code
	@echo Creative Commons Legal Code
	@license-cc0

unlicense:  ## Software unlicense
	@echo The Unlicense
	@unlicense

.PHONY: clean clean-all flake8 format help lint mypy prerelease release test tox

help:  ## Show this instructions
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

mypy: ## mypy checking
	@echo "mypy checking .."
	@mypy incolumepy/

flake8: ## flake8 checking
	@echo "flake8 checking .."
	@flake8 --config pyproject.toml incolumepy/

check-isort:  ## check isort
	@echo "isort checking .."
	@isort --check --atomic --py all incolumepy/ tests/

isort:  ## isort apply
	@isort --atomic --py all incolumepy/ tests/ && git commit -m "Applied Code style isort format automaticly at `date +"%F %T"`" . || echo
	@echo ">>>  Applied code style isort format automaticly  <<<"

check-black: ## black checking
	@echo "Black checking .."
	@black --check incolumepy/ tests/

black:  ##Apply code style black format
	@poetry run black incolumepy/ tests/ && git commit -m "Applied Code style Black format automaticly at `date +"%F %T"`" . || echo
	@echo ">>>  Applied code style Black format automaticly  <<<"

.PHONY: check-docstyle
check-docstyle: ## docstring checking
	@echo "docstyle checking .."
	@pydocstyle incolumepy/ tests/

pylint:  ## pylint checking
	@echo "pylint checking .."
	@pylint incolumepy/ tests/

lint:  ## Run all linters (check-isort, check-black, flake8, pylint, mypy, docstyle)
lint: mypy pylint flake8 check-docstyle check-isort check-black

test: ## Run all tests avaliable and generate html coverage
test: lint
	@pytest  tests/ -vv --cov=incolumepy.makefilelicense --cov-report='html'

clean: ## Shallow clean into environment (.pyc, .cache, .egg, .log, et all)
	@echo -n "Cleanning environment .."
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*.log' -exec rm -f {} \;
	@find ./ -name ".cache" -exec rm -fr {} \;
	@find ./ -name "*.egg-info" -exec rm -rf {} \;
	@find ./ -name "*.coverage" -exec rm -rf {} \;
	@rm -rf docs/_build
	@echo " Ok."

clean-all: ## Deep cleanning into environment (dist, build, htmlcov, .tox, *_cache, et all)
clean-all: clean
	@echo -n "Deep cleanning .."
	@rm -rf dist
	@rm -rf build
	@rm -rf htmlcov
	@rm -rf .tox
	@rm -rf ".pytest_cache" ".mypy_cache"
	@#fuser -k 8000/tcp &> /dev/null
	@poetry env list|awk '{print $1}'|while read a; do poetry env remove $${a}; done
	@echo " Ok."

prerelease: ## Generate new prerelease commit version default semver
prerelease: test format
	@v=$$(poetry version prerelease); poetry run pytest tests/ && git commit -m "$$v" pyproject.toml $$(find -name version.txt)  #sem tag

release: test ## Generate new release commit with version/tag default semver
	@msg=$$(poetry version patch); poetry run pytest tests/; \
git commit -m "$$msg" pyproject.toml $$(find -name version.txt) \
&& git tag -f $$(poetry version -s) -m "$$msg"; \
git checkout main; git merge --no-ff dev -m "$$msg" \
&& git tag -f $$(poetry version -s) -m "$$msg" \
&& git checkout dev

format: ## Formate project code with code style (isort, black)
format: clean isort black

tox: ## Run tox completly
	@poetry run tox
