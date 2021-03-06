from flask.globals import request
import json
import uuid


def ValidateArgs(args, key):
    """Validates query strings

    Args:
        args (request): request from flask
        key (string): key to validate

    Returns:
        string: value from key
    """
    if request.args.get(key) != None:
        return request.args['user']
    else:
        return "Invalid query"


def BuildResponse(msg, code):
    """Builds json response to requester

    Args:
        msg (string): message body
        code (int): status code

    Returns:
        json: built json body with code and msg
    """
    data = {}
    data['code'] = code
    data['msg'] = msg
    return json.dumps(data), code


def GenerateUUID():
    return uuid.uuid4()
