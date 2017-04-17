import json
import logging
import os
from urllib.parse import unquote

from flask import Flask, request

from common.config import Config
from server.command_manager import CommandManager
from server.db.commands_dal import CommandsDal

logger = logging.getLogger(__name__)
config = Config().config
app = Flask(__name__)
command_manager = CommandManager()


@app.route("/")
def hello():
    return "diag server v0.11"


@app.route("/client/<client_id>/add", methods=['POST'])
def add_command(client_id):
    cmd = unquote(request.args['command'])
    logger.info("adding command %s to client %s", cmd, client_id)
    cd = CommandsDal()
    cd.add_command_for_client(client_id, cmd)
    return "ok"

@app.route("/client/<client_id>/list")
def list(client_id):
    logger.debug('got list request for client %s' % client_id)
    json_result = json.dumps(command_manager.get_all_commands_for_client(client_id))
    return json_result

@app.route("/client/<client_id>/poll")
def poll(client_id):
    logger.debug('got poll request from %s' % client_id)
    json_result = json.dumps(command_manager.get_command_for_client(client_id))
    logger.debug(json_result)
    return json_result


@app.route('/client/result', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            logger.error('No file part')
            return 'no file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            logger.error('No selected file')
            return 'no selected file'
        if file:
            # filename = secure_filename(file.filename)
            filename = file.filename
            full_path_filename = os.path.join('./uploads', filename)
            file.save(full_path_filename)
            logger.debug("received file, client_id: %s, command_id: %s, filename: %s, file size: %s",
                         request.args['client_id'], full_path_filename, request.args['command_id'],
                         os.stat(full_path_filename).st_size)
            return 'file uploaded'
    return 'ok'


if __name__ == "__main__":
    app.run(port=config["server"]["port"])
