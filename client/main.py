from flask import Flask
from flask import request
from common.logger import Logger
from common.config import Config
from client.poller import Poller

logger = Logger().getLogger(__name__)
logger.error("init config")
config = Config().config
logger.debug("done")
app = Flask(__name__)
poller = Poller()


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