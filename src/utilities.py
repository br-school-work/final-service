from flask.globals import request
import json


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
    data = {}
    data['code'] = code
    data['msg'] = msg
    return json.dumps(data)
