from common.config import Config
import logging
logger = logging.getLogger(__name__)


class Poller:
    def __init__(self, timer_provider, poller_action_provider):
        self.poller_action_provider = poller_action_provider()
        self.config = Config().config
        self.enabled = False
        self.t = None
        self.timerProvider = timer_provider
        self.error_state = False

    def state(self):
        return self.enabled

    def poll(self):
        try:
            self.poller_action_provider.poll()
            if self.error_state:  # we're recovering from connection refused
                self.error_state = False
                logger.info("connection restored")
        except ConnectionRefusedError as cre:
            logger.warning("server seems to be down, will retry (%s)", format(cre))
            self.error_state = True

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
