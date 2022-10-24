from flask import Flask,abort,Response,jsonify
import logging

from services.service import getResultTask,execStatus,shutDownALlTask


app = Flask(__name__)
app.logger.debug('A value for debugging')

@app.route("/start")
def hello_world():
    return execStatus()
@app.route("/getResult")
def getResult():
    return getResultTask()

@app.route("/shutDownALlTask")
def shutDownALlTaskFFF():
    return shutDownALlTask()


@app.route("/getStatus")
def getStatusFunc():
    return  execStatus()

if __name__ == '__main__':
    app.logger.debug('A value for debugging')

    handler = logging.FileHandler("flask.log")
    app.logger.addHandler(handler)
    app.run(port=52280, host="0.0.0.0",debug=True)