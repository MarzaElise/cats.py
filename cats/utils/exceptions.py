

class HTTPException(Exception):
    """
    Raised when the API does not return a 2xx-3xx status code
    """


class NotFound(HTTPException):
    """
    Raised when the API returns a 404 status code
    Derives from HTTPException
    """

class Forbidden(HTTPException):
    """
    Raised when the API returns a 403 status code
    Derives from HTTPException
    """

class ServerError(HTTPException):
    """
    Raised when the server returns a 5xx status code
    """

