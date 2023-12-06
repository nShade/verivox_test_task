source .venv/bin/activate
pytest -vvl test.py --config=config.yaml --html=report.html
deactivate