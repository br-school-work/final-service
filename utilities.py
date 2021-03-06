from flask.globals import request


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
