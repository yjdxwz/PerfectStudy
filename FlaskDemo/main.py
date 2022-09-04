from flask import Flask,abort,Response,jsonify
import logging


app = Flask(__name__)

@app.route("/")
def hello_world():
    resp = Response("失败了")
    app.logger.debug('A value for debugging')

    abort(jsonify({"name":"123"}))
    return "<p>hello dddworld </p>"


if __name__ == '__main__':
    app.logger.debug('A value for debugging')

    handler = logging.FileHandler("flask.log")
    app.logger.addHandler(handler)
    app.run(port=52280, host="0.0.0.0",debug=True)