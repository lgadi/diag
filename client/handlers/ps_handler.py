from .base_handler import BaseHandler
import logging
logger = logging.getLogger(__name__)


class PsHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        logger.debug("init")

    def run(self, args):
        super().run(args)
        logger.debug("run")
        logger.debug("executing ps command with args %s", args)
