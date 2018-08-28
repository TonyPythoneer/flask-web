#!/bin/bash

# build venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip show pip

# install requirements
pip install -r requirements_dev.txt

# keep alive
echo 'I am alive!'
tail -f /dev/null
