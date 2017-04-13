import logging
from server.db.commands_dal import CommandsDal
logger = logging.getLogger(__name__)


class CommandManager:
    def __init__(self):
        logger.debug("init")
        self.commands_dal = CommandsDal()

    def get_command_for_client(self, client_id):
        logger.debug("get command for %s", client_id)
        command_for_client = self.commands_dal.pop_command_for_client(client_id)
        logger.debug(command_for_client)
        if command_for_client is not None:
            return {'command': command_for_client["command"], 'id': command_for_client["id"]}
        return None
