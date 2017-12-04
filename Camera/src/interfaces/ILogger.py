import abc


class ILogger(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def info(self, message):
        print(message)

    @abc.abstractclassmethod
    def warning(self, message):
        print(message)

    @abc.abstractclassmethod
    def error(self, message):
        print(message)

    @abc.abstractclassmethod
    def exception(self, message):
        print(message)


class LoggerStub(ILogger):
    def __init__(self):
        pass

    def info(self, message):
        print(message)

    def warning(self, message):
        print(message)

    def error(self, message):
        print(message)

    def exception(self, message):
        print(message)
