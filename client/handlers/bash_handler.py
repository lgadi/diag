import logging
import subprocess
import threading

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)


class BashHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        logger.debug("init")

    def run(self, command, command_args, command_id):
        super().run(command, command_args, command_id)
        logger.debug("run")
        logger.debug("executing command %s with args %s (id: %s)", self.command, self.command_args, self.command_id)
        t = threading.Thread(target=self.async_run)
        t.start()
        logger.debug("started")


    def async_run(self):
        stdoutdata = subprocess.getoutput(" ".join([self.command, " ".join(self.command_args)]))
        logger.debug(stdoutdata)
        logger.debug("will send result for command id %s", self.command_id)
        self.post_result(stdoutdata)
