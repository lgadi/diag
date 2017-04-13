import mysql.connector
import logging
from common.config import Config
logger = logging.getLogger(__name__)


class DbAccess:
    def __init__(self):
        config = Config().config
        self.cnx = mysql.connector.connect(user=config["database"]["user"], password=config["database"]["password"],
                                           host=config["database"]["host"], port=config["database"]["port"])
        self.cnx.database = config["database"]["database"]

    def reconnect(self):
        config = Config().config
        logger.info("reconnecting")
        self.cnx.reconnect()
        self.cnx.database = config["database"]["database"]

    def query(self, query, args):
        self.reconnect()
        cur = self.cnx.cursor()
        cur.execute(query, args)
        return cur

    def query_and_commit(self, query, args):
        self.reconnect()
        cur = self.cnx.cursor()
        cur.execute(query, args)
        self.cnx.commit()
