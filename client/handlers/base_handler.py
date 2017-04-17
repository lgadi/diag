import logging
import tempfile

import requests

from common.config import Config

logger = logging.getLogger(__name__)
config = Config().config


class BaseHandler:
    def __init__(self):
        logger.debug("init")
        self.command_id = None
        self.command = None
        self.command_args = []

    def run(self, command, command_args, command_id):
        self.command_id = command_id
        self.command = command
        self.command_args = command_args

    def get_command_name(self):
        return None

    def post_result(self, data):
        fp = tempfile.NamedTemporaryFile()
        fp.write(data.encode())
        fp.flush()
        response = requests.post('http://localhost:8081/client/result?client_id=' + config.get('client', 'client_id') +
                                 '&command_id=' + str(self.command_id),
                                 files={'file': open(fp.name)})
        print(response.content)
