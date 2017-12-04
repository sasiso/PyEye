import abc


class IDetection(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def detect(self, image_1, image_2):
        return False


class DetectionStub(IDetection):
    def __init__(self):
        pass

    def detect(self, image_1, image_2):
        return False
