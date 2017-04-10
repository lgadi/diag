import logging
import http.client
from common.config import Config
import json


class ServerPoller:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = Config().config

    def poll(self):
        self.logger.info("polling")
        conn = http.client.HTTPConnection(self.config["client"]["poll_host"], self.config["client"]["poll_port"])
        conn.request("GET", self.config["client"]["poll_url"])
        resp = conn.getresponse()
        result = resp.readline()
        json_result = json.loads(result)
        self.logger.info("got command %s (id: %s)", json_result["command"], json_result["id"])
