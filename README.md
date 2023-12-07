# Dependencies

Test written in python 3 using python [pytest](https://docs.pytest.org/en) framework.

# Before executing tests

## Requirements

Python 3.8 or later version is required. I recommend to use [pyenv](https://github.com/pyenv/pyenv) for installing
it if it's not installed yet.

## Setup script

To setup tests on Linux/MacOS run

    source setup.sh

on Windows

    setup.bat

## Manual setup

Create virtual environment

    python -m venv .venv

Activate virtual environment on Linux/MacOS

    source .venv/bin/activate

Activate virtual environment on Windows

    .venv\Scripts\activate.bat

Install required packages

    pip install -r requirements.txt

To deactivate virtual environment on Linux/MacOS run

    deactivate

on Windows

    deactivate.bat

# Executing tests

To automatically execute test on Linux/MacOS run

    source run.sh

On Windows

    run.bat

The script will activate virtual environment created by setup script, run tests, generate html report and
deactivate virtual environment

To execute test manually run

    pytest -vvl tests --config=config.yaml --log-level=debug

Where -vv is for verbose reporting. -l for displaying local variables in the report in case of test failure. --config -
path to the config file. --log-level=debug to display detailed information about HTTP requests made during the test 
in case of failure.