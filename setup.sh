#!/bin/bash

pip install virtualenv
# setup python virtual environment

virtualenv -p python3 venv

# go into the virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt