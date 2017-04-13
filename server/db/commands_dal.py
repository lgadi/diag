import logging
from datetime import date, datetime
from .db_access import DbAccess

logger = logging.getLogger(__name__)


class CommandsDal:
    def __init__(self):
        self.db_access = DbAccess()

    def get_commands_for_client(self, client_id):
        cur = self.db_access.query("SELECT id, account, command, date FROM commands WHERE account = %s", (client_id,))
        commands_for_client = []
        for (cmd_id, account, command, cmd_date) in cur:
            logger.debug("id: %s, account: %s, command: %s, date: %s", cmd_id, account, command, cmd_date)
            commands_for_client.append([id, account, command, cmd_date])
        return commands_for_client

    def add_command_for_client(self, client_id, command):
        self.db_access.query_and_commit("INSERT INTO commands (account, command, date) VALUES (%s, %s, %s)",
                                        (client_id, command, datetime.now()))

    def clear_commands_for_client(self, client_id):
        self.db_access.query_and_commit("DELETE FROM commands WHERE account=%s", (client_id,))
