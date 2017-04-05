from flask import Flask
from flask import request
import common.config
from .poller import Poller

config = common.config.config()
app = Flask(__name__)
poller = Poller()


@app.route("/")
def hello():
    return "diag client v0.1"


@app.route("/state")
def state():
    print(request.args.get('enabled'))
    if request.args.get('enabled') is not None:
        poller.setstate(request.args.get('enabled'))
    return str(poller.state())

if __name__ == "__main__":
    app.run(port=config["client"]["port"])