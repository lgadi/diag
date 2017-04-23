import logging
from .db_access import DbAccess


class ResultsDal:
    def __init__(self):
        self.db_access = DbAccess()

    def save_result(self, client_id, command, filename, date):
        self.db_access.query_and_commit("INSERT INTO results (account, command, filename, date) "
                                        "VALUES (%s, %s, %s, %s)",
                                        (client_id, command, filename, date))
