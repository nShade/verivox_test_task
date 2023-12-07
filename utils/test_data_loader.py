import yaml
from yaml.parser import ParserError


class TestDataLoadError(Exception):
    """Error loading file with test data"""


def load_test_data(path):
    try:
        with open(path, 'r', encoding='utf-8') as data_file:
            return yaml.safe_load(data_file)
    except (FileNotFoundError, ParserError) as err:
        raise TestDataLoadError(f'Error loading test data from {path}') from err
