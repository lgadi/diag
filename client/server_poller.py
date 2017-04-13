from common.config import Config
from client.command_handler import CommandHandler
import json
import http.client
import logging
logger = logging.getLogger(__name__)


class ServerPoller:
    def __init__(self):
        self.config = Config().config
        self.command_handler = CommandHandler()

    def poll(self):
        logger.debug("polling")
        conn = http.client.HTTPConnection(self.config["client"]["poll_host"], self.config["client"]["poll_port"])
        conn.request("GET", self.config["client"]["poll_url"])
        resp = conn.getresponse()
        result = resp.readline()
        json_result = json.loads(result)
        logger.info('result: %s', json_result)
        if json_result is not None:
            logger.debug("got command %s (id: %s)", json_result["command"], json_result["id"])
            self.command_handler.execute_command(json_result["command"], json_result["id"])
        else:
            logger.debug('no command')
