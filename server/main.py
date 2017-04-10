from flask import Flask
import logging
from common.config import Config
import json
from server.command_manager import CommandManager

logger = logging.getLogger(__name__)
config = Config().config
app = Flask(__name__)
command_manager = CommandManager()


@app.route("/")
def hello():
    return "diag server v0.11"


@app.route("/client/<client_id>/poll")
def poll(client_id):
    logging.debug('got poll request from %s' % client_id)
    json_result = json.dumps(command_manager.get_command_for_client(client_id))
    return json_result

if __name__ == "__main__":
    app.run(port=config["server"]["port"])
