from .handlers.ps_handler import PsHandler
import logging
logger = logging.getLogger(__name__)


class CommandHandler:
    def __init__(self):
        logger.debug("init")

    def execute_command(self, command, command_id):
        logger.debug("executing command %s, id %s", command, command_id)
        ps_handler = PsHandler()
        ps_handler.run("test")
