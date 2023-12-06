import functools

import yaml
from _pytest.config import filename_arg, UsageError
from pytest import fixture, Config, StashKey
from yaml.parser import ParserError

from api_wrapper.address_checking_service_client import AddressCheckingServiceClient

config_file_key = StashKey["ConfigFile"]()


def pytest_addoption(parser):
    parser.addoption(
        "--config",
        "--cfg",
        help="Config file to use, defaults to %(default)s",
        action='store',
        dest='config_file_path',
        type=functools.partial(filename_arg, optname="--config"),
    )


class ConfigFilePlugin:
    def __init__(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as config_file:
                self.config = yaml.safe_load(config_file)
        except (FileNotFoundError, ParserError) as err:
            raise RuntimeError('Error loading config file') from err


def pytest_configure(config: Config) -> None:
    config_file_path = config.getoption('config_file_path', default=None)

    if not config_file_path:
        raise UsageError('No config file is specified, use --config option for that')

    config.stash[config_file_key] = ConfigFilePlugin(config_file_path)
    config.pluginmanager.register(config.stash[config_file_key])


def pytest_unconfigure(config: Config) -> None:
    config_file_plugin = config.stash.get(config_file_key, None)

    if config_file_plugin:
        del config.stash[config_file_key]
        config.pluginmanager.unregister(config_file_plugin)


@fixture(scope='session')
def config(pytestconfig: Config):
    """
    Returns configuration object loaded from the configuration file
    """
    config_file_plugin = pytestconfig.stash.get(config_file_key, None)

    config = {}

    if config_file_plugin:
        config = config | config_file_plugin.config

    return config


@fixture(scope='session')
def host(config) -> str:
    return config['host']


@fixture(scope='session')
def api_client(host) -> AddressCheckingServiceClient:
    return AddressCheckingServiceClient(host)
