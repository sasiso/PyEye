import numpy as np
import picamera

from interfaces import ICamera


class RaspberryPiCam(ICamera.ICamera):
    def set_image_frequency(self):
        super().set_image_frequency()

    def register_callback(self, cb):
        super().register_callback(cb)

    def get_last_image(self):
        output = np.empty((512, 512, 3), dtype=np.uint8)
        self._camera.capture(output, 'rgb')
        return output

    def __init__(self):
        self._camera = picamera.PiCamera(resolution=(512, 512), framerate=1)
