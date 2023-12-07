source .venv/bin/activate
pytest -vvl tests/ --config=config.yaml --log-level=debug --html=report.html
deactivate