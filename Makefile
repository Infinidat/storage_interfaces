default: test

test: env
	.env/bin/pytest -x tests

env: .env/.up-to-date


.env/.up-to-date: setup.py
	virtualenv .env
	.env/bin/pip install -e ".[testing]"
	.env/bin/pip install pytest
	touch $@

