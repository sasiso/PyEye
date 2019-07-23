from application import Application
from capture import camera_factor
from capture.camera_factor import get_camera

from interfaces.IAlert import AlertStub
from interfaces.ICamera import CameraStub

from interfaces.ILogger import LoggerStub

if __name__ == '__main__':
    print("Welcome to PyEye Camera, Staring for you...")

    logger = LoggerStub()
    configuration = None
    camera = get_camera(camera_factor.stubbed_camera)
    detection = None
    alert = AlertStub()

    application = Application(logger=logger,
                              camera=camera,
                              configuration=configuration,
                              detection=detection, alert=alert
                              )

    application.start()
