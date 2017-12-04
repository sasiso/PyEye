import abc


class ICamera(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def register_callback(self, cb):
        return None

    @abc.abstractclassmethod
    def set_image_frequency(self):
        return None

    @abc.abstractclassmethod
    def get_last_image(self):
        return None


class CameraStub(ICamera):
    def __init__(self):
        pass

    def register_callback(self, cb):
        return None

    def set_image_frequency(self):
        return None

    def get_last_image(self):
        return None
