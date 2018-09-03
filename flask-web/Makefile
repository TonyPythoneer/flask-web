.PHONY: venv
venv:
	apt install -y python3-pip python3-apt python3-setuptools; \
	python3.7 -m venv ./.venv

.PHONY: install_precommit
install_precommit:
	python3.7 -m pip install pre-commit flake8 pylint autopep8; \
	pre-commit install; \
	pre-commit autoupdate;
