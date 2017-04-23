import json
import logging
import os
from datetime import datetime
from urllib.parse import unquote
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


from flask import Flask

from common.config import Config
from server.command_manager import CommandManager
from server.db.commands_dal import CommandsDal
from server.db.results_dal import ResultsDal
from server.db.client_dal import ClientDal

logger = logging.getLogger(__name__)
config = Config().config
app = Flask(__name__)
command_manager = CommandManager()


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


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
@crossdomain(origin='*')
def list(client_id):
    logger.debug('got list request for client %s' % client_id)
    json_result = json.dumps(command_manager.get_all_commands_for_client(client_id))
    return json_result


@app.route("/client/<client_id>/poll")
def poll(client_id):
    client_dal = ClientDal()
    client_dal.save_client(client_id, datetime.now())
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
            logger.info("received file, client_id: %s, command_id: %s, filename: %s, file size: %s",
                        request.args['client_id'], full_path_filename, request.args['command_id'],
                        os.stat(full_path_filename).st_size)
            results_dal = ResultsDal()
            results_dal.save_result(request.args['client_id'], request.args['command'], full_path_filename,
                                    datetime.now())
            return 'file uploaded'
    return 'ok'


if __name__ == "__main__":
    app.run(port=config["server"]["port"])
