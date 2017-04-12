import logging
logger = logging.getLogger(__name__)


class CommandManager:
    def __init__(self):
        logger.debug("init")
        self.commands_for_clients = {'1': [{'id': 123, 'command': 'ls -l'}],
                                     '2': [{'id': 124, 'command': 'ps -ef'}]}

    def get_command_for_client(self, client_id):
        logger.debug("get command for %s", client_id)
        if client_id in self.commands_for_clients:
            commands_for_client = self.commands_for_clients[client_id]
        else:
            return None
        if len(commands_for_client) > 0:
            return commands_for_client[0]
        return None
