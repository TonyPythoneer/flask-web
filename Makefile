# docker

.PHONY: up
up:
	docker-compose up

.PHONY: up_prod
up_prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

# precommit

.PHONY: install_precommit
install_precommit:
	python3.7 -m pip install pre-commit flake8 pylint autopep8; \
	pre-commit install; \
	pre-commit autoupdate;
