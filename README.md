# Before executing tests

## Requirements

Python 3.8 or later version is required. I recommend to use [pyenv](https://github.com/pyenv/pyenv) for installing 
it if it's not installed yet.

## Setup script

To setup tests on Linux/MacOS run 
            
    source setup.sh

## Manual setup
  
Create virtual environment 

    python -m venv .venv

Activate virtual environment

    source .venv/bin/activate

Install required packages

    pip install -r requirements.txt

To deactivate virtual environment run

    deactivate

# Executing tests

    source run.sh

Manually execute

    pytest -vvl test.py --config=config.yaml
