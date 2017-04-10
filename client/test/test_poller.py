import unittest
from unittest.mock import MagicMock
from client.poller import Poller
from threading import Timer



class TestMain(unittest.TestCase):
    def test_poller_start(self):
        MockTimer = Timer
        MockTimer.start = MagicMock(return_value=3)
        poller = Poller(MockTimer)
        poller.start()
        MockTimer.start.assert_called_with()

    def test_poller_stop(self):
        MockTimer = Timer
        MockTimer.start = MagicMock()
        MockTimer.cancel = MagicMock()
        poller = Poller(MockTimer)
        poller.start()
        MockTimer.start.assert_called_with()
        poller.stop()
        MockTimer.cancel.assert_called_with()

    def test_poller_stop_without_start(self):
        MockTimer = Timer
        MockTimer.start = MagicMock()
        MockTimer.cancel = MagicMock()
        poller = Poller(MockTimer)
        poller.stop()
        MockTimer.cancel.assert_not_called()

