import unittest
import logging
from server.db.db_access import DbAccess
logger = logging.getLogger(__name__)


class TestDb(unittest.TestCase):
    def test_db_access(self):
        db_access = DbAccess()
        db_access.get_commands_for_client(2)

    def test_db_insert(self):
        db_access = DbAccess()
        db_access.clear_commands_for_client(2)
        commands_for_client = db_access.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")
        db_access.add_command_for_client(2, "ps -ef")
        db_access.add_command_for_client(2, "ps -e")
        commands_for_client = db_access.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 2, "should have 2 commands")
        db_access.clear_commands_for_client(2)
        commands_for_client = db_access.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")
        logger.debug(commands_for_client)

    def test_db_clear(self):
        db_access = DbAccess()
        db_access.clear_commands_for_client(2)
        commands_for_client = db_access.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")
