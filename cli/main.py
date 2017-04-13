import logging
import http.client
from common.config import Config
from urllib.parse import urlencode
import argparse
config = Config().config
logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser()
parser.add_argument("action", type=str, help="action to take (add/show)")
parser.add_argument("-id", "--client_id", type=int, help="client id")
parser.add_argument("-c", "--command", type=str, help="command")


def add(client_id, command):
    logger.debug("adding command %s to client %s", command, client_id)
    conn = http.client.HTTPConnection(config["client"]["poll_host"], config["client"]["poll_port"])
    conn.request("POST", "/client/"+str(client_id)+"/add?"+urlencode({'command': command}))

if __name__ == "__main__":
    logger.info("cli started")
    args = parser.parse_args()
    if args.action == 'add':
        add(args.client_id, args.command)

