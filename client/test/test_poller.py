import unittest
from unittest.mock import MagicMock
from client.poller import Poller
from threading import Timer


class TestMain(unittest.TestCase):
    def test_poller_start(self):
        mock_timer = Timer
        mock_timer.start = MagicMock()
        poller = Poller(mock_timer)
        poller.start()
        mock_timer.start.assert_called_with()

    def test_poller_stop(self):
        mock_timer = Timer
        mock_timer.start = MagicMock()
        mock_timer.cancel = MagicMock()
        poller = Poller(mock_timer)
        poller.start()
        mock_timer.start.assert_called_with()
        poller.stop()
        mock_timer.cancel.assert_called_with()

    def test_poller_stop_without_start(self):
        mock_timer = Timer
        mock_timer.start = MagicMock()
        mock_timer.cancel = MagicMock()
        poller = Poller(mock_timer)
        poller.stop()
        mock_timer.cancel.assert_not_called()

