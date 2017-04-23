import argparse
import http.client
import logging
from urllib.parse import urlencode
import json

from common.config import Config

config = Config().config
logger = logging.getLogger(__name__)
parent_parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument("action", choices=['add', 'list'], type=str, help="action to take (add/list)")
parser.add_argument("client", type=int, help="client id")
parser.add_argument("command", type=str, help="command")


def add(client_id, command):
    logger.debug("adding command %s to client %s", command, client_id)
    conn = http.client.HTTPConnection(config["client"]["poll_host"], config["client"]["poll_port"])
    conn.request("POST", "/client/" + str(client_id) + "/add?" + urlencode({'command': command}))


def list(client_id):
    logger.debug("showing commands for client %s", client_id)
    conn = http.client.HTTPConnection(config["client"]["poll_host"], config["client"]["poll_port"])
    conn.request("GET", "/client/" + str(client_id)+"/list")
    resp = conn.getresponse()
    result = resp.readline()
    json_result = json.loads(result)
    print(json_result)


if __name__ == "__main__":
    logger.info("cli started")
    args = parser.parse_args()
    if args.action == 'add':
        add(args.client, args.command)
    if args.action == 'list':
        list(args.client)
