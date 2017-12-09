import cv2

from interfaces import ICamera
import numpy as np

class PCWebCam(ICamera.ICamera):
    def set_image_frequency(self):
        super().set_image_frequency()

    def register_callback(self, cb):
        super().register_callback(cb)

    def get_last_image(self):
        # Capture frame-by-frame
        ret, frame = self._cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = gray.astype(np.uint8)

        return gray

    def __init__(self):
        self._cap = cv2.VideoCapture(0)
