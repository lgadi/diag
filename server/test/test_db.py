import unittest
from server.db.db_access import DbAccess

class TestDb(unittest.TestCase):
    def test_db_access(self):
        db_access = DbAccess()
        db_access.get_commands_for_client(2)
