import configparser

_config = configparser.ConfigParser()
print("reading config")
_config.read('../diag.ini')


def sections():
    return config.sections()


def config():
    return _config
