import logging
logger = logging.getLogger(__name__)


class BaseHandler:
    def __init__(self):
        logger.debug("init")
        self.command_id = None
        self.command = None
        self.command_args = []

    def run(self, command, command_args, command_id):
        self.command_id = command_id
        self.command = command
        self.command_args = command_args

    def get_command_name(self):
        return None
