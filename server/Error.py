from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 500
    message = 'AccessError'

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'