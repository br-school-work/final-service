from flask import Flask
from flask import request
import redis_client
import utilities
import os
import configparser
import logging

app = Flask(__name__)
UPLOAD_FOLDER = f'{os.getcwd()}/uploaded_files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

config = configparser.ConfigParser()
config.read('config.ini')


def get_files(request):
    Result = utilities.ValidateArgs(request, "user")
    return Result


@app.route('/files')
def handle_files():
    """Handles incoming requests to /files api

    Returns:
       Data to requester
    """
    if request.method == "GET":
        return get_files(request)
    else:
        logging.error("Unsupported Method")
        return "Method unsupported"


if __name__ == "__main__":
    logging.basicConfig(filename="server.log", level=logging.INFO)

    if config["debug"]["enabled"] == "1":
        logging.info("Started with debug enabled")
        app.run(debug=True)
    elif config["debug"]["enabled"] == "0":
        logging.info("Started in release mode")
        app.run(debug=False)
    else:
        logging.error("Invalid debug setting"),
        exit(1)