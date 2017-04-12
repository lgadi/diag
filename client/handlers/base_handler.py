import logging
logger = logging.getLogger(__name__)


class BaseHandler:
    def __init__(self):
        logger.debug("init")

    def run(self, args):
        logger.debug("run")
