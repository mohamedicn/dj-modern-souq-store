class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class ConnectionError(Error):
    def __init__(self, exception, message):
        self.exception = exception
        self.message = message
        super.__init__(self, exception, message)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Message: {}\n\tException: {}".format(self.message, self.exception)
