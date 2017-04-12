from .handlers.ps_handler import PsHandler
import logging
logger = logging.getLogger(__name__)


class CommandHandler:
    def __init__(self):
        logger.debug("init")
        self.commands = [PsHandler()]

    def execute_command(self, command, command_id):
        logger.debug("executing command %s, id %s", command, command_id)
        command_arr = command.split()
        command = command_arr[0]
        command_args = command_arr[1:]
        try:
            command_handler = list(filter(lambda cmd: cmd.get_command_name() == command, self.commands))[0]
            command_handler.run(command, command_args, command_id)
        except IndexError as ie:
            logger.error("command %s not found (%s)", command, format(ie))
