from flask import Flask
import common.config

config = common.config.config()
app = Flask(__name__)

@app.route("/")
def hello():
    return "diag client v0.1"

if __name__ == "__main__":
    app.run(port=config["client"]["port"])