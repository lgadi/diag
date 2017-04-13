import unittest
import logging
from server.db.commands_dal import CommandsDal
import time
logger = logging.getLogger(__name__)


class TestDb(unittest.TestCase):

    def setUp(self):
        self.commands_dal = CommandsDal()

    def test_db_access(self):
        self.commands_dal.get_commands_for_client(2)

    def test_db_insert(self):
        self.commands_dal.clear_commands_for_client(2)
        commands_for_client = self.commands_dal.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")
        self.commands_dal.add_command_for_client(2, "ps -ef")
        self.commands_dal.add_command_for_client(2, "ps -e")
        commands_for_client = self.commands_dal.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 2, "should have 2 commands")
        self.commands_dal.clear_commands_for_client(2)
        commands_for_client = self.commands_dal.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")
        logger.debug(commands_for_client)

    def test_db_clear(self):
        self.commands_dal.clear_commands_for_client(2)
        commands_for_client = self.commands_dal.get_commands_for_client(2)
        self.assertEqual(len(commands_for_client), 0, "should have no commands")

    def test_db_add_pop(self):
        cd = self.commands_dal
        cd.clear_commands_for_client(2)
        cd.add_command_for_client(2, "ps -ef")
        self.assertEqual(len(cd.get_commands_for_client(2)), 1)
        cmd = cd.pop_command_for_client(2)
        self.assertEqual(cmd["command"], "ps -ef")
        self.assertEqual(len(cd.get_commands_for_client(2)), 0, "after pop there should be no more commands")

    def test_db_add_2_pop(self):
        cd = self.commands_dal
        cd.clear_commands_for_client(2)
        cd.add_command_for_client(2, "ps -ef")
        time.sleep(1)
        cd.add_command_for_client(2, "ls -l")
        self.assertEqual(len(cd.get_commands_for_client(2)), 2)
        cmd = cd.pop_command_for_client(2)
        self.assertEqual(cmd["command"], "ps -ef", "command should be ps -ef")
        self.assertEqual(len(cd.get_commands_for_client(2)), 1, "after pop there should be no more commands")


