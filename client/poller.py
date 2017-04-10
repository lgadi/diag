import logging
from common.config import Config


class Poller:
    def __init__(self, timer_provider, poller_action_provider):
        self.logger = logging.getLogger(__name__)
        self.poller_action_provider = poller_action_provider()
        self.config = Config().config
        self.enabled = False
        self.t = None
        self.timerProvider = timer_provider

    def state(self):
        return self.enabled

    def poll(self):
        self.poller_action_provider.poll()
        if self.enabled:
            self.start()

    def setstate(self, enabled):
        self.enabled = enabled in ['true', 'True', 'yes', 'Yes', '1']
        if self.enabled:
            self.start()
        else:
            self.stop()

    def start(self):
        self.t = self.timerProvider(self.config.getint("client", "poll_interval"), self.poll)
        self.t.start()

    def stop(self):
        if self.t is not None:
            self.t.cancel()
