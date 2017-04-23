import logging
import json
from datetime import datetime

from server.db.commands_dal import CommandsDal

logger = logging.getLogger(__name__)


def json_serial(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError


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

    def get_all_commands_for_client(self, client_id):
        logger.debug("get all commands for client %s", client_id)
        commands_for_client = self.commands_dal.get_commands_for_client(client_id)
        return json.dumps(commands_for_client, default=json_serial)
