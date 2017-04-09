import logging
from common.config import Config


class Logger:
    def __init__(self):
        root = logging.getLogger()
        root.setLevel(logging.INFO)
        self.getLogger(__name__).debug("hello logger")


    def getLogger(self, name):
        _logger = logging.getLogger(name)
        _logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s:%(message)s')
        ch.setFormatter(formatter)
        _logger.addHandler(ch)
        return _logger