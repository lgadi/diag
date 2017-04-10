from flask import Flask
import logging
from common.config import Config

logger = logging.getLogger(__name__)
config = Config().config
app = Flask(__name__)


@app.route("/")
def hello():
    return "diag server v0.11"


@app.route("/client/<client_id>/poll")
def poll(client_id):
    logging.debug('got poll request from %s' % client_id)
    return str('ok')

if __name__ == "__main__":
    app.run(port=config["server"]["port"])
