import abc


class IConfiguration(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def get_capture_interval_sec(self):
        return 1


class ConfigurationStub(IConfiguration):
    def __init__(self):
        pass

    def get_capture_interval_sec(self):
        return 1
