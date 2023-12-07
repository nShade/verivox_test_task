call .venv\Scripts\activate.bat
call pytest -vvl tests\ --config=config.yaml --log-level=debug --html=report.html
call deactivate.bat