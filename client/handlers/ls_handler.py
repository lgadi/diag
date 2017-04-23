import logging
import subprocess
import threading

from .bash_handler import BashHandler

logger = logging.getLogger(__name__)


class LsHandler(BashHandler):

    def get_command_name(self):
        return "ls"