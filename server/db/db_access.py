import mysql.connector
import logging
logger = logging.getLogger(__name__)


class DbAccess:
    def __init__(self):
        self.mysql_user = 'root'
        self.mysql_password = ''
        self.mysql_host = '127.0.0.1'
        self.mysql_port = 3306
        self.mysql_database = 'diagnostics'
        self.cnx = mysql.connector.connect(user=self.mysql_user, password=self.mysql_password, host=self.mysql_host, port=self.mysql_port)
        self.cnx.database = self.mysql_database

    def get_commands_for_client(self, client_id):
        query = "SELECT id, account, command, date FROM commands WHERE account = " + str(client_id)
        cur = self.cnx.cursor()
        cur.execute(query)
        for (id, account, command, date) in cur:
            logger.debug("id: %s, account: %s, command: %s, date: %s", id, account, command, date)