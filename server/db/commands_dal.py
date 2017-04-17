import logging
from datetime import datetime

from .db_access import DbAccess

logger = logging.getLogger(__name__)


class CommandsDal:
    def __init__(self):
        self.db_access = DbAccess()

    def get_commands_for_client(self, client_id):
        cur = self.db_access.query("SELECT id, account, command, date FROM commands "
                                   "WHERE account = %s "
                                   "ORDER BY date ASC", (client_id,))
        commands_for_client = []
        for (cmd_id, account, command, cmd_date) in cur:
            logger.debug("id: %s, account: %s, command: %s, date: %s", cmd_id, account, command, cmd_date)
            commands_for_client.append({'id': cmd_id, 'client_id': account, 'command': command, 'date': cmd_date})
        return commands_for_client

    def add_command_for_client(self, client_id, command):
        self.db_access.query_and_commit("INSERT INTO commands (account, command, date) VALUES (%s, %s, %s)",
                                        (client_id, command, datetime.now()))

    def pop_command_for_client(self, client_id):
        cmds = self.get_commands_for_client(client_id)
        if len(cmds) > 0:
            cmd = cmds[0]
            self.db_access.query_and_commit("DELETE FROM commands WHERE id = %s AND account = %s",
                                            (cmd['id'], client_id))
            return cmd
        else:
            return None

    def clear_commands_for_client(self, client_id):
        self.db_access.query_and_commit("DELETE FROM commands WHERE account=%s", (client_id,))
