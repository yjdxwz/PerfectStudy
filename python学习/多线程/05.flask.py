import flask
import json

app = flask.Flask(__name__)

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "Read file"


def read_db():
    time.sleep(0.2)
    return "Read file"


def read_api():
    time.sleep(0.3)
    return "Read file"


@app.route("/")
def index():
    rsult_file = pool.submit(read_file)
    rsult_db = pool.submit(read_db)
    rsult_api = pool.submit(read_api)
    return json.dumps({
        "result_file": rsult_file.result(),
        "rsult_db": rsult_db.result(),
        "rsult_api": rsult_api.result(),
    })


if __name__ == '__main__':
    app.run()
