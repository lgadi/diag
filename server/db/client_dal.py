import logging
from .db_access import DbAccess


class ClientDal:
    def __init__(self):
        self.db_access = DbAccess()

    def save_client(self, client_id, date):
        self.db_access.query_and_commit("INSERT INTO customers (account, lastSeen) "
                                        "VALUES (%s, %s) ON DUPLICATE KEY UPDATE lastSeen = %s",
                                        (client_id, date, date))