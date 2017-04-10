import logging


class Poller:
    def __init__(self, timerProvider):
        logging.debug("poller init")
        self.enabled = False
        self.t = None
        self.timerProvider = timerProvider

    def state(self):
        return self.enabled

    def poll(self):
        logging.debug("polling")
        if self.enabled:
            self.start()

    def setstate(self, enabled):
        self.enabled = enabled in ['true', 'True', 'yes', 'Yes', '1']
        if self.enabled:
            self.start()
        else:
            self.stop()

    def start(self):
        self.t = self.timerProvider(5, self.poll)
        self.t.start()

    def stop(self):
        if self.t is not None:
            self.t.cancel()
