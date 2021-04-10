from flask import Flask
from flask import request
import redis_client
import utilities
import os
import configparser
import logging

app = Flask(__name__)
UPLOAD_FOLDER = f'{os.getcwd()}/uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

config = configparser.ConfigParser()
config.read('src/config.ini')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_files(request):
    Result = utilities.ValidateArgs(request, "user")
    return Result


@app.route('/files', methods=['GET', 'POST'])
def handle_files():
    """Handles incoming requests to /files api

    Returns:
       Data to requester
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print(request.files)
            return utilities.BuildResponse("Invalid request", 400)
        file = request.files['file']
        if file.filename == '':
            return utilities.BuildResponse("File data is empty", 400)
        if file and allowed_file(file.filename):
            path = os.path.join(
                app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            id = redis_client.CreateImage(path)
            return utilities.BuildResponsePOST("Upload complete", 200, id)
    elif request.method == "GET":
        Result = get_files(request)
        return utilities.BuildResponse(Result, 200)
    else:
        logging.error("Unsupported Method")
        return utilities.BuildResponse("Unsupported type", 500)


if __name__ == "__main__":
    logging.basicConfig(filename="server.log", level=logging.INFO)

    if config["debug"]["enabled"] == "1":
        logging.info("Started with debug enabled")
        app.run(debug=True)
    elif config["debug"]["enabled"] == "0":
        logging.info("Started in release mode")
        app.run(debug=True, port=3818)
    else:
        logging.error("Invalid debug setting"),
        exit(1)
