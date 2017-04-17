import unittest
from threading import Timer
from unittest.mock import MagicMock

from client.poller import Poller
from client.server_poller import ServerPoller

mock_server_poller = ServerPoller
mock_timer = Timer


class TestMain(unittest.TestCase):
    def test_poller_start(self):
        mock_timer.start = MagicMock()
        poller = Poller(mock_timer, mock_server_poller)
        poller.start()
        mock_timer.start.assert_called_with()

    def test_poller_stop(self):
        mock_timer.start = MagicMock()
        mock_timer.cancel = MagicMock()
        poller = Poller(mock_timer, mock_server_poller)
        poller.start()
        mock_timer.start.assert_called_with()
        poller.stop()
        mock_timer.cancel.assert_called_with()

    def test_poller_stop_without_start(self):
        mock_timer.start = MagicMock()
        mock_timer.cancel = MagicMock()
        poller = Poller(mock_timer, mock_server_poller)
        poller.stop()
        mock_timer.cancel.assert_not_called()
