source .venv/bin/activate
pytest -vvl test.py --config=config.yaml --log-level=debug --html=report.html
deactivate