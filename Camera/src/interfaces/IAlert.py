import abc


class IAlert(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def register_callback(self, cb):
        return None

    @abc.abstractclassmethod
    def alert(self):
        return None


class AlertStub(IAlert):
    def register_callback(self, cb):
        return None

    def alert(self):
        return None
