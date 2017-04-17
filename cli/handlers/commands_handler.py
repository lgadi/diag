import logging

from .handler_base import HandlerBase

logger = logging.getLogger(__name__)


class CommandsHandler(HandlerBase):
    def __init__(self):
        logger.debug("init")

    def add(self, command):
        logger.debug("add")
        print("add")
        return "command added " + command

    def handler_name(self):
        return "commands"
