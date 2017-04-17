import logging
from threading import Timer

from flask import Flask
from flask import request

from client.poller import Poller
from client.server_poller import ServerPoller
from common.config import Config

logger = logging.getLogger(__name__)
logger.debug("init config")
config = Config().config
logger.debug("done")
app = Flask(__name__)
poller = Poller(Timer, ServerPoller)


@app.route("/")
def hello():
    return "diag client v0.1"


@app.route("/state")
def state():
    logging.debug(request.args.get('enabled'))
    if request.args.get('enabled') is not None:
        poller.setstate(request.args.get('enabled'))
    return str(poller.state())


if __name__ == "__main__":
    app.run(port=config["client"]["port"])
