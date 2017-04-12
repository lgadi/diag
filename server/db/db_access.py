import mysql.connector
from datetime import date, datetime
import logging
logger = logging.getLogger(__name__)


class DbAccess:
    def __init__(self):
        self.mysql_user = 'root'
        self.mysql_password = ''
        self.mysql_host = '127.0.0.1'
        self.mysql_port = 3306
        self.mysql_database = 'diagnostics'
        self.cnx = mysql.connector.connect(user=self.mysql_user, password=self.mysql_password, host=self.mysql_host,
                                           port=self.mysql_port)
        self.cnx.database = self.mysql_database

    def get_commands_for_client(self, client_id):
        query = "SELECT id, account, command, date FROM commands WHERE account = %s"
        cur = self.cnx.cursor()
        cur.execute(query, (client_id,))
        commands_for_client = []
        for (cmd_id, account, command, cmd_date) in cur:
            logger.debug("id: %s, account: %s, command: %s, date: %s", cmd_id, account, command, cmd_date)
            commands_for_client.append([id, account, command, cmd_date])
        return commands_for_client

    def add_command_for_client(self, client_id, command):
        query = "INSERT INTO commands (account, command, date) VALUES (%s, %s, %s)"
        cur = self.cnx.cursor()
        cur.execute(query, (client_id, command, datetime.now()))
        self.cnx.commit()

    def clear_commands_for_client(self, client_id):
        query = "DELETE FROM commands WHERE account=%s"
        cur = self.cnx.cursor()
        cur.execute(query, (client_id,))
        self.cnx.commit()
