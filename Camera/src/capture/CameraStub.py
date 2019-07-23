from interfaces import ICamera


class CameraStub(ICamera.ICamera):
    def set_image_frequency(self):
        super().set_image_frequency()

    def register_callback(self, cb):
        super().register_callback(cb)

    def get_last_image(self):
        import numpy
        return numpy.random.randint(0, 255, (512, 512, 3), dtype=numpy.uint8)

    def __init__(self):
        pass
